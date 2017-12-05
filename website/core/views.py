from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html',{})

def sobre_nos(request):
	return render(request,"sobre-nos.html",{})

def equipe(request):
	return render(request,'equipe.html',{})

def especialidades(request):
	return render(request,'especialidades.html',{})

def como_chegar(request):
	return render(request,'como-chegar.html',{})
