from django.db import connection

def GetQuerySetFromDataBases(request):
    try:
        cursor = connection.cursor()
        result = cursor.execute(request)
        result = cursor.fetchall()
        connection.commit()
        print(result)
        connection.close()

    except:
        connection.rollback()
        print("Failed selecting in GetQuerySetFromDataBases")


    return result

