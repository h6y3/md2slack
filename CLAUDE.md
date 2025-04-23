# Project Overview

A Python script that converts Markdown into Slack Markdown.

## Implementation Suggestion

- Leverage the Python library markdown_to_mrkdwn to write a shell script that converts markdown to markdown.
- Script should follow normal shellscript conventions in terms of arguments it accepts and error checking for arguments.
- Make reasonable decisions about output file.
- Support clipboard operations for easy copying and pasting with pyperclip library.

## Key Features

- Convert from file, stdin, or clipboard input
- Output to file, stdout, or clipboard
- Cross-platform clipboard support using pyperclip
- Graceful fallback when clipboard libraries aren't available
- Espanso integration for text expansion workflow

## Espanso Integration

The project includes an espanso configuration file (`md2slack.yml`) that enables quick text expansion for Markdown conversion:

- `:md2slack` - Converts clipboard contents to Slack format and puts result back in clipboard
- `:md2s` - Converts selected text to Slack format and replaces it inline
- `:md2c` - Converts selected text to Slack format and copies to clipboard without replacing

