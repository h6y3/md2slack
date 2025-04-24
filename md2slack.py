#!/usr/bin/env python3

import sys
import os
import argparse
from markdown_to_mrkdwn import SlackMarkdownConverter

try:
    import pyperclip
    CLIPBOARD_SUPPORTED = True
except ImportError:
    CLIPBOARD_SUPPORTED = False

def process_input(input_str):
    """Convert markdown to mrkdwn format"""
    converter = SlackMarkdownConverter()
    
    # Register custom plugin to fix trailing spaces in bold text
    # This runs after the standard conversion with high priority (lower number)
    converter.register_regex_plugin(
        name="fix_bold_spaces", 
        pattern=r"\*([^*\n]+?)[ ]+\*", 
        replacement=r"*\1*", 
        priority=10
    )
    
    return converter.convert(input_str)

def main():
    parser = argparse.ArgumentParser(description='Convert Markdown to Slack Markdown (mrkdwn)')
    parser.add_argument('file', nargs='?', help='Input markdown file (optional, stdin used if not provided)')
    parser.add_argument('-o', '--output', help='Output file (stdout if not specified)')
    
    if CLIPBOARD_SUPPORTED:
        parser.add_argument('-c', '--clipboard', action='store_true', help='Use clipboard for input')
        parser.add_argument('-C', '--copy', action='store_true', help='Copy output to clipboard')
    
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
            sys.stderr.write("No input file specified and no stdin input detected.\n")
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