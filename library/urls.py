from django.urls import path
from . import views

urlpatterns = [
    path('all/', views.HomeView.as_view(), name='home'),
    path('bookmark/<int:card_template_id>/', views.BookmarkToggleView.as_view(), name='bookmark_toggle'),
    # path('library/all/', views.SearchView.as_view(), name='search'),
    path('<str:category>/', views.FilterByCategoryView.as_view(), name='filter_by_category'),

]