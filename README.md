# md2slack

A lightweight, command-line utility for converting standard Markdown to Slack-compatible Markdown (mrkdwn) format.

## Overview

`md2slack` provides a seamless way to prepare your Markdown content for Slack's specific markdown implementation, eliminating the frustration of manually adjusting formatting when copying content to Slack.

This tool is built on top of the [`markdown-to-mrkdwn`](https://pypi.org/project/markdown-to-mrkdwn/) Python library, providing a convenient command-line interface with additional features like clipboard integration.

## Features

- **Multiple Input Methods**: Read from files, standard input (stdin), or system clipboard
- **Flexible Output Options**: Write to files, standard output (stdout), or copy directly to clipboard
- **Cross-Platform Support**: Works on macOS, Linux, and Windows
- **Clipboard Integration**: Seamless copy-paste workflow using pyperclip
- **Graceful Degradation**: Falls back to file/stream operations when clipboard isn't available
- **Error Handling**: Comprehensive error messages and validation
- **Espanso Integration**: Built-in text expansion shortcuts for efficient workflows

## Installation

### Prerequisites

- Python 3.6 or higher
- pip (Python package manager)

### Setup

1. Clone this repository or download the source code:
   ```bash
   git clone https://github.com/username/md2slack.git
   cd md2slack
   ```

2. Set up a virtual environment and install dependencies:
   ```bash
   python3 -m venv md2slack_venv
   source md2slack_venv/bin/activate  # On Windows: md2slack_venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Make the shell script executable:
   ```bash
   chmod +x md2slack
   ```

## Usage

### Basic Examples

```bash
# Convert a Markdown file to a Slack-compatible text file
./md2slack document.md -o slack_formatted.txt

# Pipe content through stdin/stdout
cat document.md | ./md2slack > slack_formatted.txt

# Copy from clipboard, convert, and copy result back to clipboard
./md2slack -c -C
```

### Command-Line Options

```
usage: md2slack [-h] [-o OUTPUT] [-c] [-C] [file]

Convert Markdown to Slack Markdown (mrkdwn)

positional arguments:
  file                  Input markdown file (optional, stdin used if not provided)

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        Output file (stdout if not specified)
  -c, --clipboard       Use clipboard for input
  -C, --copy            Copy output to clipboard
```

### Workflow Examples

#### Document Preparation Workflow

```bash
# Edit your document in your favorite Markdown editor
# Then convert and copy to clipboard in one step:
./md2slack my_document.md -C

# Now paste directly into Slack!
```

#### Quick Clipboard Conversion

```bash
# Copy markdown text from any source
# Then run this command to convert and replace clipboard contents:
./md2slack -c -C

# Paste the converted text into Slack
```

## How It Works

`md2slack` is a thin wrapper around the [`markdown-to-mrkdwn`](https://pypi.org/project/markdown-to-mrkdwn/) Python library, which handles the conversion logic. The script provides:

1. A convenient command-line interface
2. Multiple input/output options (files, streams, clipboard)
3. Error handling and user feedback
4. Clipboard integration via pyperclip
5. Custom fixes for Slack markdown rendering issues

### Custom Fixes

This tool implements fixes for known issues in the underlying markdown-to-mrkdwn library:

- **Trailing Spaces in Bold Text**: Fixes rendering issues where trailing spaces in bold text (e.g., `**Bold  **` or headings with trailing spaces) cause Slack to not render formatting correctly. The tool automatically trims these spaces to ensure proper rendering.

### Formatting Examples

Input Markdown | Output Slack Markdown
-------------- | --------------------
`# Heading 1` | `*Heading 1*`
`## Heading 2` | `*Heading 2*`
`*italic*` | `_italic_`
`**bold**` | `*bold*`
```code``` | `` `code` ``
`* Bullet with asterisk` | `* Bullet with asterisk`
`- Bullet with dash` | `• Bullet with dash` (Unicode bullet)
`+ Bullet with plus` | `+ Bullet with plus`
`1. Numbered item` | `1. Numbered item`

## Dependencies

- [markdown-to-mrkdwn](https://pypi.org/project/markdown-to-mrkdwn/): Core conversion engine
- [pyperclip](https://pypi.org/project/pyperclip/): Cross-platform clipboard operations (optional)
- [Espanso](https://espanso.org/) (optional): For text expansion workflow integration

## Espanso Integration

[Espanso](https://espanso.org/) is an open-source text expander that allows you to define custom shortcuts and expand them into longer text when typed. The `md2slack.yml.sample` configuration file included in this repo provides several helpful text expansion triggers.

### Installation

1. [Install Espanso](https://espanso.org/install/) for your platform
2. Copy the sample configuration file to your Espanso match directory:
   ```bash
   # On macOS
   cp md2slack.yml.sample ~/Library/Application\ Support/espanso/match/md2slack.yml
   
   # On Linux
   cp md2slack.yml.sample ~/.config/espanso/match/md2slack.yml
   
   # On Windows
   cp md2slack.yml.sample %APPDATA%\espanso\match\md2slack.yml
   ```
3. Edit the configuration variables at the top of the file:
   ```yaml
   # ====================== CONFIGURATION VARIABLES ======================
   # Set this to the directory where md2slack is installed
   INSTALL_DIR="/path/to/md2slack"
   # Set this to the virtual environment activate path (if using a venv)
   # Leave as empty string "" if installed globally
   VENV_ACTIVATE="md2slack_venv/bin/activate"
   # ==================================================================
   ```
4. Restart Espanso for changes to take effect

### Available Shortcuts

- `:md2slack` - Converts clipboard contents to Slack format and puts the result back in clipboard
- `:mdinsert` - Opens a form to enter text, converts it to Slack format and inserts it
- `:mdcopy` - Opens a form to enter text, converts it to Slack format and copies to clipboard without replacing

## Contributing

Contributions are welcome! This is a simple tool, but there's always room for improvement in areas like:

- Better error handling
- Additional conversion options
- Performance enhancements
- Documentation improvements
- More integration options

## License

[MIT License](LICENSE)