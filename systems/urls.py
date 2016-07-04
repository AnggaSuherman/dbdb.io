from django.conf.urls import patterns, url, include
from rest_framework import routers
from systems import views

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browseable API.
urlpatterns = patterns('',
    # Homepage
    url(r'^$', views.HomePage.as_view()),

    # Database related urls
    url(r'^db/version/(?P<db_name>[A-Za-z0-9-_]+)/(?P<version>[0-9]+)', views.DatabaseVersionPage.as_view()),
    url(r'^db/(?P<db_name>[A-Za-z0-9-_]+)/revisions', views.DatabaseRevisionsPage.as_view()),
    url(r'^db/(?P<db_name>[A-Za-z0-9-_]+)/(?P<key>[A-Za-z0-9-_]+)/revisions', views.DatabaseRevisionsPage.as_view()),
    url(r'^db/(?P<db_name>[A-Za-z0-9-_]+)/(?P<key>[A-Za-z0-9-_]+)', views.DatabaseEditingPage.as_view()),
    url(r'^db/(?P<db_name>[A-Za-z0-9-_]+)', views.DatabasePage.as_view()),

    # Search Related urls
    url(r'^advancedsearch/', views.AdvancedSearchView.as_view()),
    url(r'^search/(?P<page_type>[A-Za-z0-9-_]+)/(?P<name>[A-Za-z0-9-_]+)', views.OSPage.as_view()),
    url(r'^language/(?P<lang_name>[A-Za-z0-9-_]+)', views.LangPage.as_view()),
    url(r'^alphabetized/', views.AlphabetizedData.as_view()),

    # Suggest a new system
    url(r'^suggest/', views.MissingSystemView.as_view()),
    
    # About
    url(r'^about/$', views.AboutView.as_view(), name='about'),


    # Add publications
    url(r'^addpublication/', views.AddPublication.as_view()),

    # Creation related urls, only createdb/ works
    url(r'^createdb/', views.DatabaseCreationPage.as_view()),
    url(r'^createlanguage', views.PLCreationView.as_view()),
    url(r'^createos', views.OSCreationView.as_view()),

    # api urls
    url(r'^1/all_systems', views.FetchAllSystems.as_view()),
    url(r'^editsrss/', views.LatestEdits())
)
