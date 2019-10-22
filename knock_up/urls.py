from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('teller_add_voter', views.teller_add_voter, name='teller_add_voter'),
    path('teller_check_voter', views.teller_check_voter, name='teller_check_voter'),
    path('teller_delete_voter', views.teller_delete_voter, name='teller_delete_voter'),
    path('admin_list_voters', views.admin_list_voters, name='admin_list_voters'),
    path('admin_assign_voters', views.admin_assign_voters, name='admin_assign_voters'),
    path('knocker_list', views.knocker_list, name='knocker_list'),
    path('knocker_delete', views.knocker_delete, name='knocker_delete')

]

#     path('', views.logon, name='logon'),