from django.conf.urls import patterns, include, url
from django.contrib import admin
from cooking.views import RecipesList, RecipeDetail

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'home.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/recipe/$', RecipesList.as_view(),
        name="RecipesList"),
    url(r'^home/recipe/(?P<pk>\d+)$', RecipeDetail.as_view(),
        name="RecipeDetail")
    )
