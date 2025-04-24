# md2slack

A Python script that converts Markdown to Slack-compatible Markdown.

## Commands to Run

```bash
# Convert file to stdout
./md2slack file.md

# Convert clipboard to clipboard
./md2slack --clipboard

# Convert stdin to file
cat file.md | ./md2slack -o output.md

# Run tests
pytest

# Run linting
flake8
```

## Implementation Details

- Uses markdown_to_mrkdwn library for conversion
- Supports file, stdin, or clipboard input
- Outputs to file, stdout, or clipboard
- Handles clipboard with pyperclip
- Includes graceful fallbacks

## Espanso Shortcuts

- `:md2slack` - Clipboard→Slack→Clipboard
- `:md2s` - Selection→Slack (inline replace)
- `:md2c` - Selection→Slack→Clipboard