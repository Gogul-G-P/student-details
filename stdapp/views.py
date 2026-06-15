from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm

def index(request):

    if request.method == 'POST':
        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/')
    
    form = StudentForm()

    data = Student.objects.all()

    return render(request, 'index.html', {
        'form': form,
        'data': data
    })

def delete_student(request, id):
    student = Student.objects.get(id=id)
    student.delete()

    return redirect('/')

def update_student(request,id):
    student = Student.object.get(id=id)

    if request.method == 'POST':
        form= StudentForm(request.POST,instance=student)

        if form.is_valid():
            form.save()
            return redirect('/')
        
    form = StudentForm(instance=student)

    return render(request, 'index.html', {
        'form': form
    })
