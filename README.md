## Compilation Instructions

### Before Starting
Ensure `local_run = False` in `env_manager.py`. This is mandatory to run the code successfully in Cloud Run.

### 1. Infrastructure Requirements

1.1 A GCP account with an active project (Project ID: `code-challenge-autoscraping`).

1.2 A BigQuery dataset (`code-challenge-autoscraping.articles_data`) with a table that has the following schema:

| Field Name            | Type    | Mode     |
|-----------------------|---------|----------|
| **title**             | STRING  | NULLABLE |
| **kicker**            | STRING  | NULLABLE |
| **link**              | STRING  | NULLABLE |
| **image**             | STRING  | NULLABLE |
| **word_count_title**  | INTEGER | NULLABLE |
| **char_count_title**  | INTEGER | NULLABLE |
| **capital_words_title** | STRING  | REPEATED |
| **persons**           | STRING  | NULLABLE |
| **organizations**     | STRING  | NULLABLE |
| **locations**         | STRING  | NULLABLE |

1.3 A repository in Artifact Registry (`us-central1-docker.pkg.dev/code-challenge-autoscraping/code-challenge-source-repo`).

### 2. Building and Deploying the Image

2.1 Set up the following environment variables in `full_deploy.ps1`:

```ps1
$env:PROJECT_ID="code-challenge-autoscraping"
$env:REGION="us-central1"
$env:REPOSITORY="code-challenge-source-repo"
$env:IMAGE_NAME="code-challenge-image"
```

2.2 Run `./full_deploy.ps1` to build the Docker image (ensure the Docker daemon is running), then push it to the repository.

### Alternative Running Options

It is possible to run the Dockerized code locally.

#### Requirements

1. Set `local_run = True` in `env_manager.py`. This is mandatory to run the code successfully in a local environment.
2. Obtain a service account and store the plain `.json` file in `secrets/service_account_big_query`.
3. Build the Docker image locally and create a container. Then execute:

```sh
curl http://localhost:8080
```

## Feature 1: Named Entity Extraction

For this project, spaCy was chosen due to its speed, efficiency, and cost-effectiveness in extracting persons, organizations, and locations from news articles.

I'm using en_core_web_md because it balances size and performance, making it suitable for large-scale processing. However, for higher precision, en_core_web_trf (a transformer-based model) could be used, though it requires more computational resources.

While LLMs provide better contextual understanding, they are slower and more expensive, making spaCy the best choice for this project.