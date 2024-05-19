"""
app.py: Main Flask application file
"""
from flask import Flask, request, render_template
from api import fetch_data
from llm import find_similar_sources

app = Flask(__name__,static_folder="static")

@app.route('/')
def index():
    """
    Index route to display the responses and their citations.
    Handles pagination to fetch data from the API.
    """
    page = request.args.get('page', 1, type=int)
    data = fetch_data(page)
    
    if data and 'data' in data:
        citations = find_similar_sources(data['data']['data'])
        pagination = {
            'current_page': data['data']['current_page'],
            'last_page': data['data']['last_page'],
            'next_page_url': data['data']['next_page_url'],
            'prev_page_url': data['data']['prev_page_url']
        }
        return render_template('index.html', citations=citations, pagination=pagination)
    return "No data available"

if __name__ == '__main__':
    app.run(debug=True)
