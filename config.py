import os

class Config:
    
    SOURCE_API_BASE_URL ='https://newsapi.org/v2/sources?apiKey=4e8b4663595f427a81d5dae7bbd2dc39/{}?api_key={}'
    ARTICLES_API_BASE_URL ='https://newsapi.org/v2/everything?q=bitcoin&apiKey=4e8b4663595f427a81d5dae7bbd2dc39/{}?api_key={}'
    NEWS_API_KEY = os.environ.get('4e8b4663595f427a81d5dae7bbd2dc39')
    SECRET_KEY = os.environ.get('santa7')


class ProdConfig(Config):
    pass


class DevConfig(Config):
    
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}
