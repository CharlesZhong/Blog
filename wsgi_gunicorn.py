#!/usr/bin/env python
from werkzeug.contrib.fixers import ProxyFix
import os
from app import create_app

app = create_app("default")
app.wsgi_app = ProxyFix(app.wsgi_app)

if __name__ == '__main__':
    app.run()
