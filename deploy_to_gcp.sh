#!/usr/bin/env bash
set -euo pipefail

# Deployment script for Mathmerise to Cloud Run + Cloud SQL
# Usage: run this in Google Cloud Shell or any environment with gcloud authenticated

PROJECT="active-dahlia-453113-p1"
REGION="us-central1"
IMAGE="gcr.io/${PROJECT}/mathmerise:latest"
SECRET_NAME="mathmerise-db-password"
SQL_INSTANCE="mathmerise-pg"
DB_NAME="mathmerise"
SERVICE="mathmerise"

# Generated password (keep this secret). Replace if you prefer your own.
DB_PASSWORD="xLsi25PQyRVDAd&(uq+bL2hi"

# Allow simple overrides from environment variables so you can run:
# PROJECT_OVERRIDE=your-project REGION_OVERRIDE=us-central1 DB_PASSWORD_OVERRIDE=$PWD ./deploy_to_gcp.sh
PROJECT=${PROJECT_OVERRIDE:-$PROJECT}
REGION=${REGION_OVERRIDE:-$REGION}
DB_PASSWORD=${DB_PASSWORD_OVERRIDE:-$DB_PASSWORD}
IMAGE="gcr.io/${PROJECT}/mathmerise:latest"

echo "Using configuration:"
echo "  PROJECT=$PROJECT"
echo "  REGION=$REGION"
echo "  SERVICE=$SERVICE"
echo "  DB_NAME=$DB_NAME"
echo "  SQL_INSTANCE=$SQL_INSTANCE"
echo "  Secret will be created as: $SECRET_NAME"
echo "(DB password is not printed for safety)"

read -p "Proceed with these settings? (type 'y' to continue): " yn
if [ "$yn" != "y" ]; then
  echo "Aborting. You can set overrides via PROJECT_OVERRIDE, REGION_OVERRIDE, DB_PASSWORD_OVERRIDE or edit the script." 
  exit 1
fi

echo "Enabling required Google Cloud APIs..."
gcloud config set project "$PROJECT"
gcloud services enable run.googleapis.com sqladmin.googleapis.com cloudbuild.googleapis.com secretmanager.googleapis.com containerregistry.googleapis.com

echo "Storing DB password in Secret Manager as '$SECRET_NAME'"
if gcloud secrets describe "$SECRET_NAME" --project="$PROJECT" >/dev/null 2>&1; then
  echo "Secret exists; adding new version"
  echo -n "$DB_PASSWORD" | gcloud secrets versions add "$SECRET_NAME" --data-file=- --project="$PROJECT"
else
  echo -n "$DB_PASSWORD" | gcloud secrets create "$SECRET_NAME" --data-file=- --replication-policy="automatic" --project="$PROJECT"
fi

echo "Building and pushing container image: $IMAGE"
gcloud builds submit --tag "$IMAGE"

echo "Creating Cloud SQL instance (if not exists): $SQL_INSTANCE"
if gcloud sql instances describe "$SQL_INSTANCE" --project="$PROJECT" >/dev/null 2>&1; then
  echo "Cloud SQL instance $SQL_INSTANCE already exists"
else
  gcloud sql instances create "$SQL_INSTANCE" \
    --database-version=POSTGRES_15 \
    --tier=db-f1-micro \
    --region="$REGION" \
    --project="$PROJECT"
fi

echo "Creating database '$DB_NAME' and setting postgres password"
gcloud sql databases create "$DB_NAME" --instance="$SQL_INSTANCE" --project="$PROJECT" || true
gcloud sql users set-password postgres --instance="$SQL_INSTANCE" --password="$DB_PASSWORD" --project="$PROJECT"

INSTANCE_CONNECTION_NAME=$(gcloud sql instances describe "$SQL_INSTANCE" --project="$PROJECT" --format="value(connectionName)")
echo "Instance connection name: $INSTANCE_CONNECTION_NAME"

echo "Deploying to Cloud Run service: $SERVICE"
gcloud run deploy "$SERVICE" \
  --image "$IMAGE" \
  --platform managed \
  --region "$REGION" \
  --allow-unauthenticated \
  --add-cloudsql-instances "$INSTANCE_CONNECTION_NAME" \
  --set-env-vars "DB_USER=postgres,DB_NAME=$DB_NAME,INSTANCE_CONNECTION_NAME=$INSTANCE_CONNECTION_NAME,FLASK_ENV=production" \
  --set-secrets "DB_PASSWORD=$SECRET_NAME:latest"

echo "Attempting to create domain mapping for www.mathmerise.com (you may need to finish DNS verification)"
gcloud run domain-mappings create --service "$SERVICE" --domain "www.mathmerise.com" --region "$REGION" --project="$PROJECT" || true

echo "\nDeployment script finished.\n- Check Cloud Run console for the service URL.\n- If domain mapping requires DNS changes, Cloud Run will list required records.\n"
