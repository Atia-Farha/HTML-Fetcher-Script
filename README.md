# HTML Fetcher Script

## Overview

The HTML Fetcher Script is a Python tool that allows users to fetch and optionally save the HTML content from a specified URL. This script provides user-friendly prompts for input validation, including URL format, redirect options, and timeout settings. It handles various exceptions to ensure robustness and provides informative error messages to guide the user in case of issues.

## Features

- **URL Validation**: Ensures the entered URL starts with `http://` or `https://`.
- **Redirect Options**: Allows users to choose whether to follow HTTP redirects.
- **Timeout Configuration**: Lets users specify a timeout value for the request.
- **Error Handling**: Catches and handles various exceptions related to HTTP requests.
- **HTML Saving**: Provides an option to save the fetched HTML content to a file.

## Getting Started

### Prerequisites

- Python 3.x
- `requests` library (can be installed via `pip install requests` in the terminal)

### Installation

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/Atia-Farha/HTML-Fetcher-Script.git
   ```
2. Navigate to the directory containing the script:
   ```bash
   cd HTML-Fetcher-Script
   ```

### Usage

1. Run the script:
   ```bash
   python fetch_html.py
   ```
2. Follow the on-screen prompts:
   - Enter the website link: Provide a valid URL starting with `http://` or `https://`.
   - Do you want to allow redirects?: Specify whether to allow HTTP redirects (yes or no).
   - Set timeout value: Enter a positive integer for the request timeout in seconds (e.g. 5, 10, 12,...).
   - Save HTML content: Choose whether to save the fetched HTML content to a file.
3. If saving the file:
   - Enter a file name.
   - If the file already exists, you will be prompted to overwrite or choose a different name.
4. To fetch another URL, choose yes when prompted. To exit the script, choose no.

## Error Handling

The script includes comprehensive error handling for:
- Invalid URL
- Content decoding errors
- HTTP errors
- Connection errors
- Timeout errors
- Chunked encoding errors
- General request exceptions
