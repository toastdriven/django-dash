from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify

from microapi import ApiView
from microapi import http

from .models import (
    Team,
    # TeamMember,
)


User = get_user_model()


def serialize_comp(comp):
    """
    A light serialization of Competition for deep relations.

    Just the unique data, for further lookups if needed.

    Args:
        comp (Competition): The competition to serialize.

    Returns:
        dict: The serialized competition data.
    """
    return {
        "id": comp.pk,
        "name": comp.name,
        "slug": comp.slug,
    }


def serialize_user(user):
    """
    A light serialization of User for deep relations.

    Args:
        user (User): The user to serialize.

    Returns:
        dict: The serialized user data.
    """
    return {
        "id": user.pk,
        "username": user.username,
        "email": user.email,
        "first_name": user.first_name,
        "last_name": user.last_name,
    }


def serialize_team_member(serializer, member):
    """
    A serilization of TeamMember.

    Args:
        serializer (ModelSerializer): The serializer to use.
        member (TeamMember): The team member to serialize.

    Returns:
        dict: The serialized team member data.
    """
    member_data = serializer.to_dict(member, exclude=["is_deleted"])
    member_data["user"] = serialize_user(member.user)
    member_data["competitions"] = []

    for comp in member.competitions.all():
        member_data["competitions"].append(serialize_comp(comp))

    return member_data


def serialize_team(serializer, team):
    """
    A serilization of Team.

    Args:
        serializer (ModelSerializer): The serializer to use.
        team (Team): The team to serialize.

    Returns:
        dict: The serialized team data.
    """
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

        if not data.get("name", ""):
            return self.render_error(
                "No team name provided.", status_code=http.BAD_REQUEST
            )

        if Team.objects.is_name_taken(data["name"]):
            return self.render_error(
                "Team name is already taken.", status_code=http.BAD_REQUEST
            )

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
        data = self.read_json(request)

        try:
            team = Team.objects.get(pk=pk)
        except Team.DoesNotExist:
            return self.render_error("No team found.", status_code=http.NOT_FOUND)

        # They must currently own the team to make changes.
        if team.owner != request.user:
            return self.render_error("No team found.", status_code=http.NOT_FOUND)

        # If they're supplying a new name, it must not be blank and must not be
        # already taken.
        if data.get("name") and data.get("name") != team.name:
            if Team.objects.is_name_taken(data["name"]):
                return self.render_error(
                    "Name is already taken.", status_code=http.BAD_REQUEST
                )

            team.name = data["name"]
            team.slug = slugify(data["name"])

        if data.get("owner"):
            try:
                new_owner = User.objects.get(username=data["username"])
            except User.DoesNotExist:
                return self.render_error(
                    "New owner not found.", status_code=http.BAD_REQUEST
                )

            team.owner = new_owner

        team.save()
        return self.render(
            {
                "success": True,
                "team": self.serialize(team),
            },
            status_code=http.ACCEPTED,
        )

    @login_required
    def delete(self, request, pk):
        try:
            team = Team.objects.filter(owner=request.user).get(pk=pk)
        except Team.DoesNotExist:
            return self.render_error("No team found.", status_code=http.NOT_FOUND)

        team.delete()
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
        data = self.read_json(request)

        if not data.get("name", ""):
            return self.render_error(
                "No team name provided.", status_code=http.BAD_REQUEST
            )

        if Team.objects.filter(slug=slugify(data["name"])).exists():
            return self.render_error(
                "Team name is already taken.", status_code=http.BAD_REQUEST
            )

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
