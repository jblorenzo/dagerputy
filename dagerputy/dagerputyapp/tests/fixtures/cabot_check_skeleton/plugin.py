from dagerputy.dagerputyapp.models import StatusCheck
from dagerputy.dagerputyapp.views import CheckCreateView
from dagerputy.dagerputyapp.views import CheckUpdateView
from dagerputy.dagerputyapp.views import StatusCheckForm
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

class SkeletonStatusCheck(StatusCheck):
    edit_url_name = 'update-skeleton-check'
    duplicate_url_name = 'duplicate-skeleton-check'

    check_name = 'skeleton'

class SkeletonStatusCheckForm(StatusCheckForm):
    class Meta:
        model = SkeletonStatusCheck
        fields = ('name',)

class SkeletonCheckCreateView(CheckCreateView):
    model = StatusCheck
    form_class = SkeletonStatusCheckForm

class SkeletonCheckUpdateView(CheckUpdateView):
    model = StatusCheck
    form_class = SkeletonStatusCheckForm

def duplicate_check(request, pk):
    return HttpResponseRedirect(reverse('update-skeleton-check', kwargs={'pk': 25}))
