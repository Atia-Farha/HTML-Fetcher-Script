import os
import requests

def get_valid_url() -> str:
    """Prompt the user for a URL and validate its format."""
    while True:
        # Ask the user to enter a website URL
        url = input("Enter the website link (e.g., https://example.com):\n").strip()
        # Check if the URL is empty
        if not url:
            print("The URL cannot be empty. Please enter a valid URL.")
            continue
        # Check if the URL starts with 'http://' or 'https://'
        if url.startswith("http://") or url.startswith("https://"):
            return url
        # If the URL format is invalid, prompt the user to try again
        print("Invalid URL format. Please ensure the URL starts with 'http://' or 'https://'.")

def get_valid_redirects() -> bool:
    """Prompt the user to allow or disallow redirects."""
    while True:
        # Ask the user if they want to allow redirects (True or False)
        redirects_input = input("Allow redirects? Enter 'True' or 'False':\n").strip().lower()
        # Validate the user's input and return the appropriate boolean value
        if redirects_input in ('true', 'false'):
            return redirects_input == 'true'
        # If the input is invalid, prompt the user to try again
        print("Invalid answer for redirects. Please enter 'True' or 'False'.")

def get_valid_timeout() -> int:
    """Prompt the user to set a timeout value, ensuring it is a positive integer within a reasonable range."""
    while True:
        try:
            # Ask the user to set a timeout value (in seconds)
            timeout = int(input("Set timeout value (in seconds):\n").strip())
            # Check if the timeout is a positive integer
            if timeout > 0:
                return timeout
            # If the timeout is not positive, prompt the user to try again
            print("Timeout must be a positive integer. Please try again.")
        except ValueError:
            # If the user enters a non-integer value, prompt them to try again
            print("Invalid timeout value. Please enter a valid integer for timeout.")

def fetch_html(url: str, allow_redirects: bool, timeout: int) -> None:
    """Fetch HTML content from a URL, handle various exceptions, and provide options to save the content."""
    try:
        # Send a GET request to the URL with the specified timeout and redirect options
        response = requests.get(url, timeout=timeout, allow_redirects=allow_redirects)
        # Raise an HTTPError if the status code indicates an error
        response.raise_for_status()

        # Display the status code of the response
        print(f"\nStatus Code: {response.status_code}")
        print(f"Content fetched successfully from {url}!\n")

        # Print the headers of the response
        print("Response headers:")
        for header, value in response.headers.items():
            print(f'{header}: {value}')

        # Print the HTML content of the response
        print("\nHTML Code:")
        print(response.text)

        # Ask the user if they want to save the HTML content to a file
        while True:
            save_file = input("\nDo you want to save the HTML content as a file? (yes/no)\n").strip().lower()

            if save_file in ('yes', 'no'):
                break

            print("Invalid input. Please enter 'yes' or 'no'.")

        # If the user wants to save the content, ask for a file name and save the content
        if save_file == 'yes':
            print("\nBy default, without specifying a path, the file will be saved in the same directory where the script is running.\nIf you want to save the file in a different location, you can specify an absolute file path when entering the file name.\n")
            while True:
                file_name = input("Enter the file name:\n").strip() + '.html'
                # Check if the file already exists
                if os.path.exists(file_name):
                    overwrite = input(f"The file '{file_name}' already exists. Do you want to overwrite it? (yes/no)\n").strip().lower()
                    if overwrite == 'yes':
                        break
                    elif overwrite == 'no':
                        print("Please enter a different file name.")
                        continue
                    else:
                        print("Invalid input. Please enter 'yes' or 'no'.")
                        continue
                else:
                    break

            with open(file_name, 'w', encoding='utf-8') as file:
                file.write(response.text)
            print(f"\nHTML content saved to {file_name}.")

    # Handle specific exceptions that may occur during the request
    except requests.exceptions.InvalidURL:
        print("\nThe URL provided is not valid. Check the URL format and try again.")
        print("If the issue persists, trying a different URL might help.")

    except requests.exceptions.ContentDecodingError:
        print("\nError decoding the response content. The content may be corrupted or the server might be sending an incorrect content type.")
        print("You might want to check the server's status or try fetching the content later.")
        print("If the issue persists, trying a different URL might help.")

    except requests.exceptions.HTTPError as http_err:
        print(f"\nHTTP error occurred: {http_err}")
        print("Please check the URL or try again later.")
        print("If the issue persists, trying a different URL might help.")

    except requests.exceptions.ConnectionError as conn_err:
        print(f"\nConnection error occurred: {conn_err}")
        print("There was a problem with the network connection. Ensure you are connected to the stable internet and try again.")
        print("If the issue persists, trying a different URL might help.")

    except requests.exceptions.Timeout as timeout_err:
        print(f"\nTimeout error occurred: {timeout_err}")
        print("The request timed out. Please try increasing the timeout value.")
        print("If the issue persists, trying a different URL might help.")

    except requests.exceptions.ChunkedEncodingError:
        print("\nError with the chunked transfer encoding. The server may be sending data incorrectly. Try again later.")
        print("If the issue persists, trying a different URL might help.")

    except requests.exceptions.RequestException as err:
        print(f"\nAn error occurred: {err}")
        print("Please try again later.")
        print("If the issue persists, trying a different URL might help.")

def main():
    """Main function to interact with the user and fetch HTML content from websites."""
    print("Welcome! This script will help you fetch HTML code from a website.")
    while True:
        # Get a valid URL, redirect option, and timeout value from the user
        link = get_valid_url()
        redirects_allowed = get_valid_redirects()
        timeout_seconds = get_valid_timeout()
        # Fetch the HTML content of the specified URL
        fetch_html(link, redirects_allowed, timeout_seconds)

        # Ask the user if they want to fetch another URL
        while True:
            repeat_fetch = input("\nDo you want to fetch another URL? (yes/no)\n").strip().lower()

            if repeat_fetch in ('yes', 'no'):
                break

            print("Invalid input. Please enter 'yes' or 'no'.")

        # Exit the loop and script if the user doesn't want to fetch another URL
        if repeat_fetch != 'yes':
            print("\nExiting the script. Goodbye!")
            break

# Run the main function if this script is executed as the main module
if __name__ == "__main__":
    main()
