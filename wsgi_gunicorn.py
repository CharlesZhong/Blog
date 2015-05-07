#!/usr/bin/env python
from werkzeug.contrib.fixers import ProxyFix
import os
from app import create_app

app = create_app(os.getenv('AFG_CONFIG') or 'default')
app.wsgi_app = ProxyFix(app.wsgi_app)

if __name__ == '__main__':
    app.run(host='localhost', port=8080)
