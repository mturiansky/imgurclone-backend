#!/usr/bin/env python

from setup import app
from routes import *

if __name__ == '__main__':
    app.run(debug=True, port=4999)
