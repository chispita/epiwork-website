from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^profile/$', 'epiweb.apps.survey.profile_views.index'),
    (r'^thanks/$', 'epiweb.apps.survey.survey_views.thanks'),
    (r'^$', 'epiweb.apps.survey.survey_views.index'),
)

