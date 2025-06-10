# https://www.zotero.org/support/dev/web_api/v3/basics

import requests
import re
import html

# Obtem todos os itens de uma coleção do Zotero
def get_items(collection_key, user_id, api_key):

    base = f"https://api.zotero.org/users/{user_id}/collections/{collection_key}/items/top?format=json&key={api_key}"

    response = requests.get(base, timeout=15)
    items = response.json()
    response_obj = []
    for item in items:
        response_obj.append({
            "key": item['key'],
            "version": item['version'],
            "title": item['data']['title'],
            "url": item['data'].get('url', ''),
            "abstract": item['data'].get('abstractNote', ''),
        })

    return response_obj    


# Obter um único item do Zotero pelo seu key
def get_item(item_key, user_id, api_key):

    params = {
        "format": "json",
        "include": "data,bib",
        "style": "associacao-brasileira-de-normas-tecnicas",
        "locale": "pt-BR",
    }

    base = f"https://api.zotero.org/users/{user_id}/items/{item_key}"
    headers = {"Zotero-API-Version": "3"}
    headers["Zotero-API-Key"] = api_key
    response = requests.get(base, headers=headers, params=params, timeout=15)
    response_json = response.json()

    reference_json = response_json.get("bib", "")
    TAG_RE = re.compile(r"<[^>]+>")
    reference_text = TAG_RE.sub(" ", reference_json)
    reference_text = html.unescape(reference_text) 
    reference_plain = " ".join(reference_text.split())

    url = response_json["data"]["url"]

    date = response_json["data"]["dateAdded"]
    date = date.split("T")[0]
    date = date.split("-")
    date = f"{date[2]}/{date[1]}/{date[0]}"

    response_obj = {
        "text": response_json["data"].get("abstractNote", ""),
        "reference": f"{reference_plain} Disponível em <{url} >. Acesso em {date}.",
    }
    
    return response_obj

# Excluir um item do Zotero
def delete_item(item_key, version, user_id, api_key):
    base = f"https://api.zotero.org/users/{user_id}/items/{item_key}"
    headers = {"Zotero-API-Version": "3"}
    headers["Zotero-API-Key"] = api_key
    headers["If-Unmodified-Since-Version"] = str(version)
    response = requests.delete(base, headers=headers, timeout=15)
    return response
    
    