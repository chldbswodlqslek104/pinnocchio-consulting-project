from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Requirements
from .serializers import RequirementsSerializer
from rest_framework.parsers import JSONParser
# Create your views here.

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
