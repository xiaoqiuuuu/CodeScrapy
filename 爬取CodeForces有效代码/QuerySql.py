import pymysql

class QuerySql:
    def __init__(self):
        self.conn = pymysql.connect(
            host="localhost",
            port=3306,
            user="root",
            password="Weiqt",
            database="cf_problems"
        )
        # 指定每页的行数和页数
        self.page_size = 10  # 每页行数
        self.page_number = 1  # 页数
        self.limit = 1500  # 最大查数量
        self.remote_id = "193%"

        self.sql = "select * from problems limit %s"
        self.cursor = self.conn.cursor()

    def query(self):
        self.cursor.execute(self.sql, (self.limit,))
        return self.cursor.fetchall()

    def close(self):
        self.cursor.close()
        self.conn.close()
