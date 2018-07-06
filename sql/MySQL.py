import pymysql

class DB():

    @staticmethod
    def run(query):

        db = pymysql.connect(host = '127.0.0.1',user = 'root',passwd='alumno',db='ramonnachon',charset = 'utf8',autocommit = True)
        cursor = db.cursor(pymysql.cursors.DictCursor)
        cursor.execute(query)
        db.close()
        return cursor