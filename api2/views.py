from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Subjects
from .serializers import SubjectsSerializer
from hosting.database import GetQuerySetFromDataBases

@csrf_exempt
def Api2_list(request):
    if request.method == 'GET':
        query_set = Subjects.objects.all()
        serializer = SubjectsSerializer(query_set, many=True)
        # strSql = "SELECT * FROM subjects"
        # datas = GetQuerySetFromDataBases(strSql)
        # print(datas)
        return JsonResponse(serializer.data, safe=False)
        