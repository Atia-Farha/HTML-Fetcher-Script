import os
import requests

def get_valid_url() -> str:
    """
    Prompt the user for a URL and validate its format.

    Returns:
        str: A valid URL that starts with 'http://' or 'https://'.
    """
    while True:
        url = input("Enter the website link:\n").strip()
        if not url:
            print("The URL cannot be empty. Please enter a valid URL.")
            continue
        if url.startswith("http://") or url.startswith("https://"):
            return url
        print("Invalid URL format. Please ensure the URL starts with 'http://' or 'https://'.")

def get_valid_redirects() -> bool:
    """
    Prompt the user to allow or disallow redirects.

    Returns:
        bool: True if redirects are allowed, False otherwise.
    """
    while True:
        redirects_input = input("Do you want to allow redirects? (yes/no)\n").strip().lower()
        if redirects_input in ('yes', 'no'):
            return redirects_input == 'yes'
        print("Invalid answer for redirects. Please enter 'yes' or 'no'.")

def get_valid_timeout() -> int:
    """
    Prompt the user to set a timeout value, ensuring it is a positive integer.

    Returns:
        int: A positive integer representing the timeout value in seconds.
    """
    while True:
        try:
            timeout = int(input("Set timeout value (in seconds):\n").strip())
            if timeout > 0:
                return timeout
            print("Timeout must be a positive integer. Please try again.")
        except ValueError:
            print("Invalid timeout value. Please enter a valid integer for timeout.")

def fetch_html(url: str, allow_redirects: bool, timeout: int) -> None:
    """
    Fetch HTML content from a URL, handle various exceptions, and provide options to save the content.

    Parameters:
        url (str): The URL to fetch the HTML content from.
        allow_redirects (bool): Whether to allow redirects.
        timeout (int): Timeout for the request in seconds.

    Returns:
        None
    """
    try:
        response = requests.get(url, timeout=timeout, allow_redirects=allow_redirects)
        response.raise_for_status()

        print(f"\nStatus Code: {response.status_code}")
        print(f"Content fetched successfully from {url}!\n")

        print("Response headers:")
        for header, value in response.headers.items():
            print(f'{header}: {value}')

        print("\nHTML Code:")
        print(response.text)

        while True:
            save_file = input("\nDo you want to save the HTML content as a file? (yes/no)\n").strip().lower()
            if save_file in ('yes', 'no'):
                break
            print("Invalid input. Please enter 'yes' or 'no'.")

        if save_file == 'yes':
            print("\nBy default, without specifying a path, the file will be saved in the same directory where the script is running.\nIf you want to save the file in a different location, you can specify an absolute file path when entering the file name.\n")
            while True:
                file_name = input("Enter the file name:\n").strip() + '.html'
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
    """
    Main function to interact with the user and fetch HTML content from websites.

    Returns:
        None
    """
    print("Welcome! This script will help you fetch HTML code from a website.")
    while True:
        link = get_valid_url()
        redirects_allowed = get_valid_redirects()
        timeout_seconds = get_valid_timeout()
        fetch_html(link, redirects_allowed, timeout_seconds)

        while True:
            repeat_fetch = input("\nDo you want to fetch another URL? (yes/no)\n").strip().lower()
            if repeat_fetch in ('yes', 'no'):
                break
            print("Invalid input. Please enter 'yes' or 'no'.")

        if repeat_fetch != 'yes':
            print("\nExiting the script. Goodbye!")
            break

if __name__ == "__main__":
    main()
