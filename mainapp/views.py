from django.shortcuts import render
def home_view(request): 
    return render(request, "index.html")
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Event
from .serializers import EventSerializer, TicketSerializer, TicketCreateSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from rest_framework.generics import ListAPIView
from .models import Ticket
from .serializers import TicketSerializer


class MyTicketsView(ListAPIView):
    serializer_class = TicketSerializer
    serializer_class = TicketSerializer
    permission_classes =[IsAuthenticated]

    def get_queryset(self):
        return Ticket.objects.filter(user=self.request.user)

# Liste des matchs
class EventListView(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

# Créer un ticket (achat billet)
class TicketCreateView(generics.CreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(supporter=self.request.user)

# Voir ses propres billets
class MyTicketsView(generics.ListAPIView):
    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Ticket.objects.filter (user=self.request.user)


# Scan QR pour stadier
class ValidateTicketView(APIView):
    def post(self, request):
        ticket_id = request.data.get("ticket_id")
        ticket = get_object_or_404(Ticket, id=ticket_id)

        if ticket.is_used:
            return Response({"message": "Billet déjà utilisé"}, status=400)

        ticket.is_used = True
        ticket.save()
        return Response({"message": "Billet valide - entrée autorisée"}, status=200)


class EventListView(APIView):
    def get(self, request):
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)