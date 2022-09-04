import feedparser
import time
from datetime import datetime, timezone, timedelta
import json
import requests
import re


NOTION_DATABASE_ID = 'YOUR_NOTION_DATABASE_ID'
NOTION_TOKEN = 'YOUR_NOTION_SECRET_TOKEN'

urls = [
    # feeds
]

JST = timezone(timedelta(hours=+9), 'JST')


def add_content():
    headers = {
        "Authorization": "Bearer " + NOTION_TOKEN,
        "Content-Type": "application/json",
        "Notion-Version": "2022-06-28"
    }
    notion_url = 'https://api.notion.com/v1/pages'
    data = {
        "parent": { "database_id": NOTION_DATABASE_ID },
        "properties": {
            # some properties
        },
        # if you use cover, set this property
        # "cover": {}
    }
    data = json.dumps(data)
    response = requests.request("POST", notion_url, headers=headers, data=data)
    if not response.ok:
        print(json.dumps(response.json()))


# In Google Cloud Function, triggered this function
def main(event, context):
    for url in urls:
        elements = feedparser.parse(url)
        yesterday = datetime.now(JST) - timedelta(hours=24)
        pat = re.compile(r'hoge')
        for entry in elements.entries:
            title = entry.title
            date = datetime.fromisoformat(entry.published)
            date = date.astimezone(JST)
            url = entry.link
            author = entry.author
            if yesterday <= date:
                add_content(title, str(date), url, author)
                time.sleep(0.1)
