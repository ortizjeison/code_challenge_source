#%%
from fetch_html import fetch_html
from news_parser import parse_news, post_processing
import os
from gcp_utils import upload_dataframe_to_bigquery
from env_manager import local

def run_web_scraping():

    if local():
        with open('tmp/website.html', 'r') as file:
            html_content = file.read()
    else:
        #Fetch html content with selenium
        html_content = fetch_html()

    articles = parse_news(html_content)

    processed_articles = post_processing(articles)
    upload_dataframe_to_bigquery(processed_articles)



if __name__ == "__main__":
    run_web_scraping()