from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
    print("test")
    template = loader.get_template('video/index.html')
    context = {}
    return HttpResponse(template.render(context, request)) 

@csrf_exempt
def saveVideoData(request):
    print("saveVideoData")
    d = request.POST
    print(d)
    print(d.keys())
    
    return HttpResponse("Added")



    