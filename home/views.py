from django.shortcuts import render
from .models import Post
from django.http import HttpResponseRedirect
from .forms import RegistrationForm

# Create your views here.
def indexHome(request):
   return render(request, 'pages/home.html')

def indexContact(request):
   return render(request, 'pages/contact.html')

def list(request):
   Data = {'Posts': Post.objects.all().order_by("-date")}
   return render(request, "pages/blog.html", Data)

def post(request, post_id):
   post = Post.objects.get(id=post_id)
   return render(request, "pages/post.html", {'post': post})

def register(request):
   form = RegistrationForm()
   if request.method == 'POST':
      form = RegistrationForm(request.POST)
      if form.is_valid():
         form.save()
         return HttpResponseRedirect('/')
   return render(request, 'pages/register.html', {'form': form})