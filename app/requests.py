import urllib.request,json
from .models import Source, Articles



# Getting api key
api_key = None

articles_base_url = None
# Getting the news base url
base_url = None
source_base_url = None
def configure_request(app):
    global api_key,base_url,source_base_url, articles_base_url
    api_key = app.config['NEWS_API_KEY']
    print(api_key)
    source_base_url = app.config['SOURCE_API_BASE_URL']
    articles_base_url = app.config['ARTICLES_API_BASE_URL']

def get_newsSource(category):
    '''
    Function that gets the json response to our url request
    '''
    get_newsSource_url = source_base_url.format(category,api_key)
    

    with urllib.request.urlopen(get_newsSource_url) as url:
        get_newsSource_data = url.read()
        get_newsSource_response = json.loads(get_newsSource_data)

        newsS_results = None

        if get_newsSource_response['sources']:
            news_results_list = get_newsSource_response['sources']
            newsS_results = process_results(news_results_list)
            
    return newsS_results

def process_results(newsSources_list):
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
        name = news_item.get('name')
        description = news_item.get('description')
        url = news_item.get('url')

        if url:
            newsSour_object = Source(id,name,description,url)
            newsS_results.append(newsSour_object)

    return newsS_results
    
def get_newsArticles(category):
    '''
    Function that gets the json response to our url request
    '''
    get_newsArticles_url = articles_base_url.format(category,api_key)
    print(get_newsArticles_url)
    with urllib.request.urlopen(get_newsArticles_url) as url:
        get_newsArticles_data = url.read()
        get_newsArticles_response = json.loads(get_newsArticles_data)

        news_results = None

        if get_newsArticles_response['articles']:
            news_results_list = get_newsArticles_response['articles']
            news_results = process_resultss(news_results_list)
            
    return news_results
    # pass





def process_resultss(newsArticle_list):
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
        title = news_item.get('title')
        description = news_item.get('description')
        url = news_item.get('url')
        urlToImage = news_item.get('urlToImage')
        publishedAt = news_item.get('publishedAt')
        
        if url:
            newsArt_object = Articles(author,title,description,url,urlToImage,publishedAt)
            newsA_results.append(newsArt_object)

    return newsA_results
    


# def get_newsSources(id):
#     get_newsSources_details_url = source_base_url.format(id,api_key)

#     with urllib.requests.urlopen(get_newsSources_details_url) as url:
#         newsSources_details_data = url.read()
#         newsSources_details_response = json.loads(newsSources_details_data)

#         newsSour_object = None
#         if newsSources_details_response:
#             id = newsSources_details_response.get('id')
#             name = newsSources_details_response.get('original_name')
#             description = newsSources_details_response.get('description')
#             url = newsSources_details_response.get('url')
#             newsSour_object = News(id,name,description,url)

#     return newsSour_object


# def get_newsArticle(id):
#     get_newsArticle_details_url = articles_base_url.format(id,api_key)

#     with urllib.requests.urlopen(get_newsArticle_details_url) as url:
#         newsArticle_details_data = url.read()
#         newsArticle_details_response = json.loads(newsArticle_details_data)

#         newsArt_object = None
#         if newsArticle_details_response:
#             author = newsArticle_details_response.get('author')
#             title = newsArticle_details_response.get('original_title')
#             description = newsArticle_details_response.get('description')
#             url = newsArticle_details_response.get('url')
#             urlToImage = newsArticle_details_response.get('urlToImage')
#             publishedAt = newsArticle_details_response.get('publishedAt')
#             newsArt_object = News(author,title,description,url,urlToImage,publishedAt)

#     return newsArt_object
