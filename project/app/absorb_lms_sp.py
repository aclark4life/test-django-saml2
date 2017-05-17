from onelogin.saml2 import utils
import idptest.saml2idp.base
import idptest.saml2idp.exceptions
import idptest.saml2idp.xml_render

saml2_utils = utils.OneLogin_Saml2_Utils()

class Processor(idptest.saml2idp.base.Processor):
    """
    Absorb LMS Response Handler Processor for testing against django-saml2-sp.
    """
    def _format_assertion(self):
        self._assertion_xml = idptest.saml2idp.xml_render.get_assertion_absorblms_xml(self._assertion_params, signed=True)

    def _decode_request(self):
        """
        Decodes _request_xml from _saml_request. Override base class to use python-saml's decode_base64_and_inflate.
        """
        self._request_xml = saml2_utils.decode_base64_and_inflate(self._saml_request)

    def _determine_audience(self):
        """
        """


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
