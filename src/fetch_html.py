"""
This Script is originally written by Atia Farha.
"""

import os
import requests


def get_valid_url() -> str:
    """
    Prompt the user for a URL and validate its format.

    Returns:
        str: A valid URL that starts with 'http://' or 'https://'.
    """
    while True:
        # Ask the user to enter a website URL.
        url = input("Enter the website link:\n").strip()
        
        # Check if the URL is empty.
        if not url:
            print("The URL cannot be empty. Please enter a valid URL.")
            continue
        
        # Ensure the URL starts with 'http://' or 'https://'.
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
        # Ask the user if they want to allow redirects.
        redirects_input = input("Do you want to allow redirects? (yes/no)\n").strip().lower()
        
        # Validate the input.
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
            # Ask the user to enter a timeout value in seconds.
            timeout = int(input("Set timeout value (in seconds):\n").strip())
            
            # Ensure the timeout value is positive.
            if timeout > 0:
                return timeout
            
            print("Timeout must be a positive integer. Please try again.")
        
        except ValueError:
            # Handle invalid inputs (e.g., non-integer values).
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
        # Make the HTTP GET request.
        response = requests.get(url, timeout=timeout, allow_redirects=allow_redirects)
        response.raise_for_status()  # Raise an exception for HTTP errors.

        # Display the status code and confirmation message.
        print(f"\nStatus Code: {response.status_code}")
        print(f"Content fetched successfully from {url}!\n")

        # Display the response headers.
        print("Response headers:")
        for header, value in response.headers.items():
            print(f'{header}: {value}')

        # Display the HTML content.
        print("\nHTML Code:")
        print(response.text)

        # Prompt the user to save the HTML content to a file.
        while True:
            save_file = input("\nDo you want to save the HTML content as a file? (yes/no)\n").strip().lower()
            if save_file in ('yes', 'no'):
                break
            print("Invalid input. Please enter 'yes' or 'no'.")

        if save_file == 'yes':
            # Explain file saving details to the user.
            print("\nBy default, the file will be saved in the script's directory.\n"
                  "You can also specify an absolute file path.\n")

            while True:
                # Ask the user to enter a file name.
                file_name = input("Enter the file name:\n").strip() + '.html'
                
                # Handle file naming conflicts.
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

            # Save the HTML content to the specified file.
            with open(file_name, 'w', encoding='utf-8') as file:
                file.write(response.text)
            print(f"\nHTML content saved to {file_name}.")

    # Handle various exceptions.
    except requests.exceptions.InvalidURL:
        print("\nThe URL provided is not valid. Check the URL format and try again.")

    except requests.exceptions.ContentDecodingError:
        print("\nError decoding the response content. The content may be corrupted.")

    except requests.exceptions.HTTPError as http_err:
        print(f"\nHTTP error occurred: {http_err}")

    except requests.exceptions.ConnectionError as conn_err:
        print(f"\nConnection error occurred: {conn_err}")

    except requests.exceptions.Timeout as timeout_err:
        print(f"\nTimeout error occurred: {timeout_err}")

    except requests.exceptions.RequestException as err:
        print(f"\nAn error occurred: {err}")


def main():
    """
    Main function to interact with the user and fetch HTML content from websites.

    Returns:
        None
    """
    print("Welcome! This script will help you fetch HTML code from a website.")
    while True:
        # Get the URL, redirect settings, and timeout value from the user.
        link = get_valid_url()
        redirects_allowed = get_valid_redirects()
        timeout_seconds = get_valid_timeout()
        
        # Fetch the HTML content.
        fetch_html(link, redirects_allowed, timeout_seconds)

        # Ask the user if they want to fetch another URL.
        while True:
            repeat_fetch = input("\nDo you want to fetch another URL? (yes/no)\n").strip().lower()
            if repeat_fetch in ('yes', 'no'):
                break
            print("Invalid input. Please enter 'yes' or 'no'.")

        if repeat_fetch != 'yes':
            print("\nExiting the script. Goodbye!")
            break


# Entry point of the script.
if __name__ == "__main__":
    main()