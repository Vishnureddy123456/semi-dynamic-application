from django.shortcuts import render

# Create your views here.
def wish(request):
    d={'name':'kusimma','age':7}
    return render(request,'wish.html',context=d)