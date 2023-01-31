from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')
def add(request):
    num1 = int(request.GET["num1"])
    num2 = int(request.GET["num2"])
    res1 = num1+num2
    res2 = num1-num2
    res3 = num1*num2
    res4 = num1/num2
    return render(request,'result.html', {"result1": res1, "result2": res2, "result3": res3, "result4": res4})
