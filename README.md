# md2slack

A lightweight, command-line utility for converting standard Markdown to Slack-compatible Markdown (mrkdwn) format.

## Overview

`md2slack` provides a seamless way to prepare your Markdown content for Slack's specific markdown implementation, eliminating the frustration of manually adjusting formatting when copying content to Slack.

This tool is built on top of the [`markdown-to-mrkdwn`](https://pypi.org/project/markdown-to-mrkdwn/) Python library, providing a convenient command-line interface with additional features like clipboard integration.

## Features

- **Multiple Input Methods**: Read from files, standard input (stdin), or system clipboard.
- **Flexible Output Options**: Write to files, standard output (stdout), or copy directly to clipboard.
- **Cross-Platform Support**: Works on macOS, Linux, and Windows.
- **Clipboard Integration**: Seamless copy-paste workflow (requires `pyperclip`).
- **Espanso Integration**: Sample configuration for text expansion shortcuts.
- **Customizable Fixes**: Includes fixes for common Slack markdown rendering issues, such as trailing spaces in bold text and removing Perplexity.ai style citations.

## Installation

You can install `md2slack` using pip:

```bash
pip install md2slack
```

This will install the command-line tool `md2slack` and its dependencies.

### For Development / From Source

If you want to contribute to development or install from the source code:

1.  Clone the repository:
    ```bash
    git clone https://github.com/user/md2slack # Replace with the actual repository URL
    cd md2slack
    ```

2.  Install in editable mode (preferably in a virtual environment):
    ```bash
    pip install -e .
    ```

## Usage

### Basic Examples

```bash
# Convert a Markdown file to a Slack-compatible text file
md2slack document.md -o slack_formatted.txt

# Pipe content through stdin/stdout
cat document.md | md2slack > slack_formatted.txt

# Copy from clipboard, convert, and copy result back to clipboard
md2slack -c -C
```

### Command-Line Options

The command-line options remain the same. You can view them with `md2slack --help`:

```
usage: md2slack [-h] [-o OUTPUT] [-c] [-C] [file]

Convert Markdown to Slack Markdown (mrkdwn)

positional arguments:
  file                  Input markdown file (optional, stdin used if not provided)

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        Output file (stdout if not specified)
  -c, --clipboard       Use clipboard for input (requires pyperclip)
  -C, --copy            Copy output to clipboard (requires pyperclip)
```

### Workflow Examples

#### Document Preparation Workflow

```bash
# Edit your document in your favorite Markdown editor
# Then convert and copy to clipboard in one step:
md2slack my_document.md -C

# Now paste directly into Slack!
```

#### Quick Clipboard Conversion

```bash
# Copy markdown text from any source
# Then run this command to convert and replace clipboard contents:
md2slack -c -C

# Paste the converted text into Slack
```

## How It Works

`md2slack` utilizes the [`markdown-to-mrkdwn`](https://pypi.org/project/markdown-to-mrkdwn/) Python library for the core conversion logic. It enhances this by:

1.  Providing a user-friendly command-line interface.
2.  Offering flexible input/output options (files, stdin/stdout, clipboard).
3.  Integrating `pyperclip` for clipboard access.
4.  Implementing custom regular expression-based fixes for common Slack formatting issues, such as:
    *   **Trailing Spaces in Bold Text**: Ensures `*text *` becomes `*text*`.
    *   **Perplexity Citation Removal**: Strips `[1][2]` style citations and footer sections commonly found in AI-generated text.

### Formatting Examples

Input Markdown | Output Slack Markdown
-------------- | --------------------
`# Heading 1` | `*Heading 1*`
`## Heading 2` | `*Heading 2*`
`*italic*` | `_italic_`
`**bold**` | `*bold*`
`` `code` `` | `` `code` ``
`* Bullet with asterisk` | `* Bullet with asterisk`
`- Bullet with dash` | `• Bullet with dash` (Unicode bullet)
`+ Bullet with plus` | `+ Bullet with plus`
`1. Numbered item` | `1. Numbered item`

## Dependencies

`md2slack` relies on the following Python packages:

- [markdown-to-mrkdwn](https://pypi.org/project/markdown-to-mrkdwn/): For the core Markdown to Slack mrkdwn conversion.
- [pyperclip](https://pypi.org/project/pyperclip/): For clipboard input/output functionality.

These will be installed automatically when you install `md2slack` via pip.

## Espanso Integration

[Espanso](https://espanso.org/) is an open-source text expander. You can use the provided `md2slack.yml.sample` for quick conversions.

### Setup

1.  [Install Espanso](https://espanso.org/install/) for your platform.
2.  Copy the `md2slack.yml.sample` file to your Espanso match directory:
    *   **macOS**: `~/Library/Application Support/espanso/match/md2slack.yml`
    *   **Linux**: `~/.config/espanso/match/md2slack.yml`
    *   **Windows**: `%APPDATA%\espanso\match\md2slack.yml`

    You can copy it from the cloned repository or download it directly from GitHub.

3.  **Configuration**:
    *   If you installed `md2slack` using `pip` and the `md2slack` command is in your system's PATH, the sample configuration should work out of the box. The `INSTALL_DIR` and `VENV_ACTIVATE` variables are no longer present in the sample file.
    *   If `md2slack` is not in your PATH (e.g., you installed it in a specific virtual environment that isn't globally accessible via the `md2slack` command), you'll need to modify the `cmd` lines in `md2slack.yml` to use the full path to the `md2slack` executable. For example:
        ```yaml
        # Example of a modified cmd for a specific venv path
        # cmd: "/path/to/your/venv/bin/md2slack -c -C && echo 'Markdown converted'"
        ```
4.  Restart Espanso for the changes to take effect.

### Available Shortcuts (from sample)

-   `:md2slack`: Reads from clipboard, converts, and copies back to clipboard.
-   `:mdinsert`: Opens a form to input text, converts, and inserts the result.
-   `:mdcopy`: Opens a form to input text, converts, and copies the result to the clipboard.

## Contributing

Contributions are welcome! If you have ideas for improvements, please open an issue or submit a pull request. Key areas for contribution include:

-   Enhanced error handling
-   Additional conversion rules or options
-   Performance improvements
-   Broader test coverage
-   Documentation updates

When contributing code, please ensure it aligns with the project's style and that any new functionality is appropriately tested. (Note: Specific linting/testing commands like `flake8` or `pytest` would depend on project setup if development dependencies are added, e.g., in a `dev-requirements.txt` or `pyproject.toml [dev-dependencies]`).

## License

## License

[MIT License](LICENSE)