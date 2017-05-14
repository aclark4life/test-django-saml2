import idptest.saml2idp.base
import idptest.saml2idp.exceptions
import idptest.saml2idp.xml_render

class Processor(idptest.saml2idp.base.Processor):
    """
    Absorb LMS Response Handler Processor for testing against django-saml2-sp.
    """
    def _format_assertion(self):
        self._assertion_xml = idptest.saml2idp.xml_render.get_assertion_absorblms_xml(self._assertion_params, signed=True)

    def can_handle(self, request):
        """
        Returns true if this processor can handle this request. XXX Don't need to override this method, just need a convenient place to debug.
        """
        self._reset(request)
        # Read the request.
        import pdb ; pdb.set_trace()
        try:
            self._extract_saml_request()
            self._decode_request()
            self._parse_request()
        except Exception, e:
            msg = 'Exception while reading request: %s' % e
            self._logger.debug(msg)
            raise exceptions.CannotHandleAssertion(msg)

        self._validate_request()
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
