from django.urls import path
from .views import FetchUniversityDataView, FetchAndStoreUniversityDataView, UniversityListView, UniversityDetailView
urlpatterns = [
    path('fetch_only/',FetchUniversityDataView.as_view(),name='fetch_university_data'),
    path('fetch-and-store/',FetchAndStoreUniversityDataView.as_view(), name='fetch_and_store_university_data'),
    path('list_data/', UniversityListView.as_view(),name='university_list'),
    path('data/<int:pk>/',UniversityDetailView.as_view(),name='university_detail'),
   
]
