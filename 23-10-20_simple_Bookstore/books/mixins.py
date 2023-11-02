from django.http import HttpResponseRedirect #, HttpResponseForbidden  # <- wenn Verbieten
from django.urls import reverse

class UserRequiredMixin:
    """Mixin to ensure the user is authenticated."""

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('login'))
            # du kannst auch verbieten einfach ohne Redirect:
            # return HttpResponseForbidden('Du hast keinen Zugriff als Normalo')   
        return super().dispatch(request, *args, **kwargs)
        