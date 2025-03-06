from google.cloud import bigquery
from google.oauth2 import service_account

SERVICE_ACCOUNT_FILE = "code-challenge-autoscraping-c19da9772f16.json"
SCOPES = ["https://www.googleapis.com/auth/cloud-platform"]

credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
client = bigquery.Client(credentials=credentials)

def upload_dataframe_to_bigquery(dataframe):
    # set table id
    table_id = "code-challenge-autoscraping.articles_data.parsed_articles"

    #Create job to load dataframe to BigQuery
    job = client.load_table_from_dataframe(dataframe, table_id)
    job.result()