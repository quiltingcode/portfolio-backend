from rest_framework import generics, permissions, filters
from portfolio.permissions import IsOwnerOrReadOnly
from .models import Contact
from .serializers import ContactSerializer
from django_filters.rest_framework import DjangoFilterBackend


class ContactList(generics.ListCreateAPIView):
    """
    List contacts or create a contact
    """
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]


class ContactDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a contact, or update or delete it by id.
    """
    permission_classes = [permissions.IsAdminUser]
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
