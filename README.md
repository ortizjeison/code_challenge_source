## Compilation Instructions

### Before Starting
Ensure `local_run = False` in `env_manager.py`. This is mandatory to run the code successfully in Cloud Run.

### 1. Infrastructure Requirements

1.1 GCP account with a project (In this case ID=`code-challenge-autoscraping`)

1.2 BigQuery Dataset (in this case ID=`code-challenge-autoscraping.articles_data`), also a table with the following schema:

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

1.3 A Repository in Artifact Registry (In this case: `us-central1-docker.pkg.dev/code-challenge-autoscraping/code-challenge-source-repo`)

### 2. Building and Deploying Image

2.1 Run `./full_deploy.ps1` to build the docker (docker daemon must be running), then it pushes it to the repository.

### Alternative Running Options

In this case, it's possible to run the dockerized code locally.

#### Requirements

1. Set `local_run = True` in `env_manager.py`. This is mandatory to run the code successfully in a local repo.
2. Get a service account and store the plain `.json` file in `secrets/service_account_big_query`.
3. Build the docker locally and create a container. Then execute `curl http://localhost:8080`.



SELECT  * FROM `code-challenge-autoscraping.articles_data.parsed_articles` LIMIT 1000
DELETE FROM `code-challenge-autoscraping.articles_data.parsed_articles` WHERE TRUE;