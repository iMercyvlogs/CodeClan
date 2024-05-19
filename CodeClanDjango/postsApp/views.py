from django.shortcuts import render, get_object_or_404
from .models import PostClass
from django.http import HttpResponse

# Create your views here.

def post_list(request):
    #creating variables that stores all the objects in this class/model
    #order the items based on date of entry
    all_posts=PostClass.objects.all().order_by('date')
    return render(request, 'postsApp/post_list.html',{'all_posts':all_posts})


def post_detail(request,my_slug):

    #return HttpResponse(my_slug)
    thePost=PostClass.objects.get(slug=my_slug)
    #slug here represents the attribute "slug" in the class PostClass
    return render(request, 'postsApp/post_detail.html', {'thePost':thePost})
    

#def post_detail(request,postObj_id):
    #thePost=get_object_or_404(PostClass,pk=postObj_id)
    #return render(request, 'postsApp/post_detail.html', {'thePost':thePost})
