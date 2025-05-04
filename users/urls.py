from django.urls import path
from .views import (
    UserList, UserDetail, 
    CustomTokenObtainPairView, 
    CheckAdminView, MakeAdminView,
    LogoutView
)

urlpatterns = [
    path('users/', UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetail.as_view(), name='user-detail'),
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('users/admin/<str:email>/', CheckAdminView.as_view(), name='check-admin'),
    path('users/admin/<int:pk>/make-admin/', MakeAdminView.as_view(), name='make-admin'),
]