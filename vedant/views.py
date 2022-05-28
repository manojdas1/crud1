from django.shortcuts import render,HttpResponseRedirect
from .forms import StudentRegistration
from .models import Student

# Create your views here.
def add_show(request):
    if request.method == 'POST':
        stud = Student.objects.all()
        fm=StudentRegistration(request.POST)
        if fm.is_valid():
            name = fm.cleaned_data['name']
            email = fm.cleaned_data['email']
            password = fm.cleaned_data['password']
            address = fm.cleaned_data['address']
            reg = Student(name=name, email=email, password=password, address=address)
            reg.save()
            fm = StudentRegistration()
    else:
        fm=StudentRegistration()
        stud = Student.objects.all()

    return render(request, 'vedant/addandshow.html',{'form':fm, 'st':stud})

#delete
def delete_data(request, id):
    if request.method == 'POST':
        pi = Student.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')

#edit
def edit_data(request, id):
    if request.method == 'POST':
        pi = Student.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = Student.objects.get(pk=id)
        fm = StudentRegistration(instance=pi)
    return render(request, 'vedant/update.html', {'form': fm,})