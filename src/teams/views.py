from utils.api_tools import ApiView


class TeamsView(ApiView):
    def get(self, request):
        return self.render({})


class TeamDetailView(ApiView):
    def get(self, request):
        return self.render({})


class TeamMembersView(ApiView):
    def get(self, request):
        return self.render({})


class TeamMemberDetailView(ApiView):
    def get(self, request):
        return self.render({})


class TeamInvitesView(ApiView):
    def get(self, request):
        return self.render({})


class TeamInviteDetailView(ApiView):
    def get(self, request):
        return self.render({})
