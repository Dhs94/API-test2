import pymysql.cursors
import json


class OperateMysql:
    def __init__(self):
        self.conn = pymysql.connect(
            host="127.0.0.1",
            port=83306,
            user="root",
            passwd="",
            db="wdms_db",
            charset="utf8",
            # 输出字典
            cursorclass=pymysql.cursors.DictCursor
        )
        self.cur = self.conn.cursor()

    def search_one(self, sql):
        self.cur.execute(sql)
        result = self.cur.fetchone()
        result = json.dumps(result)
        return result

    def search_all(self, sql):
        self.cur.execute(sql)
        result = self.cur.fetchall()
        # result = json.dumps(result)
        return result

    def insert(self, sql):
        try:
            self.cur.execute(sql)
            self.conn.commit()
            print('success')
        except:
            self.conn.rollback()
            print('fail')

if __name__ == '__main__':
    op_sql = OperateMysql()
    sql1 = """INSERT INTO company(companyid,companyname)
           VALUES('4','KAY')"""
    sql2 = """SELECT * FROM company"""
    r = op_sql.search_all(sql2)
    print(r)
    print(type(r))

