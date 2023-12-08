from django.contrib.auth.decorators import login_required

from microapi import ApiView
from microapi import http

from .models import (
    Team,
    # TeamMember,
)


def serialize_comp(comp):
    return {
        "id": comp.pk,
        "name": comp.name,
        "slug": comp.slug,
    }


def serialize_user(user):
    return {
        "id": user.pk,
        "username": user.username,
        "email": user.email,
        "first_name": user.first_name,
        "last_name": user.last_name,
    }


def serialize_team_member(serializer, member):
    member_data = serializer.to_dict(member, exclude=["is_deleted"])
    member_data["user"] = serialize_user(member.user)
    member_data["competitions"] = []

    for comp in member.competitions.all():
        member_data["competitions"].append(serialize_comp(comp))

    return member_data


def serialize_team(serializer, team):
    data = serializer.to_dict(team, exclude=["is_deleted"])
    data["owner"] = serialize_user(team.owner)
    data["members"] = []

    for member in team.members.all():
        data["members"].append(serialize_team_member(serializer, member))

    return data


class TeamsView(ApiView):
    def serialize(self, obj):
        return serialize_team(self.serializer, obj)

    def get(self, request):
        teams = Team.objects.active().order_by("-created")
        return self.render(
            {
                "success": True,
                "teams": self.serialize_many(teams),
            }
        )

    @login_required
    def post(self, request):
        data = self.read_json(request)

        # TODO: Needs validation/uniqueness here.

        team = Team.objects.create(
            name=data["name"],
            owner=request.user,
        )

        return self.render(
            {
                "success": True,
                "team": self.serialize(team),
            },
            status_code=http.CREATED,
        )


class TeamDetailView(ApiView):
    def serialize(self, obj):
        return serialize_team(self.serializer, obj)

    def get(self, request, pk):
        team = Team.objects.active().get(pk=pk)
        return self.render(
            {
                "success": True,
                "team": self.serialize(team),
            }
        )

    @login_required
    def put(self, request, pk):
        return self.render({}, status_code=http.ACCEPTED)

    @login_required
    def delete(self, request, pk):
        return self.render({}, status_code=http.NO_CONTENT)


class TeamMembersView(ApiView):
    def get(self, request, pk):
        team = Team.objects.active().get(pk=pk)
        members = team.members.all().active()
        return self.render(
            {
                "success": True,
                "team_members": [
                    serialize_team_member(self.serializer, member) for member in members
                ],
            }
        )

    @login_required
    def post(self, request, pk):
        return self.render({}, status_code=http.CREATED)


class TeamMemberDetailView(ApiView):
    def get(self, request, pk, member_pk):
        team = Team.objects.active().get(pk=pk)
        member = team.members.get(pk=member_pk)
        return self.render(
            {
                "success": True,
                "team_member": serialize_team_member(self.serializer, member),
            }
        )

    @login_required
    def put(self, request, pk):
        return self.render({}, status_code=http.ACCEPTED)

    @login_required
    def delete(self, request, pk):
        return self.render({}, status_code=http.NO_CONTENT)


class TeamInvitesView(ApiView):
    @login_required
    def get(self, request):
        return self.render({})

    @login_required
    def post(self, request, pk):
        return self.render({}, status_code=http.CREATED)


class TeamInviteDetailView(ApiView):
    @login_required
    def get(self, request):
        return self.render({})

    @login_required
    def post(self, request, pk):
        return self.render({}, status_code=http.CREATED)
