from django.shortcuts import render, reverse,\
    HttpResponseRedirect, HttpResponse
from recipes_app.models import Author, Recipe
from recipes_app.forms import RecipesAddForm, AuthorAddForm, ImageForm

def index(request):
    html = "index.html"
    data = Recipe.objects.all()
    return render (request, html, {"data": data})

def recipesadd(request):
    html = "generic_form.html"
    if request.method == 'POST':
        form = RecipesAddForm(request.POST)
        if form.is_valid():
            recipe = form.cleaned_data
            Recipe.objects.create(
                title = recipe['title'],
                author = recipe['author'],
                description = recipe['description'],
                instructions = recipe['instructions'],
                time_required = recipe['time_required']
            )
            return HttpResponseRedirect(reverse("homepage"))
    form = RecipesAddForm()
    return render(request, html, {"form": form})

def authoradd(request):
    html = "generic_form.html"
    if request.method == 'POST':
        form = AuthorAddForm(request.POST)
        if form.is_valid():
            author = form.cleaned_data
            Author.objects.create(
                name = author['name'],
                bio = author['bio']
            )
            return HttpResponseRedirect(reverse("homepage"))
    form = AuthorAddForm()
    return render(request, html, {"form": form})

def imageadd(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("success")
    else:
        form = ImageForm()
    return render(request, 'generic_form.html', {'form': form})

def success(request):
    return HttpResponseRedirect("upload successful")


def recipe_view(request, id):
    html = "recipe.html"
    recipe = Recipe.objects.get(id=id)
    return render(request, html, {"recipe": recipe})

def author_view(request, id):
    html = "bio.html"
    bio = Author.objects.get(id=id)
    recipe = Recipe.objects.filter(author=bio)
    return render(request, html, {"bio": bio, "recipe": recipe})
