from django.urls import path

from downloads.views import DownloadCreateView, DownloadDeleteView, DownloadListView, DownloadUpdateView

app_name = 'downloads'

urlpatterns = [
    path('', DownloadListView.as_view(), name='list'),
    path('create/', DownloadCreateView.as_view(), name='create'),
    path('update/', DownloadUpdateView.as_view(), name='update'),
    path('delete/', DownloadDeleteView.as_view(), name='delete'),
]