# Flask Application with Citation Similarity

This is a Flask application that processes responses and finds similar sources using a pre-trained sentence transformer model.

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/my_flask_app.git
   cd my_flask_app
```
2. Create a virtual environment and activate it: 
```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
    ```
3. Install the dependencies:
```bash
   pip install -r requirements.txt
   ```
4. Start the Flask application:
```bash
   python app.py
```
5. Open your web browser and go to http://127.0.0.1:5000/ to view the application.

##Code Structure
app.py: Main Flask application file.
api.py: Fetches data from an external API.
llm.py: Contains utility functions for finding similar sources.
templates/: Contains HTML templates.
static/: Contains static files like CSS.
