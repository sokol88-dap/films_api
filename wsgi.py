"""Main module for run server."""
from src import app

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
