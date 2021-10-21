from django.views import generic
from django.http import HttpResponse
from backfill.models import Backfill


class BackfillView(generic.ListView):
    def get(self, request, *args, **kwargs):
        Backfill.populate()
        return HttpResponse('Backfill of data done for articles!')
