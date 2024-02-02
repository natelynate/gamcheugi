# DB Operation functions

import pymysql
from settings.config import *   
from flask import current_app, g

def get_db_conn():
    """Returns new/existing DB connection object for a request"""
    if 'db' not in g:
        g.db = pymysql.connect(
            host=current_app.config['DB_HOST'],
            user=current_app.config['DB_USER'],
            password=current_app.config['DB_PASSWORD'],
            database=current_app.config['DB_NAME'],
            cursorclass=pymysql.cursors.DictCursor
        )
    return g.db