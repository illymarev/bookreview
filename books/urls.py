from django.urls import path
from . import views

app_name = 'books'

urlpatterns = [
    path('', views.BookList.as_view(), name='book-list'),
    path('detail/<pk>/', views.BookDetail.as_view(), name='book-detail'),
    path('quotes/', views.Quotes.as_view(), name='all-quotes'),
    path('quotes/<pk>', views.BookQuotes.as_view(), name='book-quotes')
]