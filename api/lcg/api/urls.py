from django.urls import path
from api.views import *

urlpatterns = [
    path('agreement', Agreements.as_view()),
    path('agreement/<int:id>', Agreements.as_view()),
    path('contact', Contacts.as_view()),
    path('phone', Phones.as_view()),
    path('payment', Payments.as_view()),
    path('loader', LoaderCtl.as_view()),
    path('get_ref', Ref.as_view()),
    path('csi_actions', CsiActions.as_view()),
    path('csi_actions/<int:id>', CsiActions.as_view()),
]
