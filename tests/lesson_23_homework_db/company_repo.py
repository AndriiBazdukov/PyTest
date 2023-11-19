from tests.lesson_23_homework_db._base_db_connector import BaseDbConnection


class CompanyRepo:
    def __init__(self, db_params):
        self._db = BaseDbConnection(db_params)
        self._table_name = 'STORE'

    def create_table(self, name=None):
        if name is None:
            name = self._table_name
        query_create = f'''
        CREATE TABLE {name}
        (ID INTEGER PRIMARY KEY    AUTOINCREMENT,
        NAME           TEXT    NOT NULL,
        QUANTITY            INT     NOT NULL,
        DESCRIPTION        CHAR(50),
        PRICE         REAL);
        '''
        self._db.cursor.execute(query_create)
        self._db.conn.commit()

    def update_record_by_id(self, name: str, quantity: int, description: str, price: float, record_id: int):
        query_update = f'''
                    UPDATE {self._table_name}
                    SET NAME=?, QUANTITY=?, DESCRIPTION=?, PRICE=?
                    WHERE ID=?;
                    '''
        self._db.cursor.execute(query_update, (name, quantity, description, price, record_id))
        self._db.conn.commit()

    def table_exists(self):
        result = self._db.cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{self._table_name}';")
        return result.fetchone() is not None

    def get_all(self):
        res = self._db.cursor.execute(f"SELECT * FROM {self._table_name}")
        return res.fetchall()

    def get_one_by_id(self, user_id: int):
        res = self._db.cursor.execute(f"SELECT * FROM {self._table_name} WHERE id={user_id}")
        emp = res.fetchone()
        return emp

    def delete_record_by_id(self, user_id: int):
        self._db.cursor.execute(f"DELETE FROM {self._table_name} WHERE id = {user_id}")
        self._db.conn.commit()

    def insert_one(self, name: str, quantity: int, description: str, price: float):
        query_insert = f'''
                INSERT INTO {self._table_name} (NAME,QUANTITY,DESCRIPTION,PRICE)
                VALUES ('{name}', {quantity}, '{description}', {price});
                '''
        self._db.cursor.execute(query_insert)
        self._db.conn.commit()

    def delete_table(self, name=None):
        if name is None:
            name = self._table_name
        query_drop_table = f'''
        DROP TABLE {name};
        '''
        self._db.cursor.execute(query_drop_table)
        self._db.conn.commit()

    def drop_all_tables(self):
        tables = self._db.cursor.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()

        for table in tables:
            table_name = table[0]
            if table_name != "sqlite_sequence":
                self._db.cursor.execute(f"DROP TABLE {table_name};")

        self._db.conn.commit()

    def __del__(self):
        self._db.cursor.close()
        self._db.conn.close()
