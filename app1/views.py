from django.shortcuts import render
from app1.models import *
from django.http import HttpResponse
# Create your views here.
def usernameCheck(request):
    if request.method=='POST':
        v=request.POST['us']
        u=request.POST['ps']
        if v=='vamsi' and u=='poojitha':
            return HttpResponse(f'successfully created & username is {request.POST['us']}')
        else:
            return HttpResponse('not available')
    return render(request,'h1.html')

def addStudent(request):
    v=Department.objects.all() 
    d={'v':v}
    if request.method=='POST':
        w=request.POST['sub']
        q=request.POST['sname']
        r=request.POST['num']
        s=request.POST['paid']
        t=request.POST['username']
        u=request.POST['password']
        pp=Department.objects.filter(sub=w) #FILTER METHOD
        if pp:
            p=Department.objects.get(sub=w)#IF PP IS TRUE THEN ONLY I CAN CREATE p 
            b=Student.objects.get_or_create(sub=p,sname=q,num=r,paid=s,username=t,password=u)[0]
            b.save()
            return HttpResponse(f'successfully student is added {request.POST['sname']}')
        else:
            return HttpResponse(f'sorry baby this  subject [{request.POST['sub']}] is not available in our institute')
    return render(request,'h2.html',d)

def verification(request):
    v=Student.objects.all() 
    d={'v':v}
    if request.method=='POST':
        w=request.POST['sname']
        q=request.POST['code']
        r=request.POST['verify']
        pp=Student.objects.filter(sname=w) #FILTER METHOD
        if pp:
            p=Student.objects.get(sname=w)#IF PP IS TRUE THEN ONLY I CAN CREATE p 
            b=Declaration.objects.get_or_create(sname=p,code=q,verify=r)[0]
            b.save()
            return HttpResponse(f'successfully student is Verified  {request.POST['sname']}')
        else:
            return HttpResponse(f'sorry baby this  student [{request.POST['sname']}] is not verified')
    return render(request,'h3.html',d)