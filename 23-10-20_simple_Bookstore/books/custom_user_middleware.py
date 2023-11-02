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