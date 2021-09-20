from django.shortcuts import render
from Post_Img.models import PostImage


# Create your views here.
def posts_img(request):
    posts = PostImage.objects.all()
    ctx = {'posts': posts}
    return render(request, 'Home.html', ctx)
