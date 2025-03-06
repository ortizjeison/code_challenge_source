from bs4 import BeautifulSoup
import traceback
import pandas as pd
import csv
from entity_recognition import extract_entities


def parse_news(html_content):

    soup = BeautifulSoup(html_content, 'html.parser')
    parsed_articles = []

    for article in soup.find_all('div', class_='contenedor_dato_modulo'):
        try:
            title = article.find('div', class_='volanta fuente_roboto_slab').get_text(strip=True)
            kicker_tag = article.find('h2', class_='titulo fuente_roboto_slab').find('a')
            kicker = kicker_tag.get_text(strip=True)
            link = kicker_tag['href']
            image_tag = article.find('div', class_='imagen').find('img')
            image_url = image_tag['src'] if image_tag else None
            
            parsed_articles.append({
                'title': title,
                'kicker': kicker,
                'link': link,
                'image': image_url
            })
        except:
            #In this case it's not a full article, so we can skip it
            pass

    return parsed_articles

def post_processing(parsed_articles: list):
    df = pd.DataFrame(parsed_articles)

    df['word_count_title'] = df['title'].apply(lambda x: len(x.split()))
    df['char_count_title'] = df['title'].apply(len)
    df['capital_words_title'] = df['title'].apply(lambda x: [word for word in x.split() if word.istitle()])
    
    entities = df['kicker'].apply(lambda x: extract_entities(x))
    
    df['persons'] = entities.apply(lambda x: ', '.join(list(set(x.get("PERSON", [])))))
    df['organizations'] = entities.apply(lambda x: ', '.join(list(set(x.get("ORG", [])))))
    df['locations'] = entities.apply(lambda x: ', '.join(list(set(x.get("GPE", [])))))
    
    df.to_csv('articles.csv', index=False)

    return df
