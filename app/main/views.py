from flask import render_template
from app import app
from .requests import get_newsSource
from .requests import get_newsArticles

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    # Getting popular news
    popular_newsSource = get_newsSource('popular')
    print(popular_newsSource)
    
    popular_newsArticles = get_newsArticles('popular')
    print(popular_newsArticles)
    
    title = 'Home - Welcome to The best News Review Website Online'
    return render_template('index.html', title = title, popular = popular_newsSource, popular = popular_newsArticles)




@app.route('/news/<int:news_id>')
def news(news_id):

    '''
    View news page function that returns the news details page and its data
    '''
    return render_template('news.html',id = news_id)
