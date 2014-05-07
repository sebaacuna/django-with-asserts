from .context_manager import AssertHTMLContext, HTMLNotPresent


__all__ = ['AssertHTMLMixin']


class AssertHTMLMixin(object):
    def assertHTML(self, *args, **kwargs):
        kwargs['test_case'] = self
        return AssertHTMLContext(*args, **kwargs)

    def assertNotHTML(self, *args, **kwargs):
        try:
            with self.assertHTML(*args, **kwargs) as html:
                # We found something, which is bad
                raise self.failureException(
                    'Found unexpected content: {0}'.format(html)
                )
        except HTMLNotPresent:
            # Actually this is good, the selector / element_id where not found
            # eat the assertion
            pass
