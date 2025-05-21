import re
from markdown_to_mrkdwn import SlackMarkdownConverter

def register_fix_bold_trailing_spaces(converter):
    """
    Register a custom plugin to fix trailing spaces in bold text.
    Slack doesn't render bold text correctly when there are trailing spaces
    before the closing asterisk, i.e. "*text *" should be "*text*".
    """
    converter.register_regex_plugin(
        name="fix_bold_spaces",
        pattern=r"\*([^*\n]+?)[ ]+\*",
        replacement=r"*\1*",
        priority=10
    )


def register_remove_perplexity_citations(converter):
    """
    Register a custom plugin to remove Perplexity citations.
    This removes:
    1. Citation references like [5][2] in the text
    2. The "Citations:" section and all listed citations
    3. Reference to Perplexity at the end
    """
    # Remove inline citations like [5][2]
    converter.register_regex_plugin(
        name="remove_perplexity_inline_citations",
        pattern=r"\[\d+\](?:\[\d+\])*",
        replacement=r"",
        priority=20
    )

    # Handle multi-line content
    def strip_citations_and_footer(markdown):
        # Remove citations section
        markdown = re.sub(
            r"\n+Citations:[\s\S]*?(?=\n+---|\Z)",
            "",
            markdown
        )
        # Remove "Answer from Perplexity" line and the URL
        markdown = re.sub(
            r"\n+---\n+Answer from Perplexity:.*?(?=\n|\Z)",
            "",
            markdown
        )
        return markdown

    # Register global plugin for citations and footer removal
    converter.register_plugin(
        name="strip_citations_and_footer",
        converter_func=strip_citations_and_footer,
        priority=100,  # High priority to run after other standard conversions
        scope="global"  # Apply to the entire document
    )


def convert_markdown(input_str):
    """Convert markdown to mrkdwn format"""
    converter = SlackMarkdownConverter()
    # Register all custom fix plugins
    register_fix_bold_trailing_spaces(converter)
    register_remove_perplexity_citations(converter)
    return converter.convert(input_str)
