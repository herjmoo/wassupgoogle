from django.urls import path
from MCpolls import views


app_name = 'MCpolls'
urlpatterns = [
    path('', views.index, name='index'),      # /MCpolls/
    path('<int:question_id>/', views.detail, name='detail'),       # /MCpolls/5/
    path('<int:question_id>/results/', views.results, name='results'),     # /MCpolls/5/results/
    path('<int:question_id>/vote/', views.vote, name='vote'),      # /MCpolls/5/vote/
]
