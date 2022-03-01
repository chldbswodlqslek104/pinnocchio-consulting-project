from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.db import connection
from .database import GetQuerySetFromDataBases
# Create your views here.

def index(request):
    return render(request, 'html/first-screen.html')

#HttpResponse("Hello, world. You're at the polls index.")

#render(request, 'C:/last/hosting/src/html/first-screen.html')


def DBListView(request):
    try: 
        strSql = "SELECT special_option_idx, hased_options from micro_cases;"
        datas = GetQuerySetFromDataBases(strSql)
        data = [
            {'special_option_idx': data[0],'hased_options': data[1],}
            for data in datas]

    except:
        connection.rollback()
        print("Failed selecting in DBListView")

    return datas

#print(DBListView(1))
