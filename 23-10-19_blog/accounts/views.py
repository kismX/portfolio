from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

# Create your views here.

class SignUpView(CreateView):
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

    form_class = UserCreationForm


from django.http import HttpResponse
from django.views import View


class SessionKexExample(View):

    def get(self, request, *args, **kwargs):
        # wenn session kes is already set
        if request.session.session_key:
            response_text = f"welcome Back! Session key: {request.session.session_key}"
        else:
            request.session['example_data'] = 'This is some session data'
            response_text = 'Welcome!'
        response = HttpResponse(response_text)

        # hier spielen wir mit web sessions / cookies mal rum, war aber nciht im skript
        csrf_token = request.COOKIES['csrftoken']
        response.set_cookie(csrf_token)

        print(request.COOKIES)   # printed alle cookies aus
        return HttpResponse(response_text)


