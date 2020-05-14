from django.urls import path

from .views import ham_view, home_view, spam_view

urlpatterns = [
    path('', home_view, name='home'),
    path('home/', home_view, name='home'),
    path('ham/', ham_view, name='ham'),
    path('spam/', spam_view, name='spam'),
]
