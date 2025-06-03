from wikidata.client import Client
import requests
import time
import random
import csv
from tqdm import tqdm
from datasets import load_dataset

client = Client()
dataset = load_dataset('sapienzanlp/nlp2025_hw1_cultural_dataset')

def extract_entity_id(url):
    return url.split('/')[-1]

def get_wikipedia_text(title, lang="en"):
    time.sleep(random.uniform(0.5, 1.5))  # rate limiting
    api_url = f"https://{lang}.wikipedia.org/w/api.php"
    headers = {
        "User-Agent": "MNLP_UNI_PROJECT/1.0 (olmoceriotti@gmail.com)"
    }
    params = {
        "action": "query",
        "prop": "extracts",
        "explaintext": True,
        #"exintro": True,
        "titles": title,
        "format": "json",
        "redirects": 1
    }

    res = requests.get(api_url, headers=headers, params=params).json()
    page = next(iter(res["query"]["pages"].values()))
    return page.get("extract", "")[:1000] 

output_file = "wikipedia_texts_test.csv"

with open(output_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=["id", "english_text", "other_language_text"])
    writer.writeheader()

    for example in tqdm(dataset['train']):
        entity_url = example['item']
        entity_id = extract_entity_id(entity_url)
        try:
            entity = client.get(entity_id, load=True)
        except Exception as e:
            print(f"Error fetching entity {entity_id}: {e}")
            continue

        sitelinks = entity.data.get("sitelinks", {})
        enwiki = sitelinks.get("enwiki")
        if not enwiki:
            continue

        title = enwiki["title"]
        english_text = get_wikipedia_text(title, lang='en')

        other_language_text = ""

        try:
            country_claim = entity['P495']
            if country_claim:
                country_entity = country_claim[0].value
                language_claim = country_entity['P37']
                if language_claim:
                    lang_code = language_claim[0].value.id.lower()
                    other_language_text = get_wikipedia_text(title, lang=lang_code)
        except Exception as e:
            print(f"Error getting other-language text for {entity_id}: {e}")

        writer.writerow({
            "id": entity_id,
            "english_text": english_text,
            "other_language_text": other_language_text
        })
