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
- Fixes Slack rendering issues with trailing spaces in bold text

## Code Structure

- Main conversion logic in `process_input()` function
- Custom fixes registered using SlackMarkdownConverter plugins
- Multiple regex plugins can be registered for different transformations

## SlackMarkdownConverter API

```python
# Register a regex-based plugin
converter.register_regex_plugin(
    name="plugin_name",
    pattern=r"regex_pattern",
    replacement=r"replacement",
    priority=10  # Lower numbers run first
)

# Register a custom plugin for complex processing
converter.register_plugin(
    name="plugin_name",
    converter_func=custom_function,  # Takes string, returns string
    priority=50,
    scope="global"  # Options: "global", "line", "block"
)
```

## Virtual Environment

- Python dependencies in `md2slack_venv/`
- Key dependencies:
  - markdown_to_mrkdwn: `/md2slack_venv/lib/python3.13/site-packages/markdown_to_mrkdwn/`
  - pyperclip: For clipboard support

## Espanso Shortcuts

- `:md2slack` - Clipboard→Slack→Clipboard
- `:md2s` - Selection→Slack (inline replace)
- `:md2c` - Selection→Slack→Clipboard