django-with-asserts - Test HTML with Context Managers
=====================================================

.. image:: https://api.travis-ci.org/johnpaulett/django-with-asserts.png

Make your Django HTML tests more explicit and concise.

Turn this::

    self.assertContains(
        resp,
        '<input id="id_email" type="text" name="email" maxlength="75" value="bob@example.com>',
        html=True
    )

Into this::

    with self.assertHTML(resp, 'input[name="email"]') as (elem,):
        self.assertEqual(elem.value, 'bob@example.com')

Or this (useful outside of TestCase subclasses, e.g. py.test):
    with assert_html(resp, 'input[name="email"]') as (elem,):
        self.assertEqual(elem.value, 'bob@example.com')  

Links
------

 * Documentation: https://django-with-asserts.readthedocs.org
 * Code: https://github.com/johnpaulett/django-with-asserts


