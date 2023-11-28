from utils.api_tools import ApiView


class CompetitionsView(ApiView):
    def get(self, request):
        return self.render({})


class LatestCompetitionView(ApiView):
    def get(self, request):
        return self.render({})


class CompetitionDetailView(ApiView):
    def get(self, request):
        return self.render({})


class CompetitionCommitsView(ApiView):
    def get(self, request):
        return self.render({})


class CompetitionEntriesView(ApiView):
    def get(self, request):
        return self.render({})


class CompetitionEntryDetailView(ApiView):
    def get(self, request):
        return self.render({})


class CompetitionSponsorsView(ApiView):
    def get(self, request):
        return self.render({})


class CompetitionResultsView(ApiView):
    def get(self, request):
        return self.render({})


class CompetitionResultDetailView(ApiView):
    def get(self, request):
        return self.render({})
