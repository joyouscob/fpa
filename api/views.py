from django.shortcuts import render, redirect
from django.http import JsonResponse
from cms.models import *
from users.models import *
from predictions.models import * # import all models from predictions app

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
import datetime
# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'All Pages':'pages/',
        'Single Page - ID':'page/<id>',
        'Single Page - Slug':'page/slug/<slug>',
        'All Posts':'posts/',
        'Single Post - ID':'post/<id>',
        'Single Post - Slug':'post/slug/<slug>',
        'All States':'states/',
        'Single State':'state/<id>',
        'All Local Governements':'lgas/',
        'Single Local Government':'lga/<id>',
        'All Local Government in a State - ID':'lgas/state/<id>',
        'All Menu':'menu/',
        'Single Submenu':'submenu/<id>',
        'All Submenu in a Menu':'submenu/menu/<id>',
        'All Submenu':'submenu/',
        'All Hydro Areas':'hydroareas/',
        'Single Hydro Area':'hydroarea/<id>',
        'All Predictions':'predictions/',
        'Single Prediction - Lga_id, year':'prediction/lga_id/year',
        'All Probable Class':'probableclass/',
        'Create Story':'stories/create/',
        }
    return Response(api_urls)


'''
####
PAGES API
####
'''

#view all pages
@api_view(['GET'])
def pageList(request):
    page = Page.objects.all()
    serializer = PageSerializers(page, many=True)
    return Response(serializer.data)

#view detail Page using id
@api_view(['GET'])
def pageDetail(request, pk):
    page = Page.objects.get(id=pk)
    serializer = PageSerializers(page, many=False)
    return Response(serializer.data)

#view detail Page using slug
@api_view(['GET'])
def pageSlugDetail(request, slug):
    page = Page.objects.get(slug=slug)
    serializer = PageSerializers(page, many=False)
    return Response(serializer.data)


'''
####
POSTS API
####
'''

#view all posts
@api_view(['GET'])
def postList(request):
    post = Post.objects.all()
    serializer = PostSerializers(post, many=True)
    return Response(serializer.data)

#view detail post using id
@api_view(['GET'])
def postDetail(request, pk):
    post = Post.objects.get(id=pk)
    serializer = PostSerializers(post, many=False)
    return Response(serializer.data)

#view detail post using slug
@api_view(['GET'])
def postSlugDetail(request, slug):
    post = Post.objects.get(slug=slug)
    serializer = PostSerializers(post, many=False)
    return Response(serializer.data)


'''
####
STATES
####
'''

#view all States
@api_view(['GET'])
def stateList(request):
    state = State.objects.all()
    serializer = StateSerializers(state, many=True)
    return Response(serializer.data)

#view State Detail by id
@api_view(['GET'])
def stateDetail(request, pk):
    state = State.objects.get(id=pk)
    serializer = StateSerializers(state, many=False)
    return Response(serializer.data)

'''
####
LGA
####
'''

#view all Lgas
@api_view(['GET'])
def lgaList(request):
    lga = Lgas.objects.all()
    serializer = LgaSerializers(lga, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def lgasList(request):
    lga = Lgas.objects.all()
    serializer = LgasSerializers(lga, many=True)
    return Response(serializer.data)



#view all Lgas
@api_view(['GET'])
def lgaDetail(request, pk):
    lga = Lgas.objects.get(id=pk)
    serializer = LgaSerializers(lga, many=False)
    return Response(serializer.data)


# Filter LGAs to State,
@api_view(['GET'])
def lgasUnderState(request, pk):
    lga = Lgas.objects.filter(state=pk).order_by('name')
    serializer = LgaSerializers(lga, many=True)
    return Response(serializer.data)


'''
####
MENU
####
'''
#view all Menu
@api_view(['GET'])
def menuList(request):
    menu = Menu.objects.all()
    serializer = MenuSerializers(menu, many=True)
    return Response(serializer.data)

'''
####
SUBMENU
TODO - Filter Submenu to Menu
####
'''
#view all Submenus
@api_view(['GET'])
def submenuList(request):
    submenu = Submenu.objects.all()
    serializer = SubMenuSerializers(submenu, many=True)
    return Response(serializer.data)

#view single submenu
@api_view(['GET'])
def submenuDetail(request, pk):
    submenu = Submenu.objects.get(id=pk)
    serializer = SubMenuSerializers(submenu, many=False)
    return Response(serializer.data)

#view Submenu based on menu id
@api_view(['GET'])
def submenuToMenuDetail(request, pk):
    submenu = Submenu.objects.filter(menuid=pk).order_by('id')
    serializer = SubMenuSerializers(submenu, many=True)
    return Response(serializer.data)



'''
####
HYDRO AREAS
####
'''
#view all Hydroareas
@api_view(['GET'])
def hydroareasList(request):
    hydroareas = HydroAreas.objects.all()
    serializer = HydroAreasSerializers(hydroareas, many=True)
    return Response(serializer.data)

#view all Hydroareas
@api_view(['GET'])
def hydroareasDetail(request, pk):
    hydroareas = HydroAreas.objects.get(id=pk)
    serializer = HydroAreasSerializers(hydroareas, many=False)
    return Response(serializer.data)

'''
####
PROBABLE CLASS
####
'''
#view all Probable Class
@api_view(['GET'])
def probableclassList(request):
    probableclass = Probable_Class.objects.all()
    serializer = ProbableClassSerializers(probableclass, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def probableclassList(request, pk):
    probableclass = Probable_Class.objects.get(id=pk)
    serializer = ProbableClassSerializers(probableclass, many=False)
    return Response(serializer.data)

'''
####
POSTS
####
'''

#view all Predictions
@api_view(['GET'])
def predictionsList(request):
    predictions = Predictions.objects.all()
    serializer = PredictionsSerializers(predictions, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def predictionsDetail(request, lga_id, year):
    # now = datetime.datetime.now().year #get present year
    year= Year.objects.get(year=year) #get the id of the year from Year database
    #Gets and filter by lga_id and year from the year above
    predictions = Predictions.objects.get(lga=lga_id, year=year,)
    #We serialize the main prediction data
    prediction_main = PredictionsSerializers(predictions, many=False)
    #Using prediction.prediction.id, We filter data from the probable class table
    prediction_a =  Probable_Class.objects.get(id=predictions.prediction.id)
    # serialize data from the probable table
    prediction_data = ProbableClassSerializers(prediction_a, many=False)
    # We do the same for LGA and Hydro areas
    lga = Lgas.objects.get(id=lga_id)
    lga_a = LgaSerializers(lga, many=False)
    hydroarea = HydroAreasSerializers(lga.hydro_area, many=False)
    return Response({
        'prediction':prediction_main.data,
        'Lga': lga_a.data,
        'hydroarea':hydroarea.data,
        'prediction_data':prediction_data.data,
        })

@api_view(['POST'])
def storiesCreate(request):
    serializer = StoriesClassSerializers(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
