# txttojson

This project reads text from a `.docx` file and converts it into a JSON file in a specific format. This tool is designed to process documents containing word pairs (key: value). Users can easily convert their text-based data into JSON format using this project, making it usable in various applications.

## Example

### Input `.docx` Format

The `.docx` file should have text in the following format:

```
word1: definition1
word2: definition2
word3: definition3
...
```

### Example Input

```
happy: feeling or showing pleasure or contentment
sad: feeling or showing sorrow; unhappy
angry: feeling or showing strong annoyance, displeasure, or hostility
```

### Output JSON

After running the script, the output `file.json` file will look like this:

```json
{
    "happy": "feeling or showing pleasure or contentment",
    "sad": "feeling or showing sorrow; unhappy",
    "angry": "feeling or showing strong annoyance, displeasure, or hostility"
}
```

## Code Explanation

- Opens the `.docx` file and reads all the text.
- Processes the text according to a specific format and extracts each pair as a word.
- Converts these words into a dictionary structure and writes them to a JSON file.

## Installation

Follow these steps to install the necessary dependencies:

1. Clone this project:
    ```sh
    git clone https://github.com/username/txttojson.git
    cd txttojson
    ```

2. Install the required Python packages:
    ```sh
    pip install python-docx
    ```

## Usage

1. Run the `txttojson.py` file:
    ```sh
    python txttojson.py
    ```

2. This command will read the specified `.docx` file and convert it into a `file.json` file.