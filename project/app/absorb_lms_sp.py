import base
import exceptions
import xml_render

class Processor(base.Processor):
    """
    Absorb LMS Response Handler Processor for testing against django-saml2-sp.
    """
    def _format_assertion(self):
        self._assertion_xml = xml_render.get_assertion_absorb_xml(self._assertion_params, signed=True)


class AttributeProcessor(base.Processor):
    """
    Absorb LMS Response Handler Processor for testing against django-saml2-sp;
    Adds SAML attributes to the assertion.
    """
    def _format_assertion(self):
        self._assertion_params['ATTRIBUTES'] = {
            'foo': 'bar',
        }
        self._assertion_xml = xml_render.get_assertion_absorb_xml(self._assertion_params, signed=True)
