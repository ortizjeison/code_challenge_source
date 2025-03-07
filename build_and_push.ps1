# Stop on errors
$ErrorActionPreference = "Stop"

# Define variables
$PROJECT_ID = "code-challenge-autoscraping"
$REGION = "us-central1"
$REPO_NAME = "code-challenge-source-repo"
$IMAGE_NAME = "code-challenge-image"
$SERVICE_NAME = "code-challenge-service-cd"

# Define correct full image path
$IMAGE_PATH = "$REGION-docker.pkg.dev/$PROJECT_ID/$REPO_NAME/$IMAGE_NAME"

# Authenticate with GCP (Uncomment if needed)
# Write-Host "Authenticating with GCP..."
# gcloud auth login --quiet
# gcloud config set project $PROJECT_ID


# Enable Artifact Registry if not already enabled
Write-Host "Enabling Artifact Registry service..."
gcloud services enable artifactregistry.googleapis.com

# Authenticate Docker with Artifact Registry
Write-Host "Configuring Docker authentication..."
gcloud auth configure-docker $REGION-docker.pkg.dev

# Build the Docker image (Fix: correctly referencing $IMAGE_PATH)
Write-Host "Building Docker image..."
docker build -t $IMAGE_PATH .

# Print the correctly formatted image path
Write-Host "✅ Docker image path: $IMAGE_PATH"

# Push to Artifact Registry
Write-Host "Pushing Docker image to Artifact Registry..."
docker push $IMAGE_PATH

Write-Host "✅ Docker image successfully pushed to Artifact Registry!"