from django.urls import path
from .views import (
    AgentListView,
    AgentCreateView,
    AgentDetailView,
    AgentUpdateView,
    AgentDeletelView,
)

app_name = 'agents'


urlpatterns = [
    path('', AgentListView.as_view(), name='agent-list'),
    path('<int:pk>/', AgentDetailView.as_view(), name='agent-detail'),
    path('<int:pk>/update/', AgentUpdateView.as_view(), name='agent-update'),
    path('<int:pk>/delete/', AgentDeletelView.as_view(), name='agent-delete'),
    path('create/', AgentCreateView.as_view(), name='agent-create'),
]
