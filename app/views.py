from django.core import paginator
from django.shortcuts import render, redirect
from django.http import HttpResponse
from app.forms import CarroForm
from app.models import Carro
from django.core.paginator import PageNotAnInteger, Paginator

# Create your views here.
def home(request):
	#return HttpResponse('<h1>Hello world!</h1>')
	data = {}
	#data['carro'] = 'Fiat Uno'
	#data['carros'] = Carro.objects.all()

	search = request.GET.get('search')

	if (search):
		all = Carro.objects.filter(modelo__icontains = search)
	else:
		all = Carro.objects.all()

	paginator = Paginator(all, 6)
	page = request.GET.get('page')
	data['carros'] = paginator.get_page(page)	
	data['total_pages'] = range(1, data['carros'].paginator.num_pages+1)
	data['search'] = search

	return render(request, 'index.html', data)

def form(request):
	data = {}

	data['form'] = CarroForm()

	return render(request, 'form.html', data)

def create(request):

	form = CarroForm(request.POST or None)

	if form.is_valid():
		form.save()
		return redirect('home')

def view(request, pk):
	data = {}
	data['carro'] = Carro.objects.get(pk=pk)
	return render(request, 'view.html', data)

def edit(request, pk):
	data = {}
	data['carro'] = Carro.objects.get(pk=pk)
	data['form'] = CarroForm(instance=data['carro'])
	return render(request, 'form.html', data)

def update(request, pk):
	data = {}
	data['carro'] = Carro.objects.get(pk=pk)
	form = CarroForm(request.POST or None, instance=data['carro'])
	if form.is_valid():
		form.save()
		return redirect('home')

def delete(request, pk):
	carro = Carro.objects.get(pk=pk)
	carro.delete()
	return redirect('home')