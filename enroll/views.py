from django.shortcuts import render
from .forms import StudentRegistration
from .models import user
from django.http import HttpResponseRedirect
# Create your views here.
def add_show(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = user(name=nm, email=em, password=pw)
            reg.save()
            fm = StudentRegistration()
    else:
        fm = StudentRegistration()
    stud = user.objects.all()

    return render(request, 'enroll/addandshow.html', {'form':fm, 'stu':stud})

#This fuction will delete data
def delete_data(request, id):
    if request.method == 'POST':
        pi = user.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
    
#This function will update data
def update_data(request, id):
    if request.method == 'POST':
        pi = user.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = user.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=pi)
    return render(request, 'enroll/updatestudent.html', {'form':fm})