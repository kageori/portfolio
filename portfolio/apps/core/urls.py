from django.urls import path
from .views import WorksView, WorkDetailView, InformationIndexView, IndexView, CvView, StatementView, ContactFormView, ContactResultView


app_name = 'core'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('information_list/', InformationIndexView.as_view(), name='information_list'),
    path('works_list/', WorksView.as_view(), name='works_list'),
    path('work/<slug:slug>/',  WorkDetailView.as_view(), name='work_detail'),
    path('cv/', CvView.as_view(),name='cv_list'),
    path('statement/', StatementView.index, name='statement'),
    path('contact/', ContactFormView.as_view(), name='contact_form'),
    path('contact/result/', ContactResultView.as_view(), name='contact_result'),
]