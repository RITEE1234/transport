"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, re_path
from app.views import verify_token


urlpatterns = [
    path("admin/", admin.site.urls),
    path('Vendor', views.Vendor, name='Vendor'),
    path('transport', views.transport, name='transport'),
    path('transportlist', views.transportlist, name='transportlist'),
    path('edittransport/<int:id>/', views.transporteditlist,name='transporteditlist'),
    path('deletetransport/<int:id>/',views.deteletransport, name='deletelist'),
    path('signup', views.signup, name='signup'),
    path('login/', views.signin, name='login'),
    path('logout',views.signout),
    path('',views.index),
    path('vendorlist', views.vendorlist, name='vendorlist'),
    path('editvendor/<int:id>/', views.vendoreditlist, name='vendoreditlist'),
    path('deletevendor/<int:id>/', views.detelevendor, name='deletelist'),
    path('truck', views.Operator, name='truck'),
    path('trucklist', views.Trucklist, name='trucklist'),
    path('edittruck/<int:id>/', views.Truckeditlist, name='truckeditlist'),
    path('deletetruck/<int:id>/', views.deletetruck, name='deletetruck'),
    path('labour', views.labour, name='labour'),
    path('labourlist', views.labourlist, name='labourlist'),
    path('editlabour/<int:id>/', views.laboureditlist, name='laboureditlist'),
    path('deletelabour/<int:id>/', views.deletelabour, name='deletelabour'),
    path('invoice', views.invoice, name='invoice'),
    path('invoicelist', views.invoicelist, name='invoicelist'),
    path('editinvoice/<int:id>/', views.invoiceeditlist, name='invoiceeditlist'),
    path('deleteinvoice/<int:id>/', views.deleteinvoice, name='deleteinvoice'),
    path('generate-pdf/<int:id>/', views.generate_pdf, name='generate_pdf'),
    path('verify-token/', verify_token, name='verify_token'),
    path('billformate/<int:id>/', views.billformate, name='billformate'),
    path('billhtml/<int:id>/', views.billhtml, name='billhtml'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
