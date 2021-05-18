from django.shortcuts import render
from .models import *
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import SignUpForm, ReviewForm, SearchForm
from django.views.generic import ListView
from django.http import HttpResponseRedirect


def store(request):
    movie_item = Movie.objects.all()
    cate = Category.objects.all()
    context = {'movie_item': movie_item, "cate": cate}
    return render(request,'myshow/store.html', context)


def cart(request, id):
    moviecart = Movie.objects.filter(id=id)
    context = {'moviecart': moviecart}
    return render(request, 'myshow/cart.html', context)


def checkout(request):
    context = {}
    return render(request, 'myshow/checkout.html', context)


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            messages.success(request, f'Account has been created for {username}')
            # user = authenticate(username=username, password=password)
            # login(request, user)
            return redirect('/')
    else:
        form = SignUpForm(request.POST)
    return render(request, 'myshow/signup.html', {'form': form})


def detail(request, id):
    # od = get_object_or_404(Movie, id=pk)movie = Movie.objects.get(id=id) # select * from movie where id=id
    #     reviews = Review.objects.filter(movie=id).order_by("-comment")

    product = Movie.objects.filter(id=id)
    reviews = Review.objects.filter(movie=id)
    context = {'product': product, 'reviews': reviews}
    return render(request, 'myshow/movieinfo.html', context)


# def movie_review(request, pk):
#     items = Movie_details.objects.filter(id=pk)
#     context = {"items": items}
#     return render(request, 'myshow/reviewpage.html', context)


def add_review(request, id):
    if request.user.is_authenticated:
        movie = Movie.objects.get(id=id)
        if request.method == "POST":
            form = ReviewForm(request.POST or None)
            if form.is_valid():
                data = form.save(commit=False)
                data.comment = request.POST["comment"]
                data.rating = request.POST["rating"]
                data.user = request.user
                data.movie = movie
                data.save()
                return redirect("myshow:detail", id)
        else:
            form = ReviewForm()
        return render(request, 'myshow/movieinfo.html', {"form": form})
    else:
        return redirect("myshow:login")

def search(request):
        query = request.GET['query']
        posts = Movie.objects.filter(movie_name__icontains=query)
        cate = Category.objects.all()
        context = {'posts': posts, "cate": cate}
        return render(request, 'myshow/allmovies.html',context)

def moviefilter(request,id):
    movieshow = Movie.objects.filter(movie_category=id)
    context = {"movieshow": movieshow}
    return render(request, 'myshow/store.html', context)




