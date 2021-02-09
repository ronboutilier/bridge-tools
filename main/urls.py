"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "main"

urlpatterns = [
	path("", views.homepage,name="homepage"),
	path("register/", views.register,name="register"),
	path("logout/", views.logout_request,name="logout"),
	path("login/", views.login_request,name="login"),
    path('getting_started/', views.getting_started, name='getting_started'),
    path('bridge_mechanics/', views.bridge_mechanics, name='bridge_mechanics'),
    path('ubit_videos/', views.ubit_videos, name='ubit_videos'),
    path('<slug:trip>', views.bridge_space, name="bridge_space"),
    path('<slug:trip>/delete_trip', views.delete_trip, name="delete_trip"),
    path('<slug:trip>/cover_sheet', views.cover_sheet, name="cover_sheet"),
    path('<slug:trip>/checkout_check', views.checkout_check, name="checkout_check"),
    path('<slug:trip>/<slug:structure_id>', views.bridge_view, name="bridge_view"),
    path('<slug:trip>/<slug:structure_id>/bridge_model', views.bridge_model, name="bridge_model"),
    path('<slug:trip>/<slug:structure_id>/inspected', views.inspected, name="inspected"),
    path('<slug:trip>/<slug:structure_id>/trip_notes', views.trip_notes, name="trip_notes"),     
    path('<slug:trip>/<slug:structure_id>/<int:element_id>', views.element_view, name="element_view"),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
