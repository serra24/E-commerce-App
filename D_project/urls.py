from django.urls import path
from .views import *
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('<int:pk>/',project_details.as_view(),name="project_details"),
    path('',projects.as_view(),name='projects'),
    path('createProject',create_project,name="createProject"),
    path('deleteProject/<int:pk>/',delete_project.as_view(),name="deleteProject"),
    path('donate/<int:project_id>/', donate, name='donate'),
    path('project/<int:project_id>/add_comment/', add_comment, name='add_comment'), 
    path('<int:comment_id>/add_reply/', add_reply, name='add_reply'),
]
