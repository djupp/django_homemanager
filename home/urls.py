from django.conf.urls import patterns, include, url
from django.contrib import admin
from cooking.views import RecipesList, RecipeDetail
from shopping.views import PurchaseCreate, PurchaseDetail, PurchaseList

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'home.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/recipe/$', RecipesList.as_view(),
        name="RecipesList"),
    url(r'^home/recipe/(?P<pk>\d+)$', RecipeDetail.as_view(),
        name="RecipeDetail"),
    url(r'^home/shopping/new$', PurchaseCreate.as_view(),
        name="PurchaseCreate"),
    url(r'^home/purchase/(?P<pk>\d+)$', PurchaseDetail.as_view(),
        name="PurchaseDetail"),
    )
