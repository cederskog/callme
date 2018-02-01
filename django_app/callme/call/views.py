from django.shortcuts import render
from .models import CallRequest

from django.http import HttpResponseRedirect
from django.views.generic import View

from .forms import CallRequest as CallRequestForm
from .models import CallRequest as CallRequestModel


class CallRequest(View):
    template_name = 'index.html'

    def get(self, request):
        callRequestList = []
        formCallRequest = CallRequestForm()
        callRequests = CallRequestModel.objects.all()[:50]

        for callRequest in callRequests:
            callRequestList.append({'name': callRequest.your_name, 'phone': callRequest.your_phone_number, 'status': callRequest.call_status, 'create_at': callRequest.created_at})

        return render(request, self.template_name, {
            'title': 'Call Request List',
            'callRequestList': callRequestList,
            'formCallRequest': formCallRequest,
        })

    def post(self, request):
        formCallRequest = CallRequestForm(request.POST)
        if formCallRequest.is_valid():
            formCallRequest.save()
            return HttpResponseRedirect('/call/')
