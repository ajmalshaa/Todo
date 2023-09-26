from django.urls import path
from . import views
urlpatterns=[

    path('',views.home,name='home'),
    path('signup/',views.signup,name='signup'),
    path('delete/<int:del_id>', views.delete, name='delete'),
    path('complete',views.complete,name='complete'),
    path('edit',views.edit,name='edit'),
    path('signin',views.signin,name='signin'),
    path('update/<int:update_id>',views.update,name='update'),
    path('search',views.search,name='search'),

    path('signout',views.signout,name='signout'),
    path('delete_update/<int:delup_id>',views.delete_update,name='delete_update'),
    path('Deleted',views.Deleted,name='Deleted'),
    path('save',views.save,name='save'),
    path('retrieve/<int:ret_id>',views.retrieve,name='retrieve'),
    path('open/<int:open_id>',views.open,name='open'),
    path('Sessionout',views.Sessionout,name='Sessionout'),
    path('piechart/', views.pie_chart, name='piechart'),

]