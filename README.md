# Log Analyzer CLI Tool

A simple command-line tool to analyze Linux log files and extract useful insights.

## Features

* Detects errors and warnings
* Displays summary statistics
* Shows most frequent log messages
* Works with large log files

## Tech Stack

* Python
* CLI (argparse)
* File handling

## Usage

Run the tool:

```bash
python analyzer.py sample.log
```

Optional: show top N frequent messages

```bash
python analyzer.py sample.log --top 3
```

## Example Output

* Total log lines
* Error count
* Warning count
* Frequent messages

## Learning Outcomes

* Log parsing
* CLI tool development
* Debugging workflows
