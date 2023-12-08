from django.urls import path

from .views import (
    TeamsView,
    TeamDetailView,
    TeamMembersView,
    TeamMemberDetailView,
    TeamInvitesView,
    TeamInviteDetailView,
)


urlpatterns = [
    path("", TeamsView.as_view()),
    path("<int:pk>/", TeamDetailView.as_view()),
    path("<int:pk>/members/", TeamMembersView.as_view()),
    path("<int:pk>/members/<int:member_pk>/", TeamMemberDetailView.as_view()),
    path("<int:pk>/invites/", TeamInvitesView.as_view()),
    path("<int:pk>/invites/<int:invite_pk>/", TeamInviteDetailView.as_view()),
]
