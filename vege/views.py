from django.shortcuts import render,redirect
from vege.models import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url="/Login/")
def Recipes_func(request):
    
    if(request.method=='POST'):
        recipe_name=request.POST.get('recipe_name')
        recipe_description=request.POST.get('recipe_description')
        recipe_image=request.FILES.get('recipe_image')
        
        recipe_obj=Recipes(recipe_name=recipe_name,recipe_description=recipe_description,recipe_image=recipe_image)
        recipe_obj.save()
        messages.success(request,"Your data was save sucessfully!")
        return redirect('/recipes/')
    recipe_data=Recipes.objects.all()
   
    if(request.GET.get('Search')):
        recipe_data=recipe_data.filter(recipe_name__icontains =request.GET.get('Search'))

    
    context={
        'recipe_data':recipe_data,
    }
    return render(request,"Recipes.html",context)

def delete_recipes(request,id):
    delete_obj=Recipes.objects.get(id=id)
    delete_obj.delete()
    messages.success(request,"Your data was deleted sucessfully!")
    return redirect('/recipes/')

def update_recipes(request,id):
    update_data=Recipes.objects.get(id=id)
    if (request.method=="POST"):
        recipe_name=request.POST.get('recipe_name')
        recipe_description=request.POST.get('recipe_description')
        recipe_image=request.FILES.get('recipe_image')
        update_data.recipe_name=recipe_name
        update_data.recipe_description=recipe_description
        if(recipe_image):
            update_data.recipe_image=recipe_image
            
        update_data.save()
        messages.success(request,"Your data was updated sucessfully!")
        return redirect('/recipes/')
        
    context={
        'update_data':update_data
    }
    return render(request,"Recipes_update.html",context)
        
def login_pg(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        if not User.objects.filter(username=username).exists():
            messages.error(request,"Invalid Username")
            return redirect('/Login/')
        
        user=authenticate(username=username,password=password)
        
        if user==None:
            
            messages.error(request,"Invalid Password")
            return redirect('/Login/')
        else:
            login(request,user)
            return redirect("/recipes/")
    return render(request,"Login.html")

def register_pg(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
        else:
            User.objects.create_user(username=username, password=password)
            messages.success(request, "User registered successfully!")
            return redirect('/Login/')
        
    return render(request,"Register.html")
        
def logout_pg(request):
    logout(request)
    return redirect("/Login/")
        

    