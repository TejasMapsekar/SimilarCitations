# Flask Application with Citation Similarity

This is a Flask application that processes responses and finds similar sources using a pre-trained sentence transformer model.

## Setup

1. Clone the repository:
```
   git clone https://github.com/yourusername/my_flask_app.git
   cd my_flask_app
```
2. Create a virtual environment and activate it: 
```
    python -m venv .venv
    source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
```
3. Install the dependencies:
```
   pip install -r requirements.txt
```
4. Start the Flask application:
```
   python app.py
```
5. Open your web browser and go to http://127.0.0.1:5000/ to view the application.

## Code Structure

1. app.py: Main Flask application file.
2. api.py: Fetches data from an external API.
3. llm.py: Contains utility functions for finding similar sources.
4. templates/: Contains HTML templates.
5. static/: Contains static files like CSS.
