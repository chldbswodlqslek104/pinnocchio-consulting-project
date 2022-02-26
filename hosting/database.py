from django.db import connection

def GetQuerySetFromDataBases(request):
    try:
        cursor = connection.cursor()
        result = cursor.execute(request)
        connection.commit()
        connection.close()

    except:
        connection.rollback()
        print("Failed selecting in GetQuerySetFromDataBases")


    return result

