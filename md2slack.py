#!/usr/bin/env python3

import sys
import argparse
import re
from markdown_to_mrkdwn import SlackMarkdownConverter

try:
    import pyperclip
    CLIPBOARD_SUPPORTED = True
except ImportError:
    CLIPBOARD_SUPPORTED = False


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


def process_input(input_str):
    """Convert markdown to mrkdwn format"""
    converter = SlackMarkdownConverter()
    # Register all custom fix plugins
    register_fix_bold_trailing_spaces(converter)
    register_remove_perplexity_citations(converter)
    return converter.convert(input_str)


def main():
    parser = argparse.ArgumentParser(
        description='Convert Markdown to Slack Markdown (mrkdwn)'
    )
    parser.add_argument(
        'file', nargs='?',
        help='Input markdown file (optional, stdin used if not provided)'
    )
    parser.add_argument(
        '-o', '--output',
        help='Output file (stdout if not specified)'
    )

    if CLIPBOARD_SUPPORTED:
        parser.add_argument(
            '-c', '--clipboard', action='store_true',
            help='Use clipboard for input'
        )
        parser.add_argument(
            '-C', '--copy', action='store_true',
            help='Copy output to clipboard'
        )

    args = parser.parse_args()

    # Handle input
    if CLIPBOARD_SUPPORTED and args.clipboard:
        try:
            input_text = pyperclip.paste()
            if not input_text:
                sys.stderr.write("Error: Clipboard is empty\n")
                sys.exit(1)
        except Exception as e:
            sys.stderr.write(f"Error reading from clipboard: {e}\n")
            sys.exit(1)
    elif args.file:
        try:
            with open(args.file, 'r') as f:
                input_text = f.read()
        except Exception as e:
            sys.stderr.write(f"Error reading file {args.file}: {e}\n")
            sys.exit(1)
    else:
        # Check if stdin has data
        if sys.stdin.isatty():
            sys.stderr.write(
                "No input file specified and no stdin input detected.\n"
            )
            parser.print_help()
            sys.exit(1)
        input_text = sys.stdin.read()

    # Process the markdown
    output_text = process_input(input_text)

    # Handle output
    if CLIPBOARD_SUPPORTED and args.copy:
        try:
            pyperclip.copy(output_text)
            sys.stderr.write("Output copied to clipboard\n")
        except Exception as e:
            sys.stderr.write(f"Error copying to clipboard: {e}\n")
            sys.exit(1)

    if args.output:
        try:
            with open(args.output, 'w') as f:
                f.write(output_text)
        except Exception as e:
            sys.stderr.write(f"Error writing to file {args.output}: {e}\n")
            sys.exit(1)
    elif not (CLIPBOARD_SUPPORTED and args.copy and not args.output):
        # Only write to stdout if we're not only copying to clipboard
        sys.stdout.write(output_text)


if __name__ == "__main__":
    main()
