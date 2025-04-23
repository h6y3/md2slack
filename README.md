# md2slack

A simple tool to convert standard Markdown to Slack Markdown (mrkdwn) format.

## Installation

1. Ensure Python 3 is installed
2. Set up the virtual environment and install dependencies:
   ```
   python3 -m venv md2slack_venv
   source md2slack_venv/bin/activate
   pip install markdown-to-mrkdwn pyperclip
   ```
3. Make sure the script is executable:
   ```
   chmod +x md2slack
   ```

## Usage

### Basic Usage

```bash
# Convert a file
./md2slack input.md -o output.txt

# Using stdin/stdout
cat input.md | ./md2slack > output.txt

# Using clipboard
./md2slack -c -C  # Read from clipboard and copy result back to clipboard
```

### Options

- Input:
  - Provide a file as an argument
  - Pipe content via stdin
  - Use `-c` or `--clipboard` to read from system clipboard
- Output:
  - Use `-o` or `--output` to specify an output file
  - Let the result go to stdout (default)
  - Use `-C` or `--copy` to copy result to system clipboard

## Examples

```bash
# Convert from file to file
./md2slack document.md -o slack_document.txt

# Convert from stdin to stdout
echo "# Hello **world**" | ./md2slack

# Convert from clipboard and copy result back to clipboard
./md2slack -c -C

# Convert from file and copy result to clipboard (also prints to stdout)
./md2slack input.md -C

# Convert from clipboard to file
./md2slack -c -o output.txt
```

## Requirements

- Python 3
- markdown-to-mrkdwn
- pyperclip (for clipboard support)