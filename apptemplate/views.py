"""
Example docstring
"""
from django.http import HttpResponse

from apptemplate import VERSION

def hello(request):
    """
    Doctring  for the hello module
    
    @param request a Django HttpRequest
    
    .. note ::
    
        hello
    
    """
    return HttpResponse('hello2')


def version(request):
    """
    Returns the application version number 
    @param request a Django HttpRequest
    """
    return HttpResponse(VERSION)


class MyPublicClass(object):
    """Lorem ipsum.

    Lorem ipsum :func:`some_other_func`.

    .. note::

       Lorem: ipsum :mod:`some_other_mod`

    """

    def __init__(self, foo, bar='baz'):
        """A really simple class.

        Args:
           foo (str): We all know what foo does.

        Kwargs:
           bar (str): Really, same as foo.

        """
        self._foo = foo
        self._bar = bar

    def get_foobar(self, foo, bar=True):
        """This gets the foobar

        >>> print get_foobar(10, 20)
        30
        >>> print get_foobar('a', 'b')
        ab

        Isn't that what you want?

        """
        return foo + bar

    def _get_baz(self, baz=None):
        """A private function to get baz.
        """
        return baz

