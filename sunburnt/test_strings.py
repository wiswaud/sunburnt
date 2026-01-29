import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from strings import RawString


def test_string_escape():
    """ Ensure that string characters are escaped correctly for Solr queries.
    """
    test_str = u'+-&|!(){}[]^"~*?: \t\v\\/'
    escaped = RawString(test_str).escape_for_lqs_term()
    assert escaped == u'\\+\\-\\&\\|\\!\\(\\)\\{\\}\\[\\]\\^\\"\\~\\*\\?\\:\\ \\\t\\\x0b\\\\\\/'


