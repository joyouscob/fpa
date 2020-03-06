from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import State, Lgas, PredictionSearch, Predictions, Probable_Class, HydroAreas, Year
from .forms import SearchForm
import datetime



class SearchCreateView(CreateView):
  model = PredictionSearch
  form_class = SearchForm
  success_url = reverse_lazy('search')



# Prediction Juice
def predict(request):
    states = State.objects.all().order_by('name')
    lgas = Lgas.objects.all()

    if request.method == "POST":
        #Get lga from the form data
        lga_id = request.POST.get('lga')
        now = datetime.datetime.now().year # Get the current year
        year = Year.objects.filter(year=now).first() #filter the year from the database
        predict = Predictions.objects.filter(lga=lga_id, year=year).order_by('lga') # use present year and search for filter
        context = {'states': states, 'lgas':lgas, 'predict': predict} # load contexts
    else:
        context = {'states': states, 'lgas':lgas,}


    return render(request, 'predictions/index.html', context)





# this helps in loading lgas
def load_lgas(request):
  state_id = request.GET.get('state')
  lgas = Lgas.objects.filter(state_id=state_id).order_by('name')
  return render(request, 'predictions/lgas_dropdown_list_options.html', {'lgas': lgas})
