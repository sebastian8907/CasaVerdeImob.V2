from django.urls import path
from listings import views

urlpatterns = [
    path('', views.home_page, name='homepage'),
    path('despre-noi/', views.about, name='about'),
    path('adauga-anunt/', views.listing_create, name='listing_create'),
    path('editeaza-anunt/<int:id>/<path:origin_url>/', views.listing_edit, name='listing_edit'),
    path('sterge-anunt/<int:id>/<path:origin_url>/', views.listing_delete, name='sterge_anunt'),
    path('listing/<types>/<transactions>/', views.listing_show, name='listing'),
    path('detalii/<int:pk>/', views.ListingDetailView.as_view(), name='listing_details'),
]