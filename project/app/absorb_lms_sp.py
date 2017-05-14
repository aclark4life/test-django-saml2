import idptest.saml2idp.base
import idptest.saml2idp.xml_render

class Processor(idptest.saml2idp.base.Processor):
    """
    Absorb LMS Response Handler Processor for testing against django-saml2-sp.
    """
    def _format_assertion(self):
        self._assertion_xml = idptest.saml2idp.xml_render.get_assertion_absorblms_xml(self._assertion_params, signed=True)

    def can_handle(self, request):
        return True


class AttributeProcessor(idptest.saml2idp.base.Processor):
    """
    Absorb LMS Response Handler Processor for testing against django-saml2-sp;
    Adds SAML attributes to the assertion.
    """
    def _format_assertion(self):
        self._assertion_params['ATTRIBUTES'] = {
            'foo': 'bar',
        }
        self._assertion_xml = idptest.saml2idp.xml_render.get_assertion_absorblms_xml(self._assertion_params, signed=True)
