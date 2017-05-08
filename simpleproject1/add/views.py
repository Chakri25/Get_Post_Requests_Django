from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from add.models import toDoList
from add.forms import toDoListForm

# Create your views here.
def add(request):
	x = toDoList.objects.all()
	if request.method == 'POST':
		form = toDoListForm(request.POST)
		if form.is_valid():
			d = form.cleaned_data
			v = d['data']
			ob = toDoList(data= v)
			ob.save()
			print(request.path == '/new')
			return(HttpResponseRedirect('/new'))
	else:
		form = toDoListForm()
		
	return(render(request, "add/display.html",{'x':x,'form': form}))

def delete(request):
	x = toDoList.objects.all()
	if request.method == 'POST':
		form = toDoListForm(request.POST)
		if form.is_valid():
			ob = toDoList.objects.get(id=x[0].id).delete()
			return(HttpResponseRedirect('/delete'))
	else:
		form = toDoListForm()
		
	return(render(request, "add/display.html",{'x':x,'form': form}))

"""
def delete(request):
	x = toDoList.objects.all()
	if request.method == 'POST':
		form = toDoListForm(request.POST)
		if form.is_valid():
			b = toDoList.objects.get(id=1).delete()
			b.save()
			return(HttpResponse("Done"))
	return(render(request, "add/display.html",{'x':x,'form': form}))"""

def test(request, id):
	return(HttpResponse("<h1>This is "+id+"</h1>"))
