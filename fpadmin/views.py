from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from cms.models import *
from users.models import *
from predictions.models import * # import all models from predictions app
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
# for messages in the delete class
from django.contrib import messages
from django.forms import modelformset_factory



# Create your views here.
@login_required
def index(request):
	return render(request, 'fpadmin/index.html')

#MULTIPLE DELETE PAGE
@login_required
def deleteMultiple(request):
	if request.method == 'POST':
		Page.objects.filter(id__in=request.POST.getlist('id')).delete()
		messages.success(request, 'Pages were deleted!', extra_tags='alert')
		return redirect('/fpadmin/page/list/')


#post update class
class HomePageUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
	model = HomeSettings
	fields = ['mini_header_right', 'phone', 'email', 'video', 'title', 'content', 'link', 'section1', 'section2', 'footer', 'copyright_text', 'site_name', 'toppage_notification', 'website', 'active']#'__all__'
	template_name = 'fpadmin/home_editor.html'
	success_url = '/fpadmin/home/editor/'
	success_message = "Home Page Updated!"


	# take the logged in user and add it to the form
	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

#page create class
class PageCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
	model = Page
	template_name = 'fpadmin/page_form.html'
	fields = ['title', 'content', 'slug'] # '__all__'
	success_url = '/fpadmin/page/create/'
	success_message = "Page Created!"


	# take the logged in user and add it to the form
	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)





#page update class
class PageUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
	model = Page
	template_name = 'fpadmin/page_form.html'
	fields = ['title', 'content', 'slug'] # '__all__'
	success_url = '/fpadmin/page/list/'
	success_message = "Page Updated!"


	# take the logged in user and add it to the form
	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)


#page Delete class
class PageDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
	model = Page
	template_name = 'fpadmin/page_delete.html'
	success_url = '/fpadmin/page/list/'
	success_message = "Page Deleted!"

	#Initialize the page delete success message
	def delete(self, request, *args, **kwargs):
		messages.success(self.request, self.success_message)
		return super(PageDeleteView, self).delete(request, *args, **kwargs)

	# take the logged in user and add it to the form
	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

		# Add this to any class view that will use the main_pages.html template
	def get_context_data(self, **kwargs):
		context = super(DeleteView, self).get_context_data(**kwargs)
		context['Menu'] = Menu.objects.all()
		context['PageMenu'] = Menu.objects.all()
		context['Submenu'] = Submenu.objects.all()
		return context



#Page List
class PageListView(LoginRequiredMixin, ListView):
	model = Page
	template_name = 'fpadmin/page_list.html'
	context_object_name = 'pages'
	ordering = ['-date_posted']
		#Pass the Menu and Submenu to page for rendering menu
		# Add this to any class view that will use the main_pages.html template
	def get_context_data(self, **kwargs):
		context = super(ListView, self).get_context_data(**kwargs)
		context['Menu'] = Menu.objects.all()
		context['Submenu'] = Submenu.objects.all()
		return context


#Menu List
class MenuListView(LoginRequiredMixin, ListView):
	model = Menu
	template_name = 'fpadmin/menu_list.html'
	context_object_name = 'menus'
	ordering = ['-date_created']
		#Pass the Menu and Submenu to page for rendering menu
		# Add this to any class view that will use the main_pages.html template
	def get_context_data(self, **kwargs):
		context = super(ListView, self).get_context_data(**kwargs)
		context['Menu'] = Menu.objects.all()
		context['Submenu'] = Submenu.objects.all()
		return context



#Menu create class
class MenuCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
	model = Menu
	template_name = 'fpadmin/menu_form.html'
	fields = ['title', 'page'] #'__all__'
	success_url = '/fpadmin/menu/list/'
	success_message = "Menu Created!"


	# take the logged in user and add it to the form
	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)



#Menu update class
class MenuUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
	model = Menu
	template_name = 'fpadmin/menu_form.html'
	fields = ['title', 'page'] #'__all__'
	success_url = '/fpadmin/menu/list/'
	success_message = "Menu Updated!"


	# take the logged in user and add it to the form
	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)


#Menu delete class
class MenuDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
	model = Menu
	template_name = 'fpadmin/menu_delete.html'
	success_url = '/fpadmin/menu/list/'
	success_message = "Menu Deleted!"

	#Initialize the page delete success message
	def delete(self, request, *args, **kwargs):
		messages.success(self.request, self.success_message)
		return super(MenuDeleteView, self).delete(request, *args, **kwargs)

	# take the logged in user and add it to the form
	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)



