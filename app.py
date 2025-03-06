from flask import Flask
from main import run_web_scraping

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    """
    Endpoint to trigger the preprocessing of data.
    """
    print('Started process')
    try:
        run_web_scraping()
        
    except Exception as e:
        print(f'Error during processing: {e}')
    return "Process completed", 200

def start_app():
    """
    Start the Flask application.
    """
    #app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
    app.run(debug=True, host="0.0.0.0", port=8080)

if __name__ == "__main__":
    start_app()