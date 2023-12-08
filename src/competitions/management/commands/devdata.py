import datetime

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.utils.timezone import make_aware

from microapi import ModelSerializer

from competitions.models import (
    Competition,
)
from entries.models import (
    Entry,
    Commit,
)

# from invites.models import (
#     Invite,
# )
# from judging.models import (
#     Judge,
#     Score,
#     Result,
# )
from sponsors.models import (
    Sponsor,
    Prize,
)
from teams.models import (
    Team,
    TeamMember,
)


User = get_user_model()


# Idea from https://www.revsys.com/tidbits/devdata-improving-developer-velocity-and-experience/
class Command(BaseCommand):
    help = "Reloads a development database with test data"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.serializer = ModelSerializer()

    def create_or_update(self, model_class, lookups, defaults=None):
        if defaults is None:
            defaults = {}

        obj, created = model_class.objects.get_or_create(
            **lookups,
            defaults=defaults,
        )

        if not created:
            self.serializer.from_dict(obj, defaults)
            obj.save()

        return obj

    def make_datetime(self, *args):
        return make_aware(datetime.datetime(*args), timezone=datetime.timezone.utc)

    def create_competition(self):
        return self.create_or_update(
            Competition,
            {
                "name": "2024",
                "slug": "2024",
            },
            {
                "signup_start_date": self.make_datetime(2024, 1, 14, 0, 0),
                "signup_end_date": self.make_datetime(2024, 1, 27, 0, 0),
                "contest_start_date": self.make_datetime(2024, 2, 14, 18, 0),
                "contest_end_date": self.make_datetime(2024, 2, 4, 18, 0),
                "judging_start_date": self.make_datetime(2024, 2, 4, 18, 0),
                "judging_end_date": self.make_datetime(2024, 2, 18, 18, 0),
            },
        )

    def create_users(self, count=5):
        users = []

        for i in range(count):
            user = self.create_or_update(
                User,
                {
                    "username": f"user_{i}",
                },
                {
                    "email": f"user_{i}@example.com",
                    "first_name": f"User {i}",
                    "last_name": "McTest",
                },
            )
            user.set_password(f"testpass_{i}")
            user.save()
            users.append(user)

        return users

    def create_team(self, owner, team_name):
        return self.create_or_update(
            Team,
            {
                "name": team_name,
            },
            {
                "owner": owner,
            },
        )

    def create_team_member(self, user, team, comps=None):
        if comps is None:
            comps = []

        member = self.create_or_update(
            TeamMember,
            {
                "team": team,
                "user": user,
            },
        )
        member.competitions.add(*comps)
        return member

    def create_sponsors(self, comp):
        sponsor_1 = self.create_or_update(
            Sponsor,
            {
                "name": "CodeThing",
            },
            {
                "url": "https://codething.com/",
                "description": "The place for code to live.",
            },
        )
        sponsor_1.competitions.add(comp)

        self.create_or_update(
            Prize,
            {
                "competition": comp,
                "sponsor": sponsor_1,
                "name": "Lifetime Membership",
            },
            {
                "place": Prize.PLACE_FIRST,
                "estimated_value": 300,
            },
        )
        self.create_or_update(
            Prize,
            {
                "competition": comp,
                "sponsor": sponsor_1,
                "name": "One Year Membership",
            },
            {
                "place": Prize.PLACE_SECOND,
                "estimated_value": 50,
            },
        )

        sponsor_2 = self.create_or_update(
            Sponsor,
            {
                "name": "Deployalot",
            },
            {
                "url": "https://deployalot.io/",
                "description": "We make production easy.",
            },
        )
        sponsor_2.competitions.add(comp)

        self.create_or_update(
            Prize,
            {
                "competition": comp,
                "sponsor": sponsor_2,
                "name": "Small Fleet",
            },
            {
                "place": Prize.PLACE_FIRST,
                "estimated_value": 100,
            },
        )

        sponsor_3 = self.create_or_update(
            Sponsor,
            {
                "name": "Consultants-R-Us",
            },
            {
                "url": "https://consultants-r.us/",
                "description": "Django consulting.",
            },
        )
        sponsor_3.competitions.add(comp)

        return [sponsor_1, sponsor_2, sponsor_3]

    def create_entry(self, comp, team, name, repository_url, members=None):
        entry = self.create_or_update(
            Entry,
            {
                "competition": comp,
                "team": team,
                "name": name,
            },
            {
                "repository_url": repository_url,
            },
        )

        if members is not None:
            entry.team_members.add(*members)

        return entry

    def create_commit(self, entry, committer, commit_id, message):
        return self.create_or_update(
            Commit,
            {
                "commit_id": commit_id,
            },
            {
                "entry": entry,
                "committer": committer,
                "email": committer.user.email,
                "message": message,
            },
        )

    def handle(self, *args, **options):
        comp = self.create_competition()

        users = self.create_users()

        team_1 = self.create_team(
            owner=users[0],
            team_name="SuperNinjas",
        )
        team_2 = self.create_team(
            owner=users[2],
            team_name="Shadjowy Django Cjabal",
        )

        team_1_member_1 = self.create_team_member(
            user=users[0],
            team=team_1,
            comps=[comp],
        )
        team_1_member_2 = self.create_team_member(
            user=users[1],
            team=team_1,
            comps=[comp],
        )
        team_2_member_1 = self.create_team_member(
            user=users[2],
            team=team_2,
            comps=[comp],
        )

        self.create_sponsors(comp)

        entry_1 = self.create_entry(
            comp=comp,
            team=team_1,
            name="Sneaky-Beaky-Like",
            repository_url="https://github.com/superninjas/sneaky",
            members=[
                team_1_member_1,
                team_1_member_2,
            ],
        )

        entry_2 = self.create_entry(
            comp=comp,
            team=team_2,
            name="Our Entry",
            repository_url="https://github.com/cjabal/dd2024entry",
            members=[
                team_2_member_1,
            ],
        )

        self.create_commit(
            entry=entry_1,
            committer=team_1_member_1,
            commit_id="e313ec12e4aeb34bac9b920596471f64c96969f0",
            message="Initial commit.",
        )
        self.create_commit(
            entry=entry_1,
            committer=team_1_member_1,
            commit_id="c5d34f79d85a8fa1d7d5d9e68a6d1a5a6aa77918",
            message="Added app & settings.",
        )
        self.create_commit(
            entry=entry_2,
            committer=team_2_member_1,
            commit_id="0ad21203c5b1adf8962ae1468485f248242bad9e",
            message="Imported project scaffolding.",
        )
        self.create_commit(
            entry=entry_1,
            committer=team_1_member_2,
            commit_id="4bf0997a66e787b2723e5346a01493763f6b97df",
            message="A bit of design work.",
        )
