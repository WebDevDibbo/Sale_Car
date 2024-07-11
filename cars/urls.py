from django.urls import path
from . import views
urlpatterns = [
    path('add/', views.AddPostCreateView.as_view(), name = 'add_post'),
    path('edit/<int:id>', views.EditPostView.as_view(), name = 'edit_post'),
    path('delete/<int:id>', views.DeletePost.as_view(), name = 'delete_post'),
    path('details/<int:id>', views.DetailPost.as_view(), name = 'detail_post'),
]
