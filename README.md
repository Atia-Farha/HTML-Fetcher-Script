# HTML Fetcher Script

<a href="https://github.com/Atia-Farha/HTML-Fetcher-Script" target="_blank">HTML Fetcher Script</a> is a Python script that allows users to fetch and optionally save the HTML content from a specified URL using `requests` library. This script provides user-friendly prompts for input validation including URL format, timeout value etc. and allows customization of settings like handling redirects and timeout durations. It handles various exceptions to ensure robustness and provides informative error messages to guide the user in case of issues.

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

- **Detailed Console Messages:** Guides users through every step with clear instructions and error 
- **Robust Error Handling:** Catches and handles various exceptions like invalid URLs, connection errors, timeouts, and HTTP issues.
- **URL Validation:** Ensures the entered URL starts with `http://` or `https://`.
- **Redirect Options:** Allows users to choose whether to follow HTTP redirects.
- **Timeout Configuration:** Lets users specify a timeout duration (in seconds) for the request.
- **Fetch HTML:** The script fetches the HTML content from the specified URL and displays the response headers and the HTML content. 
- **HTML Saving:** Provides an option to save the fetched HTML content to a local file and handles overwriting conflicts.
- **Repeat or Exit:** After completing one request, provides user an option to fetch another URL or exit the program.

## Getting Started

### Prerequisites

- Python 3 (can be downloaded from <a href="https://www.python.org/downloads/" target="_blank">Python Official website</a>)
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

1. Run the `fetch_html.py` file located inside the `src` folder of this project.
2. Follow the on-screen prompts:
   - **Enter the website link**: Provide a valid URL starting with `http://` or `https://` (e.g., `https://example.com`).
   - **Allow redirects:** Specify whether to allow HTTP redirects (`yes` or `no`).
   - **Set timeout value:** Enter a positive integer for the request timeout in seconds (e.g., `5`, `10`, `12`,...).
   - **Save HTML content:** Choose whether to save the fetched HTML content to a file (`yes` or `no`).
3. If saving the file:
   - Enter a file name.
   - If the file already exists, you will be prompted to overwrite or choose a different name.
4. To fetch another URL when prompted, answer `yes` and repeat the same process. To exit the script, answer `no`.

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

If you encounter any bugs or have suggestions for improvement, please report them in the <a href="https://github.com/Atia-Farha/HTML-Fetcher-Script/issues" target="_blank">Issues</a> section of this GitHub repository. I will address them promptly.

## License
This script is provided for personal, non-commercial purposes. Commercial use of this software is not permitted. When using this script, credit must be given to the original author. For more details, read [LICENSE file](LICENSE).

<p align="center">© Originally written by <a href="https://github.com/Atia-Farha" target="_blank">Atia Farha</a></p>
