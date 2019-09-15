from app import app
import urllib.requests,json
from .models import news 

Source = news.Source
Articles = news.Articles

# Getting api key
api_key = app.config['News_API_KEY']


# Getting the news base url
source_base_url = app.config["SOURCE_API_BASE_URL"]
articles_base_url = app.config["ARTICLES_API_BASE_URL"]

def get_newsSource(category):
    '''
    Function that gets the json response to our url request
    '''
    get_newsSource_url = source_base_url.format(category,api_key)

    with urllib.requests.urlopen(get_newsSource_url) as url:
        get_newsSource_data = url.read()
        get_newsSource_response = json.loads(get_newsSource_data)

        news_results = None

        if get_newsSource_response['results']:
            news_results_list = get_newsSource_response['results']
            news_results = process_results(news_results_list)
            
    return news_results


def get_newsArticles(category):
    '''
    Function that gets the json response to our url request
    '''
    get_newsArticles_url = articles_base_url.format(category,api_key)

    with urllib.requests.urlopen(get_newsArticles_url) as url:
        get_newsArticles_data = url.read()
        get_newsArticles_response = json.loads(get_newsArticles_data)

        news_results = None

        if get_newsArticles_response['results']:
            news_results_list = get_newsArticles_response['results']
            news_results = process_results(news_results_list)
            
    return news_results


def process_results(newsSources_list)
     '''
    Function  that processes the news result and transform them to a list of Objects

    Args:
        newsSources_list: A list of dictionaries that contain source details

    Returns :
        newsS_results: A list of source objects
    '''
    newsS_results = []
    for news_item in newsSources_list:
        id = news_item.get('id')
        name = news_item.get('original_name')
        description = news_item.get('description')
        url = news_item.get('url')
        
        if url:
            newsSour_object = News(id,name,description,url)
            newsS_results.append(newsSour_object)

    return newsS_results


def process_results(newsAricle_list)
     '''
    Function  that processes the news result and transform them to a list of Objects

    Args:
        newsArticle_list: A list of dictionaries that contain articles details

    Returns :
        newsArticles_results: A list of articles objects
    '''
    newsA_results = []
    for news_item in newsArticle_list:
        author = news_item.get('author')
        title = news_item.get('original_title')
        description = news_item.get('description')
        url = news_item.get('url')
        publishedAt = news_item.get('publishedAt')
        
        if url:
            newsArt_object = News(author,title,description,url,publishedAt)
            newsA_results.append(newsArt_object)

    return newsA_results

