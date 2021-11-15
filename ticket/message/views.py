from django.shortcuts import render
from django.views import View
from django.core.mail import send_mail
from django.http import HttpResponseRedirect, HttpResponse

from rest_framework.response import Response
from rest_framework.views import APIView

from message.forms import CredentialForm
from message.models import Credentials
from message.serializers import CredentialSerializer


class GetCredentialInfoView(APIView):
    def get(self, request):
        queryset = Credentials.objects.all()
        serializer_for_queryset = CredentialSerializer(
            instance=queryset,
            many=True
        )
        return Response(serializer_for_queryset.data)

class HomeView(View):
    form = CredentialForm
    template = 'home.html'

    def get(self, request, *args, **kwargs):
        form = self.form()
        return render(request, self.template, {'form': form})

    def post(self, request):
        if request.method == 'POST':
            form = CredentialForm(request.POST)
            if form.is_valid():
                new_form = form.save(commit=False)
                name = form.cleaned_data['name']
                recipient = form.cleaned_data['email']


                send_mail(
                    'Request successfully saved',
                    f'Hello dear {name}, thank you for reporting us the problem\n'
                    f'We will come back to you with the solution shortly\n',
                    'deniro094@gmail.com',
                    [recipient],
                    fail_silently=False
                )

                new_form.save()


                return HttpResponseRedirect('/success/')




class Success(View):

    def get(self, request):
        return HttpResponse('Thank you for making us better!')


