from flask import render_template
from . import main
from ..requests import get_newsSource,get_newsArticles




# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    # Getting popular news_source 
    business_newsSource = get_newsSource('business')
    entertainment_newsSource = get_newsSource('entertainment')
    general_newsSource = get_newsSource('general')
    title = 'Home - Welcome to The best News_Source Review Website Online'
    
    return render_template('index.html', title = title, business = business_newsSource, entertainment  = entertainment_newsSource, general = general_newsSource)

    
    
@main.route('/news/<int:news_id>')
def news(news_id):

    '''
    View news page function that returns the news details page and its data
    '''
    return render_template('index.html',id = news_id)


@main.route('/newsSources/<id>')
def newsSources(id):


    '''
    View newsSources page function that returns the newsSources details page and its data
    '''
    newsSources = get_newsArticles(id)
    # title = f'{newsSources.title}'

    return render_template('news.html', newsSources = newsSources)

