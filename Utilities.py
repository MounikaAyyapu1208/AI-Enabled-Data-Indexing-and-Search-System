
# Utilities.py
from flask import Flask, request, render_template_string
import requests
import json

app = Flask(__name__)

# HTML template with proper handling for responses and errors
HTML_TEMPLATE = '''
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document Search and Analysis</title>
    <style>
        body, html {
            height: 100%;
            margin: 0;
            font-family: Arial, sans-serif;
            background-color: #fafafa;
            color: #333;
        }
        .container {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100%;
        }
        .form {
            margin: 30px;
            padding: 20px;
            width: 90%;
            max-width: 600px;
            background-color: #fff;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }
        input[type="text"], input[type="submit"] {
            width: 100%;
            padding: 10px;
            margin: 8px 0;
            border: 1px solid #ccc;
            border-radius: 4px;
            box-sizing: border-box;
        }
        input[type="submit"] {
            background-color: #4CAF50;
            color: white;
            cursor: pointer;
        }
        input[type="submit"]:hover {
            background-color: #45a049;
        }
        .results {
            width: 90%;
            max-width: 600px;
            margin-top: 20px;
            background-color: #fff;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 2px 6px rgba(0,0,0,0.1);
        }
        .results section {
            margin-top: 10px;
            padding: 8px;
            border-bottom: 1px solid #eee;
        }
        .results section:last-child {
            border-bottom: none;
        }
        .error {
            color: red;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="form">
            <h1>Document Search and Analysis</h1>
            <form method="post">
                <input type="text" id="query" name="query" placeholder="Enter your query...">
                <input type="submit" value="Search">
            </form>
        </div>
        {% if response_content %}
            <div class="results">
                {% if response_content.get('error') %}
                    <section class="error">{{ response_content['error'] }}</section>
                {% else %}
                    <section>
                        <strong>Corrected Query:</strong> {{ response_content.get('corrected_query', '') }}
                    </section>
                    <section>
                        <strong>Distances:</strong> {{ response_content.get('distances', [])|tojson }}
                    </section>
                    <section>
                        <strong>Expanded Query:</strong> {{ response_content.get('expanded_query', '') }}
                    </section>
                    <section>
                        <strong>Indices:</strong> {{ response_content.get('indices', [])|tojson }}
                    </section>
                {% endif %}
            </div>
        {% endif %}
    </div>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def home():
    response_content = {}
    if request.method == 'POST':
        query = request.form.get('query', '')
        if query:
            response_content = send_request(query)
    return render_template_string(HTML_TEMPLATE, response_content=response_content)

def send_request(query):
    url = 'http://127.0.0.1:5000/query'
    json_data = {'query': query, 'top_k': 5}
    try:
        response = requests.post(url, json=json_data)
        response.raise_for_status()  # Check for HTTP errors
        return response.json()  # Attempt to parse JSON
    except requests.exceptions.HTTPError as err:
        return {'error': f'HTTP error: {err}'}
    except requests.exceptions.RequestException as err:
        return {'error': f'Request error: {err}'}
    except json.JSONDecodeError:
        return {'error': 'Invalid JSON received'}
    except Exception as err:
        return {'error': f'An unexpected error occurred: {err}'}

if __name__ == '__main__':
    app.run(debug=True, port=5001)
