from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin 
from .forms import CustomCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login

from django.contrib.auth.decorators import login_required
from miapp.models import *

from django.core.paginator import Paginator
from .forms import ArticlesForm
from django.db.models import Q

# Create your views here.

class Home(LoginRequiredMixin,generic.TemplateView):
    template_name = 'bases/home.html'
    login_url = 'miapp:login'


def home(request):

    articles = Article.objects.all()

    return render(request, 'bases/home.html', {
        
        'articles': articles
    })


def registro(request):
    data = {
        'form': CustomCreationForm()
    }
    if request.method == 'POST':
        formulario = CustomCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            #redirigir al home
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "te has registrado correctamente")
            return redirect(to="/nopor")
        data["form"] = formulario

    return render(request, 'bases/registro.html', data)

#@login_required(login_url='miapp:login')
def pagina(request):

    articles = Article.objects.all()

    return render(request, 'bases/pagina.html', {
        
        'articles': articles
    })

def category(request, category_id):

    category = get_object_or_404(Category, id=category_id)
    articles = Article.objects.filter(categories=category_id)

    return render(request, 'bases/category.html', {
        'category': category,
        'articles': articles
    })

def article(request, article_id):

    article = get_object_or_404(Article, id=article_id)

    return render(request, 'bases/articles.html', {
        'article': article
    })


def nopor(request):
    #sacar articulos
    articles = Article.objects.all()

    #paginar para cada articulo
    paginator = Paginator(articles, 10)

    #recoger numero de pagina
    page = request.GET.get('page')

    page_articles = paginator.get_page(page)

    return render(request, 'bases/nopor.html', {
        'title': 'Articulos',
        'articles': page_articles,
        
    })

    #return render(request, 'bases/nopor.html')

def buscar(request):

    articles = Article.objects.all()

    queryset = request.GET.get("buscar")
    if queryset:
        articles = Article.objects.filter(
            Q(title__icontains= queryset)
        ).distinct()

    return render(request, 'bases/nopor.html',{'articles': articles})


def userpage(request):

    articles = Article.objects.all()

    return render(request, 'bases/userpage.html', {
        'title': 'Articulos',
        'articles': articles,
    })

def crear(request):

    if request.method == "POST":
        formulario = ArticlesForm(request.POST, request.FILES)
        if formulario.is_valid():
            #formulario.save(user=request.user, commit=False)
            post = formulario.save(commit=False)
            post.autor_id = request.user.id
            post.save()
            title = formulario.cleaned_data.get("title")
            messages.success(request, f"el post {title} fue creado")
            return redirect('nopor')
    
    formulario = ArticlesForm()
    
    return render(request, 'bases/crear.html',{
        'formulario': formulario
    })  

def editar(request, id):

    articles = Article.objects.get(id=id)
    formulario = ArticlesForm(request.POST or None, request.FILES or None, instance=articles)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('userpage')

    return render(request, 'bases/editar.html', {'formulario': formulario})

def borrar(request, id):
     
    articles = Article.objects.get(id=id)
    articles.delete()
    return redirect('userpage')








from urllib.request import urlopen
import json 
import requests

def apis(request):

    wea = requests.get('https://random-data-api.com/api/commerce/random_commerce?size=100').json()

    paginator = Paginator(wea,9)
    page = request.GET.get('page')
    page_wea = paginator.get_page(page)

    
    return render(request, 'bases/api.html', {'wea': page_wea})

def apiss(request):

    jon = requests.get('https://api-sismologia-chile.herokuapp.com/').json()

    return render(request, 'bases/sismo.html', {'jon': jon})





    
