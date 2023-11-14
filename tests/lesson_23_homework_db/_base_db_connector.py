import psycopg2
from utilities.deco import singleton


@singleton
class BaseDbConnection:
    def __init__(self, db_params):
        self.conn = psycopg2.connect(**db_params)
        self.cursor = self.conn.cursor()
