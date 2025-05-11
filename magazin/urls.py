from django.urls import path
from .import views 

urlpatterns = [
    
    path('magazin/', views.products,name='products'),
    path('magazin/addprodinb/<int:product_id>/', views.basket_add,name='basket_add'),
    path('magazin/basket', views.basket,name='basket'),
    path('magazin/clear_baskets', views.clear_baskets,name='clear_baskets'),
    path('magazin/basket-deleted/<int:id>/', views.basket_deleted,name='basket_deleted'),
    path('magazin/get/<int:pro_id>',views.product,name='product'),
    path('magazin/ord/',views.orders,name='orders'),
    path('magazin/ord/<int:ord_id>',views.order,name='order'),
    path('magazin/ord/form/',views.orderf,name='orderf'),
    path('magazin/ord/form/add/',views.addorder,name ='addorder'),
    path('magazin/ord/form/addpf/<int:ord_id>',views.addprof,name ='addprof'),
    path('register/',views.RegisterUser.as_view(), name='register'),
    path('login/',views.LoginUser.as_view(), name='login'),
    path('logout/',views.logout_user, name='logout'),
    path('magazin/ord/addfrombasket',views.addorderfrombasket,name='addorderfrombasket'),
    path('magazin/ord/addorderfromforordbasket/<int:id_ord>/',views.addorderfromforordbasket,name='addorderfromforordbasket'),
    
]
