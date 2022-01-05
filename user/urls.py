from django.urls import path
from . import views
from user.views import UpdateUser,DeleteUser,editcus_view,userlist,signout

urlpatterns = [
	path('',views.register,name="register"),
    path('signup',views.signup,name="signup"),
    path('edit/user/update/<pk>/',UpdateUser.as_view()),
    path('edit/user/delete/<pk>/',DeleteUser.as_view()),
    # path('edit/user/',editcus_view),
    path('details/',userlist),
    path('signout', views.signout, name='signout')
]