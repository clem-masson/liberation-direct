""" Basic tests for the parser. """

from liberation_direct import LiberationDirect


def test_can_parse_live():
    """ Verifies that the parser returns something. """

    elements = LiberationDirect().parse_live()

    assert elements is not None
    for e in elements:
        assert e.title_text is not None


def test_can_find_news_summary():
    """ Verifies that the parser can find and convert the latest news summary. """

    summary = LiberationDirect().get_news_summary_markdown()

    assert summary is not None
    assert summary.startswith("###")
