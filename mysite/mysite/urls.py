# -*-coding:utf-8 -*-

"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
#from django.conf.urls import url

from django.conf.urls import  url, include

from django.contrib import admin


import debug_toolbar


#from django.conf.urls import include

from cmdb import views





#django-rest-framework
from rest_framework import routers
#from tutorial.quickstart import views
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'depts', views.DeptViewSet)
#router.register(r'depts_all', views.DeptViewSet)



# if settings.DEBUG:
#    urlpatterns += patterns('', url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT }),
#         url(r'^static/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATIC_ROOT}), )

urlpatterns = [
    #url(r'^cmdb/', include('cmdb.urls', namespace='cmdb')),
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^index1/', views.index1, name='index1'),
    url(r'^products/', views.products, name='products'),

    url(r'^__debug__/', include(debug_toolbar.urls)),
    #(r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': os.path.join(settings.SITE_ROOT,'media')},name='media'),
    #(r'^static/(?P<path>.*)$','django.views.static.serve',{'document_root':'/Users/kk/PycharmProjects/mysite/static/', 'show_indexes': True}),
    #url(r'^static/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': settings.STATIC_ROOT}),


    #url(r'^cmdb/', include('cmdb.urls')),

    # url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # # ex: /polls/5/results/
    # url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # # ex: /polls/5/vote/
    # url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),

    #django-rest-framework
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/', include(router.urls)),
    #url(r'^api/users/', include(router.urls)),
    #url(r'^api/groups/', include(router.urls)),
    #url(r'^api/depts/', include(router.urls)),


]



from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# This will work if DEBUG is True
urlpatterns += staticfiles_urlpatterns()


# import  django.conf.urls.static import static
# from django.conf import settings
#
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

