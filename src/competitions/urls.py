from django.urls import path

from .views import (
    CompetitionsView,
    LatestCompetitionView,
    CompetitionDetailView,
    CompetitionCommitsView,
    CompetitionEntriesView,
    CompetitionEntryDetailView,
    CompetitionSponsorsView,
    CompetitionResultsView,
    CompetitionResultDetailView,
)


urlpatterns = [
    path("", CompetitionsView.as_view()),
    path("latest/", LatestCompetitionView.as_view()),
    path(":pk/", CompetitionDetailView.as_view()),
    path(":pk/commits/", CompetitionCommitsView.as_view()),
    path(":pk/entries/", CompetitionEntriesView.as_view()),
    path(":pk/entries/:entry_pk/", CompetitionEntryDetailView.as_view()),
    path(":pk/sponsors/", CompetitionSponsorsView.as_view()),
    path(":pk/results/", CompetitionResultsView.as_view()),
    path(":pk/results/:result_pk/", CompetitionResultDetailView.as_view()),
]
