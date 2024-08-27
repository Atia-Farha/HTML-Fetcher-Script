# HTML Fetcher Script

## Overview

The HTML Fetcher Script is a Python script that allows users to fetch and optionally save the HTML content from a specified URL using `requests` library. This script provides user-friendly prompts for input validation, including URL format, redirect options, and timeout settings. It handles various exceptions to ensure robustness and provides informative error messages to guide the user in case of issues.

## Table of Contents

- [Project Structure](#project-structure)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Usage](#usage)
- [Error Handling](#error-handling)
- [Reporting Issues](#reporting-issues)

## Project Structure

```plaintext
HTML-Fetcher-Script/
├── src/
│   └── fetch_html.py       # Main Python script
├── .gitignore              # Ignored files
├── LICENSE                 # License file
└── README.md               # Documentation      
```

## Features

- **URL Validation**: Ensures the entered URL starts with `http://` or `https://`.
- **Redirect Options**: Allows users to choose whether to follow HTTP redirects.
- **Timeout Configuration**: Lets users specify a timeout value for the request.
- **Error Handling**: Catches and handles various exceptions related to HTTP requests.
- **HTML Saving**: Provides an option to save the fetched HTML content to a file.

## Getting Started

### Prerequisites

- Python 3 (can be download from <a href="https://www.python.org/downloads/" target="_blank">this website</a>)
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

1. Run the `fetch_html.py` file.
2. Follow the on-screen prompts:
   - **Enter the website link**: Provide a valid URL starting with `http://` or `https://` (e.g., `https://example.com`).
   - **Allow redirects:** Specify whether to allow HTTP redirects (`yes` or `no`).
   - **Set timeout value:** Enter a positive integer for the request timeout in seconds (e.g., `5`, `10`, `12`,...).
   - **Save HTML content:** Choose whether to save the fetched HTML content to a file (`yes` or `no`).
3. If saving the file:
   - Enter a file name.
   - If the file already exists, you will be prompted to overwrite or choose a different name.
4. To fetch another URL, answer `yes` when prompted. To exit the script, answer `no`.

## Error Handling

The script includes comprehensive error handling for:
- Invalid URL
- Content decoding errors
- HTTP errors
- Connection errors
- Timeout errors
- Chunked encoding errors
- General request exceptions

## Reporting Issues

If you encounter any functional issues or complaints, please let me know in the 'Issues' section. I will make every effort to fix it as quickly as possible.

## License
This script is provided for personal, non-commercial purposes. Commercial use of this software is not permitted. When using this script, credit must be given to the original author. For more details, read [LICENSE file](LICENSE).

<p align="center">Copyright © originally written by Atia Farha</p>
