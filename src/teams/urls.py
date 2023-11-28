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
    path(":pk/", TeamDetailView.as_view()),
    path(":pk/members/", TeamMembersView.as_view()),
    path(":pk/members/:pk/", TeamMemberDetailView.as_view()),
    path(":pk/invites/", TeamInvitesView.as_view()),
    path(":pk/invites/:pk/", TeamInviteDetailView.as_view()),
]
