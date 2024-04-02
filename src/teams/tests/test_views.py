from django.contrib.auth import get_user_model

from microapi.tests import ApiTestCase

# from competitions.models import Competition

# from ..models import (
#     Team,
#     TeamMember,
# )
from ..views import (
    TeamsView,
    #     TeamDetailView,
    #     TeamMembersView,
    #     TeamMemberDetailView,
    #     TeamInvitesView,
    #     TeamInviteDetailView,
)


User = get_user_model()


class TeamsViewTestCase(ApiTestCase):
    def test_get(self):
        req = self.create_request(
            "/api/v1/posts/",
        )
        resp = self.make_request(TeamsView, req)
        self.assertOK(resp)


class TeamDetailViewTestCase(ApiTestCase):
    def test_get(self):
        pass


class TeamMembersViewTestCase(ApiTestCase):
    def test_get(self):
        pass


class TeamMemberDetailViewTestCase(ApiTestCase):
    def test_get(self):
        pass


class TeamInvitesViewTestCase(ApiTestCase):
    def test_get(self):
        pass


class TeamInviteDetailViewTestCase(ApiTestCase):
    def test_get(self):
        pass
