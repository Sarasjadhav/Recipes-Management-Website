from django.shortcuts import render,HttpResponse

# Create your views here.

def home(request):
    # return HttpResponse("<h2>Hey, This is Home page</h2>")
    
    #this is dictionary in list
    peoples=[
        {'name':'Saras' ,'age':20},
        {'name':'Rohan' ,'age':22},
        {'name':'Aniket' ,'age':23},
        {'name':'Ruhi' ,'age':36},
        {'name':'Tina' ,'age':16},
        
    ]
   
    context={
        'peoples':peoples,
        'title':"home"
        }
    return render(request,"home.html",context) 
# return render(request,"path/home.html") 

def about(request):
    context={
        'title':'about'
    }
    return render(request,"about.html",context)

def contact(request):
    context={
        'title':'contact'
    }
    return render(request,"contact.html",context)


















# How to render list tuple dict in function
# from django.shortcuts import render

# def view_with_multiple_contexts(request):
#     my_list = [1, 2, 3]
#     my_tuple = ("dog", "cat", "rabbit")
#     my_dict = {"title": "Animal List", "count": 3}
    
#     context = {
#         "my_list": my_list,
#         "my_tuple": my_tuple,
#         "my_dict": my_dict
#     }
#     return render(request, "template.html", context)
