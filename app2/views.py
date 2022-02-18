from django.shortcuts import render

# Create your views here.
def result(request):
	a=request.GET["department"]
	b=request.GET["major"]
	c=request.GET["track"]
	d=request.GET["entry_year"]
	datas=CreaditRequirements.objects.filter(
	case_contains= 'a' & 'b' & 'c',
	start='d')
	return render(request,"list.html",{"sangpums":datas})