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

    def can_handle(self, request):
        """
        Returns true if this processor can handle this request. XXX Don't need to override this method, just need a convenient place to debug.
        """
        self._reset(request)
        # Read the request.
        try:
            self._extract_saml_request()
            self._decode_request()
            self._parse_request()
        except Exception, e:
            msg = 'Exception while reading request: %s' % e
            self._logger.debug(msg)
            raise idptest.saml2idp.exceptions.CannotHandleAssertion(msg)

        self._validate_request()
        return True

    def _decode_request(self):
        """
        Decodes _request_xml from _saml_request. Override base to use python-saml utils from OneLogin.
        """
        # self._request_xml = saml2_utils.decode_base64_and_inflate(self._saml_request)
        self._request_xml = """
<samlp:AuthnRequest ID="_802c81b9-f6eb-47d5-adf3-4a8f3b12d11f"
                    Version="2.0"
                    IssueInstant="2017-05-14T17:12:43.757Z"
                    ForceAuthn="false"
                    IsPassive="false"
                    ProtocolBinding="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST"
                    AssertionConsumerServiceURL="https://aclark.myabsorb.com/account/saml"
                    xmlns:samlp="urn:oasis:names:tc:SAML:2.0:protocol"
                    >
    <saml:Issuer xmlns:saml="urn:oasis:names:tc:SAML:2.0:assertion">https://aclark.myabsorb.com</saml:Issuer>
    <samlp:NameIDPolicy SPNameQualifier="Id"
                        AllowCreate="true"
                        />
</samlp:AuthnRequest>
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
