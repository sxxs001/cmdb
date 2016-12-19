# -*-coding:utf-8 -*-
from django.shortcuts import render

# Create your views here.


# from django.http import HttpResponse
# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")
#
# def detail(request, question_id):
#     return HttpResponse("You're looking at question %s." % question_id)
#
# def results(request, question_id):
#     response = "You're looking at the results of question %s."
#     return HttpResponse(response % question_id)
#
# def vote(request, question_id):
#     return HttpResponse("You're voting on question %s." % question_id)
#
#




#from django.template import RequestContext, loader
from .models import *

#from django.shortcuts import render

from django.shortcuts import render_to_response
from django.template import RequestContext


def index(request):
    #latest_question_list = Dept.objects.order_by('-dept_name')[:5]
    latest_question_list = Dept.objects.values()
    context = {'latest_question_list': latest_question_list}
    return render(request, 'cmdb/index.html', context)

def index1(request):
    #latest_question_list = Dept.objects.order_by('-dept_name')[:5]
    latest_question_list = Dept.objects.values()
    context = {'latest_question_list': latest_question_list}
    return render(request, 'cmdb/index1.html', context)

#def show_genres(request):
#    return render_to_response("genres.html",
#                          {'nodes':Genre.objects.all()},
#                          context_instance=RequestContext(request))

def products(request):
    #latest_question_list = Dept.objects.order_by('-dept_name')[:5]

    return render_to_response("cmdb/products.html",
                              {'nodes': MPTTProduct.objects.all()},)
                              #context_instance=RequestContext(request))


    #latest_question_list = MPTTProduct.objects.values()
    #context = {'latest_question_list': latest_question_list}
    #return render(request, 'cmdb/products.html', context)

# def index(request):
#     latest_question_list = Dept.objects.order_by('-name')[:5]
#     output = ', '.join([p.question_text for p in latest_question_list])
#     return HttpResponse(output)


# def index(request):
#     #latest_question_list = Dept.objects.order_by('-dept_name')[:5]
#     latest_question_list = Dept.objects.order_by('-dept_name')[:5]
#     template = loader.get_template('cmdb/index.html')
#     context = RequestContext(request, {
#         'latest_question_list': latest_question_list,
#     })
#     return HttpResponse(template.render(context))



from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from cmdb.models import *
from serializers import UserSerializer, GroupSerializer , DeptSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class DeptViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    #queryset = Dept.objects.all()
    queryset = Dept.objects.all()
    serializer_class = DeptSerializer