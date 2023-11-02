from django.contrib.auth.models import User
from django.http import HttpResponseNotAllowed, HttpResponse, HttpResponseRedirect
from django.urls import reverse, resolve

class SpecialUserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # one-time configuratoin and initialization


    def __call__(self, request):
        # code to be executed for each request before
        # the view (and the later middleware) are called

        user_id = request.session.get('_auth_user_id')
        if user_id:
            user = User.objects.get(pk=user_id)
            return HttpResponse(f"You are user {user}!")    # wenn du dich im browser einloggst, wird "You are user xxx!" ausgegeben

        response = self.get_response(request)

        # print(response)
        # response.write('Hello World!')

        return response
    
class ProtectSpecificRoutesMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        # List of protected URL names
        protected_url_names = [
            'home',
            'post_new',
            'post_edit',
            'post_delete',
        ]

        # resolve the current path to its URL name
        try:
            current_url_name = resolve(request.path_info).url_name
        except:
            current_url_name = None

        if current_url_name in protected_url_names and not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('login'))
        
        return self.get_response(request)


class LanguageMiddleware:
    # der Konstruktor wird automatisch aufgerufen wenn instanz des objektes erstellt wird und nitialisiert die class-eigenschaften (attribute)
    # in diesem wir machen das get_respose für die __call__ funktion verfügbar, um durch das get_response den request durch die middleware-kette zu leiten 
    def __init__(self, get_response):
        self.get_response = get_response
    
    # mit __call__ mache ich die Class aufrufbar wie eine funktion. sobald also ein request durch die middleware geschickt wird, wird die class aufgerufen und dann diese methode
    def __call__(self, request):
        # wir holen uns über die HEADER-infos die vom User bevorzugte Sprache heraus und speichern diese in language, um den request in der für den user geeigneten sprache auszugeben
        # gibt es keine info darüber, wird deutsch als custom definiert
        language = request.headers.get('Accept-Language', 'de')
        
        # nun spreichern wir die oben extrahierte sprachee in der LANGUAGE_CODE-variable des requests, 
        # so könnten wir im View auf diese variable zugreigfen und je nach sprache dann das passende template ausgeben lassen
        request.LANGUAGE_CODE = language
        # print(language) 
        
        # nun schicken wir den request weiter in der middlewareschleife
        response = self.get_response(request)
        return response


