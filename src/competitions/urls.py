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
    path("<int:pk>/", CompetitionDetailView.as_view()),
    path("<int:pk>/commits/", CompetitionCommitsView.as_view()),
    path("<int:pk>/entries/", CompetitionEntriesView.as_view()),
    path("<int:pk>/entries/<int:entry_pk>/", CompetitionEntryDetailView.as_view()),
    path("<int:pk>/sponsors/", CompetitionSponsorsView.as_view()),
    path("<int:pk>/results/", CompetitionResultsView.as_view()),
    path("<int:pk>/results/<int:result_pk>/", CompetitionResultDetailView.as_view()),
]
