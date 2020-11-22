class Config:
    '''
    General configuration parent class
    '''

    NEWS_API_SOURCE_URL = 'https://newsapi.org/v2/sources?category={}&apiKey={}'
    NEWS_API_ARTICLE_URL = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'

class DevConfig(Config):
    '''
    Development configuration child class

    Args:
        Config: The parent configuration class with General configuration setting
    '''

    DEBUG = True

class ProdConfig(Config):
    '''
    Production configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''


