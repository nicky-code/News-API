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
    # Getting popular news_source 
    popular_newsSource = get_newsSource('popular')
    upcoming_newsSource = get_newsSource('upcoming')
    now_showing_newsSource = get_newsSource('now_reading')
    
    title = 'Home - Welcome to The best News_Source Review Website Online'
    
    return render_template('index.html', title = title, popular = popular_newsSource, upcoming = upcoming_newsSource, now_showing = now_showing_newsSource)

    # Getting popular news_articles
    popular_newsArticles = get_newsArticles('popular')
    upcoming_newsArticles = get_newsArticles('upcoming')
    now_showing_newsArticles = get_newsArticles('now_reading')
    
    title = 'Home - Welcome to The best News_Articles Review Website Online'
    return render_template('index.html', title = title, popular = popular_newsArticles, upcoming = upcoming_newsArticles, now_showing = now_showing_newsArticles)
    
@app.route('/news/<int:news_id>')
def news(news_id):

    '''
    View news page function that returns the news details page and its data
    '''
    return render_template('news.html',id = news_id)
