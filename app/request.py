from app import app
from .models import source
import urllib.request, json

Source = source.Source

#Getting api key
api_key = app.config['NEWS_API_KEY']

#Getting the base urls
source_base_url = app.config['NEWS_API_SOURCE_URL']
article_base_url = app.config['NEWS_API_ARTICLE_URL']

def get_sources(category):
    '''
    Function that get the sources data from the api
    '''

    get_sources_url = source_base_url.format(category, api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        sources_results = None

        if get_sources_response['sources']:
            get_sources_list = get_sources_response['sources']
            sources_results = process_results(get_sources_list)

    return sources_results

def process_results(source_list):
    '''
    Function that processes the sources data to transform them to a list of objects

    Args:
        source_list: list of dictionaries that hold news data
    Returns:
        source_results: A list of source object
    '''

    source_results = []

    for item in source_list:
        id = item.get('id')
        name = item.get('name')
        description = item.get('description')
        category = item.get('category')

        source_data = Source(id, name, description, category)
        source_results.append(source_data)

    return source_results


