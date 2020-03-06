from django.shortcuts import render
from django.http import HttpResponse
from .models import Page, Menu, Submenu, Setting, Post, Stories, HomeSettings
from django.views.generic import DetailView, ListView, CreateView
from django.contrib.messages.views import SuccessMessageMixin



# Create your views here.
def index(request):
	pages = Page.objects.all()
	posts = Post.objects.all().order_by('-id')
	menu = Menu.objects.all()
	submenu = Submenu.objects.all()
	setting = Setting.objects.all()
	homesettings = HomeSettings.objects.filter(active=1).order_by('-id')[0]
	context = {'pages': pages, 'menu':menu, 'submenu':submenu, 'setting':setting, 'homesettings':homesettings, 'posts':posts}
	return render(request, 'cms/index.html', context)


#Post List
class PostListView(ListView):
	model = Post
	template_name = 'cms/updates.html'
	context_object_name = 'posts'
	ordering = ['-date_posted']
		#Pass the Menu and Submenu to page for rendering menu
		# Add this to any class view that will use the main_pages.html template
	def get_context_data(self, **kwargs):
		context = super(ListView, self).get_context_data(**kwargs)
		context['Menu'] = Menu.objects.all()
		context['Submenu'] = Submenu.objects.all()
		return context


#Page Loader
class PageDetailView(DetailView):
	model = Page
	#Pass the Menu and Submenu to page for rendering menu
	# Add this to any class view that will use the main_pages.html template
	def get_context_data(self, **kwargs):
		context = super(DetailView, self).get_context_data(**kwargs)
		context['Menu'] = Menu.objects.all()
		context['Submenu'] = Submenu.objects.all()
		return context





#Post Loader
class PostDetailView(DetailView):
	model = Post
	#Pass the Menu and Submenu to page for rendering menu
	# Add this to any class view that will use the main_pages.html template
	def get_context_data(self, **kwargs):
		context = super(DetailView, self).get_context_data(**kwargs)
		context['Menu'] = Menu.objects.all()
		context['Submenu'] = Submenu.objects.all()
		return context


#Story Loader
class StoriesDetailView(DetailView):
	model = Stories
	#Pass the Menu and Submenu to page for rendering menu
	# Add this to any class view that will use the main_pages.html template
	def get_context_data(self, **kwargs):
		context = super(DetailView, self).get_context_data(**kwargs)
		context['Menu'] = Menu.objects.all()
		context['Submenu'] = Submenu.objects.all()
		return context



#story create class
class StoriesCreateView(SuccessMessageMixin, CreateView):
	model = Stories
	fields = ['name', 'email', 'phone', 'content', 'video_link', ] # '__all__'
	success_url = '/story/new/create/'
	success_message = "Your story was successfully submitted, we will be reaching out to you"

	#Pass the Menu and Submenu to page for rendering menu
	# Add this to any class view that will use the main_pages.html template
	def get_context_data(self, **kwargs):
		context = super(CreateView, self).get_context_data(**kwargs)
		context['Menu'] = Menu.objects.all()
		context['Submenu'] = Submenu.objects.all()
		return context


	# take the logged in user and add it to the form
	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

#sample about page
def about(request):
	return render(request, 'cms/about.html')


#sample about page
def fp(request):
	return render(request, 'cms/fp.html')

def page_detail(request, slug):
	page = get_object_or_404(Page, slug=slug)
	return render(request, 'cms/index.html', {'page': page})
