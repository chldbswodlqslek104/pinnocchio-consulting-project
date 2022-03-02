from django.db import connection
import pandas as pd
import pymysql.cursors

def GetQuerySetFromDataBases(request):
    try:
        connection = pymysql.connect(host='localhost', port=3306, user='root',
                                     password='freefree104460!', db='project',
                                     charset='utf8',autocommit=True,
                                     cursorclass=pymysql.cursors.DictCursor)
        cursor = connection.cursor()
        cursor.execute(request)
        result = cursor.fetchall()
        connection.commit()
        print(result)
        connection.close()
        result = pd.DataFrame(result)
        print(result)

    except:
        connection.rollback()
        print("Failed selecting in GetQuerySetFromDataBases")


    return result

