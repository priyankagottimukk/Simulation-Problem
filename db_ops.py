import sqlite3

class sqlite_conn:
    def __init__(self):
        self.conn = sqlite3.connect("chats.db")

    def create_table(self,table_name, fields):
        exec_status = True
        try:
            cursor = self.conn.cursor()
            query = "CREATE TABLE %s (%s)" %(table_name, ",".join(fields))
            cursor.execute(query)
        except Exception as e:
            print(e)
            exec_status = False
        self.conn.commit()
        return exec_status

    def insert_row(self, table_name, values):
        exec_status = True
        try:
            cursor = self.conn.cursor()
            #This may be succeptible for SQL injection never do direct interpolation from strings unless they are pre formated
            query = "INSERT INTO %s VALUES (%s)" %(table_name, ",".join(values))
            cursor.execute(query)
        except Exception as e:
            print(e)
            exec_status = False
        self.conn.commit()
        return exec_status       
            
    def get_data(self, table_name, where_clause):
        try:
            cursor = self.conn.cursor()
            query = "SELECT * FROM %s where %s" %(table_name, where_clause)
            return [row for row in cursor.execute(query)]
        except Exception as e:
            raise e

    def close_conn(self):
        self.conn.close()
