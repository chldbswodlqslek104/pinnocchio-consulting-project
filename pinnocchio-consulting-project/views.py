
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Subjects
from .serializers import SubjectsSerializer
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

print(DBListView(1))

@csrf_exempt
def Api2_list(request):
    if request.method == 'GET':
        # query_set = Subjects.objects.all()
        # serializer = SubjectsSerializer(query_set, many=True)
        # strSql = "SELECT * from subjects;"
        # datas = GetQuerySetFromDataBases(strSql)
        test = [
            { 
        "subject_idx": 1,
		"subject_name": "1",
		"grade": 1,
		"subject_mode": "1",
		"subject_code": "1",
		"instructor": "1",
		"credits": 1,
		"tags": "1",
		"mon": "1",
		"tue": "1",
		"wed": "1",
		"thu": "1",
		"fri": "1",
		"sat": "1",
		"sun": "1",
		"x_grade": 1,
		"o_grade": 1,
		"x_department": 1,
		"o_department": 1,
		"subject_type_1_idx": 1,
		"subject_type_1_name": "1",
		"subject_type_2_idx": 1,
		"subject_type_2_name": "1",
		"subject_type_3_idx": 1,
		"subject_type_3_name": "1",
		"department_idx": 1,
		"department_name": "1"
        }
        for data in range(20)
        ]
        serializer = SubjectsSerializer(test, many=True)
        return JsonResponse(serializer.data, safe=False)

    
@csrf_exempt
def Requirement(request):
    if request.method == 'GET':
        #TODO
        #해당 request에 대한 query를 DB에 요청하여 추출
        dummyDict = {
            "special_option_idx" : 10, #해당 테이블 상 각  레코드의 고유 식별자
            "hashed_options" : "SW_AI_AI_NEW", #(학과+전공+트랙+입과경로)로 얻은 해시값
            "entry_year" : 2022,
            "basic_major_subject" : 30,
            "necess_major_subject" : 30,
            "total_major_subject" : 30,
            "common_GE_subject" : 30,
            "core_GE_subject" : 12,
            "total_subjects" : 132
        }

        #Return Dummy Json
        return JsonResponse(dummyDict)