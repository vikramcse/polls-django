from django.conf.urls import url

from . import views

# When Django finds a regular expression match, Django calls the specified view function, 
# with an HttpRequest object as the first argument and any captured values from the 
# regular expression as other arguments.
# In this case the index function is called in the views.py

urlpatterns = [
	# ex: /polls/
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]