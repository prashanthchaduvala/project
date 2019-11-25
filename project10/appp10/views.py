from django.shortcuts import render


def showdata(request):
    return render(request,"main.html")
def mainshow(request):
    username=request.POST.get("t1")
    paas=request.POST.get("t2")
   # d1=makedict(name=username,pass=paas)
    return render(request,"welcome.html")
#def makedict(** kwargs):
 #   return kwargs
