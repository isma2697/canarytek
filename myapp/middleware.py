from django_saml2_auth.views import _get_saml_auth

class LogSamlAttributesMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        # Verifica si el usuario está autenticado y si se utilizó la autenticación SAML
        if request.user.is_authenticated and hasattr(request.session, 'samlSessionIndex'):
            saml_auth = _get_saml_auth(request)
            saml_attributes = saml_auth.get_attributes()
            
            # Imprime los atributos SAML en la consola:
            print("Atributos SAML recibidos:", saml_attributes)

            # Opcional: registra los atributos SAML en el archivo de registro de Django:
            import logging
            logger = logging.getLogger(__name__)
            logger.info(f"Atributos SAML recibidos: {saml_attributes}")

        return response
