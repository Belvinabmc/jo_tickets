from django.urls import path
from .views import EventListView, TicketCreateView, MyTicketsView, ValidateTicketView
from mainapp.views import EventListView, TicketCreateView, MyTicketsView, ValidateTicketView
from .views import MyTicketsView
urlpatterns = [
    path('events/', EventListView.as_view(), name='events'),
    path('tickets/buy/', TicketCreateView.as_view(), name='buy-ticket'),
    path('tickets/mine/', MyTicketsView.as_view(), name='my-tickets'),
path('tickets/validate/', ValidateTicketView.as_view(), name='validate-ticket'),]
