import os

from app import app


def runserver():
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, threaded=False, debug=False)


if __name__ == '__main__':
    runserver()