#Menu List
class SubMenuListView(LoginRequiredMixin, ListView):
	model = Submenu
	template_name = 'fpadmin/submenu_list.html'
	context_object_name = 'menus'
	ordering = ['-date_created']
		#Pass the Menu and Submenu to page for rendering menu
		# Add this to any class view that will use the main_pages.html template
	def get_context_data(self, **kwargs):
		context = super(ListView, self).get_context_data(**kwargs)
		context['Menu'] = Menu.objects.all()
		context['Submenu'] = Submenu.objects.all()
		return context

#Menu create class
class SubMenuCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
	model = Submenu
	template_name = 'fpadmin/submenu_form.html'
	fields = ['title', 'menuid', 'page']#'__all__'
	success_url = '/fpadmin/submenu/list/'
	success_message = "Sub-Menu Created!"


	# take the logged in user and add it to the form
	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)



#Menu create class
class SubMenuUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
	model = Submenu
	template_name = 'fpadmin/submenu_form.html'
	fields = ['title', 'menuid', 'page']#'__all__'
	success_url = '/fpadmin/submenu/list/'
	success_message = "Sub-Menu Updated!"


	# take the logged in user and add it to the form
	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)



#Menu delete class
class SubMenuDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
	model = Submenu
	template_name = 'fpadmin/submenu_delete.html'
	success_url = '/fpadmin/submenu/list/'
	success_message = "Sub-Menu Deleted!"

	#Initialize the page delete success message
	def delete(self, request, *args, **kwargs):
		messages.success(self.request, self.success_message)
		return super(SubMenuDeleteView, self).delete(request, *args, **kwargs)

	# take the logged in user and add it to the form
	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)


#Post List
class PostListView(LoginRequiredMixin, ListView):
	model = Post
	template_name = 'fpadmin/post_list.html'
	context_object_name = 'posts'
	ordering = ['-date_posted']
		#Pass the Menu and Submenu to page for rendering menu
		# Add this to any class view that will use the main_pages.html template
	def get_context_data(self, **kwargs):
		context = super(ListView, self).get_context_data(**kwargs)
		context['Menu'] = Menu.objects.all()
		context['Submenu'] = Submenu.objects.all()
		return context


#post create class
class PostCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
	model = Post
	fields = ['title', 'content', 'slug'] # '__all__'
	template_name = 'fpadmin/post_form.html'
	success_url = '/fpadmin/post/create/'
	success_message = "Post Created!"


	# take the logged in user and add it to the form
	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)



#post update class
class PostUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
	model = Post
	fields = ['title', 'content', 'slug'] # '__all__'
	template_name = 'fpadmin/post_form.html'
	success_url = '/fpadmin/post/list/'
	success_message = "Post Updated!"


	# take the logged in user and add it to the form
	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)


#post delete class
class PostDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
	model = Post
	template_name = 'fpadmin/post_delete.html'
	success_url = '/fpadmin/post/list/'
	success_message = "Post Deleted!"

	def delete(self, request, *args, **kwargs):
		messages.success(self.request, self.success_message)
		return super(PostDeleteView, self).delete(request, *args, **kwargs)

	# take the logged in user and add it to the form
	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)


#stories create class
class StoriesCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
	model = Stories
	fields = ['title', 'content', 'video_link', 'name', 'email', 'phone', 'slug'] # '__all__'
	success_url = '/fpadmin/post/create/'
	success_message = "Story Created!"


	# take the logged in user and add it to the form
	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)


#Stories List
class StoriesListView(LoginRequiredMixin, ListView):
	model = Stories
	template_name = 'fpadmin/stories_list.html'
	context_object_name = 'stories'
	ordering = ['-date_posted']



#Stories Delete
class StoriesDeleteView(LoginRequiredMixin, DeleteView):
	model = Stories
	template_name = 'fpadmin/stories_delete.html'
	success_url = '/fpadmin/stories/list/'
	success_message = "Story Deleted!"

	def delete(self, request, *args, **kwargs):
		messages.success(self.request, self.success_message)
		return super(StoriesDeleteView, self).delete(request, *args, **kwargs)



#Stories List
#Story Loader
class StoriesDetailView(LoginRequiredMixin, DetailView):
	model = Stories
	template_name = 'fpadmin/stories_detail.html'
	



