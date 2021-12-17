from django.http import HttpResponse
from django.shortcuts import render, redirect
from . models import Task
from . forms import Todoforms
from django. views.generic import ListView
from django. views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView
from django.urls import reverse_lazy

# Create your views here.

class TaskListview(ListView):
    model = Task
    template_name = 'product_view.html'
    context_object_name = 'obj1'

class TaskDetailView(DetailView):
    model = Task
    template_name = 'detail.html'
    context_object_name = 'i'

class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'updates.html'
    context_object_name = 'task'
    fields = ('name','rate')
    def get_success_url(self):
        return reverse_lazy('cbvdetail',kwargs={'pk':self.object.id})




def product_view(request):
    obj1=Task.objects.all()
    if request.method=='POST':
        name=request.POST.get('name')
        rate=request.POST.get('rate')
        datetime=request.POST.get('datetime')
        obj=Task(name=name,rate=rate,datetime=datetime)
        obj.save()
    return render(request,'product_view.html',{'obj1':obj1})

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvtask')

def delete(request,taskid):
    task=Task.objects.get(id=taskid)
    if request.method=="POST":
        task.delete()
        return  redirect('/')
    return render(request,'delete.html',{'task':task})

def update(request,id):
    task=Task.objects.get(id=id)
    form=Todoforms(request.POST or None,instance=task)
    if form.is_valid():
        form.save()
        return  redirect('/')
    return render(request,'update.html',{'task':task,'form':form})

