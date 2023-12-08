from django.contrib.auth.decorators import login_required

from microapi import (
    ApiView,
    # ModelSerializer,
)
from microapi import http

from entries.models import (
    Entry,
    Commit,
)

from .models import Competition


class CompetitionsView(ApiView):
    def serialize(self, obj):
        return self.serializer.to_dict(obj, exclude=["is_deleted"])

    def get(self, request):
        competitions = Competition.objects.active().order_by("-contest_start_date")
        return self.render(
            {
                "success": True,
                "competitions": self.serialize_many(competitions),
            }
        )


class LatestCompetitionView(ApiView):
    def serialize(self, obj):
        return self.serializer.to_dict(obj, exclude=["is_deleted"])

    def get(self, request):
        competition = Competition.objects.active().latest("contest_start_date")
        return self.render(
            {
                "success": True,
                "competition": self.serialize(competition),
            }
        )


class CompetitionDetailView(ApiView):
    def serialize(self, obj):
        return self.serializer.to_dict(obj, exclude=["is_deleted"])

    def get(self, request, pk):
        competition = Competition.objects.active().get(pk=pk)
        return self.render(
            {
                "success": True,
                "competition": self.serialize(competition),
            }
        )


class CompetitionCommitsView(ApiView):
    # def serialize(self, obj):
    #     return {
    #         "id": obj.id,
    #         # FIXME: Fix serialization.
    #         "entry": obj.entry,
    #         # FIXME: Fix serialization.
    #         "committer": obj.committer,
    #         "gravatar": obj.gravatar,
    #         "commit_id": obj.commit_id,
    #         "email": obj.email,
    #         "message": obj.message,
    #         "short_message": obj.short_message(),
    #         "created": obj.created,
    #     }

    def get(self, request, pk):
        competition = Competition.objects.active().get(pk=pk)
        commits = Commit.objects.filter(entry__competition=competition).order_by(
            "-created"
        )[:30]
        return self.render(
            {
                "success": True,
                "competitions": self.serialize_many(commits),
            }
        )


class CompetitionEntriesView(ApiView):
    def serialize(self, obj):
        return {
            "id": obj.id,
            # FIXME: Fix serialization.
            "team": obj.team,
            # FIXME: Fix serialization.
            "team_members": obj.team_members,
            "name": obj.name,
            "description": obj.description,
            "repository_url": obj.repository_url,
            "created": obj.created,
            "updated": obj.updated,
        }

    def get(self, request, pk):
        competition = Competition.objects.active().filter(pk=pk)
        entries = (
            Entry.objects.active().filter(competition=competition).order_by("name")
        )
        return self.render(
            {
                "success": True,
                "entries": self.serialize_many(entries),
            }
        )

    @login_required
    def post(self, request, pk):
        return self.render({}, status_code=http.CREATED)


class CompetitionEntryDetailView(ApiView):
    def serialize(self, obj):
        return {
            "id": obj.id,
            # FIXME: Fix serialization.
            "team": obj.team,
            # FIXME: Fix serialization.
            "team_members": obj.team_members,
            "name": obj.name,
            "description": obj.description,
            "repository_url": obj.repository_url,
            "created": obj.created,
            "updated": obj.updated,
        }

    def get(self, request, pk, entry_pk):
        competition = Competition.objects.active().filter(pk=pk)
        entry = Entry.objects.active().filter(competition=competition, pk=entry_pk)
        return self.render(
            {
                "success": True,
                "entry": self.serialize(entry),
            }
        )

    @login_required
    def put(self, request, pk):
        return self.render({}, status_code=http.ACCEPTED)

    @login_required
    def delete(self, request, pk):
        return self.render({}, status_code=http.NO_CONTENT)


class CompetitionSponsorsView(ApiView):
    def serialize(self, obj):
        return {
            "id": obj.id,
            "name": obj.name,
            "url": obj.url,
            "description": obj.description,
            "created": obj.created,
            "updated": obj.updated,
        }

    def get(self, request, pk):
        competition = Competition.objects.active().filter(pk=pk)
        sponsors = competition.sponsors.all().order_by("name")
        return self.render(
            {
                "success": True,
                "sponsors": self.serialize_many(sponsors),
            }
        )


class CompetitionResultsView(ApiView):
    def serialize(self, obj):
        return {
            "id": obj.id,
            # FIXME: Fix serialization.
            "team": obj.team,
            # FIXME: Fix serialization.
            "entry": obj.entry,
            # FIXME: Fix serialization.
            "prizes": obj.prizes,
            "code_quality_score": obj.code_quality_score,
            "design_score": obj.design_score,
            "idea_score": obj.idea_score,
            "execution_score": obj.execution_score,
            "created": obj.created,
            "updated": obj.updated,
        }

    def get(self, request, pk):
        competition = Competition.objects.active().filter(pk=pk)
        results = competition.results.all().order_by("name")
        return self.render(
            {
                "success": True,
                "results": self.serialize_many(results),
            }
        )


class CompetitionResultDetailView(ApiView):
    def serialize(self, obj):
        return {
            "id": obj.id,
            # FIXME: Fix serialization.
            "team": obj.team,
            # FIXME: Fix serialization.
            "entry": obj.entry,
            # FIXME: Fix serialization.
            "prizes": obj.prizes,
            "code_quality_score": obj.code_quality_score,
            "design_score": obj.design_score,
            "idea_score": obj.idea_score,
            "execution_score": obj.execution_score,
            "created": obj.created,
            "updated": obj.updated,
        }

    def get(self, request, pk, result_pk):
        competition = Competition.objects.active().filter(pk=pk)
        result = competition.results.filter(pk=result_pk).order_by("name")
        return self.render(
            {
                "success": True,
                "result": self.serialize(result),
            }
        )
