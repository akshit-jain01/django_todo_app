from django.urls import path
from . import views
from todolist.settings import DEBUG, STATIC_URL, STATIC_ROOT, MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static
from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns = [
    path('', views.index, name='index'),
    path('upload/', views.upload, name='upload-task'),
    path('update/<int:task_id>', views.update_task),
    path('delete/<int:task_id>', views.delete_task),
    path('bookmark/<int:task_id>', views.bookmark),
    path('snippets/', views.snippet_list),
    path('snippets/<int:pk>/', views.snippet_detail),

]
urlpatterns = format_suffix_patterns(urlpatterns)

if DEBUG:
    urlpatterns += static(STATIC_URL, document_root=STATIC_ROOT)
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
