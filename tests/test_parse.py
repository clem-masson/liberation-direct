""" Basic tests for the parser. """

from liberation_direct import LiberationDirect


def test_can_parse_live():
    """ Verifies that the parser returns something. """

    elements = LiberationDirect().parse_live()

    assert elements is not None
    for e in elements:
        assert e.html_content is not None


def test_can_find_news_summary():
    """ Verifies that the parser can find and convert the latest news summary. """

    summary = LiberationDirect().get_news_summary_markdown()

    assert summary is not None
    assert summary.startswith("###")


def test_no_summary():
    """ Verifies that the Markdown converter does not crash if there are no summaries in the live page. """

    class DummySummary(LiberationDirect):
        """ Dummy class with a fake parser that removes all the summary elements from the live page"""
        def parse_live(self):
            return [e for e in LiberationDirect().parse_live() if not e.is_summary]

    dummy_markdown = DummySummary().get_news_summary_markdown()

    assert dummy_markdown == ""