#Predictions List
class PredictionsListView(LoginRequiredMixin, ListView):
	model = Predictions
	template_name = 'fpadmin/predictions_list.html'
	context_object_name = 'predictions'
	ordering = ['-created_date']


#Predictino single create class
class PredictionsCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
	model = Predictions
	fields = ['state', 'lga', 'year', 'prediction', 'actual_occurence']#'__all__'
	success_url = '/fpadmin/predictions/create/'
	success_message = "Prediction Created!"
	template_name = 'fpadmin/predictions_form.html'

	# take the logged in user and add it to the form
	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)



#Add Multiple Predictions
def PredictionsCreate(request):
	PredictionFormSet = modelformset_factory(Predictions, fields=('state', 'lga', 'year', 'prediction'), extra=4)
	if request.method == 'POST':
		form = PredictionFormSet(request.POST)
		# instances = form.save(commit=False)
		#
		# for instance in instances:
		# 	instance.save()
		if form.is_valid():
			instances = form.save()
			messages.success(request, 'Predictions were added!', extra_tags='alert')
			return redirect('/fpadmin/predictions/list')

	form = PredictionFormSet(queryset=Predictions.objects.none())
	# list out the latest filled in Predictions
	predictions = Predictions.objects.all().order_by('-id')[:10]
	return render(request, 'fpadmin/predictions_multiple_form.html', {'form': form, 'predictions':predictions})




#Predictino single create class
class PredictionsUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
	model = Predictions
	fields = ['state', 'lga', 'year', 'prediction', 'actual_occurence']#'__all__'
	success_url = '/fpadmin/predictions/list/'
	success_message = "Prediction Updated!"
	template_name = 'fpadmin/predictions_form.html'

	# take the logged in user and add it to the form
	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)


#Predictino single delete class
class PredictionsDeleteView(LoginRequiredMixin, DeleteView):
	model = Predictions
	success_url = '/fpadmin/predictions/list/'
	success_message = "Prediction Deleted!"
	template_name = 'fpadmin/prediction_delete.html'

	def delete(self, request, *args, **kwargs):
		messages.success(self.request, self.success_message)
		return super(PredictionsDeleteView, self).delete(request, *args, **kwargs)



#LGAs List
class LgasListView(LoginRequiredMixin, ListView):
	model = Lgas
	template_name = 'fpadmin/lgas_list.html'
	context_object_name = 'lgas'
	ordering = ['-create_date']

#Add Multiple Lgas
def LgasCreate(request):
	LgaFormSet = modelformset_factory(Lgas, fields=('state', 'name', 'lat', 'lng', 'hydro_area'), extra=4)
	if request.method == 'POST':
		form = LgaFormSet(request.POST)
		# instances = form.save(commit=False)
		#
		# for instance in instances:
		# 	instance.save()
		if form.is_valid():
			instances = form.save()
			messages.success(request, 'Lgas were added!', extra_tags='alert')
			return redirect('/fpadmin/lgas/list')

	form = LgaFormSet(queryset=Lgas.objects.none())
	# list out the latest filled in LGAs
	lgas = Lgas.objects.all().order_by('-id')[:10]
	return render(request, 'fpadmin/lgas_multiple_form.html', {'form': form, 'lgas':lgas})



#Predictino single create class
class LgasUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
	model = Lgas
	fields = ['state', 'name', 'lat', 'lng', 'hydro_area']#'__all__'
	success_url = '/fpadmin/lgas/list/'
	success_message = "Local Government Data Successfully Updated!"
	template_name = 'fpadmin/lgas_form.html'

	# take the logged in user and add it to the form
	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)



#Lgas List
class LgasDeleteView(LoginRequiredMixin, DeleteView):
	model = Lgas
	template_name = 'fpadmin/lgas_delete.html'
	success_url = '/fpadmin/lgas/list/'
	success_message = "Local Government Data Deleted!"

	def delete(self, request, *args, **kwargs):
		messages.success(self.request, self.success_message)
		return super(LgasDeleteView, self).delete(request, *args, **kwargs)


# this helps in loading lgas
def load_lgas(request):
  state_id = request.GET.get('state')
  lgas = Lgas.objects.filter(state_id=state_id).order_by('name')
  return render(request, 'fpadmin/lga_loader.html', {'lgas': lgas})
