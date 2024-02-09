# Web Crawler

## Introduction
This Crawler is designed to parse HTML and extract content from it. It includes code blocks and functions implemented to handle well-written HTML pages. Some edge cases are also handled, although the module assumes that HTML pages are structured correctly.

## Author
Narayan Jat

## Date
11 January 2024

## Description
The script fetches content from a given URL, removes HTML tags, and extracts the main content from the page. It also collects all anchor links present on the page and prints them separately at the end.

## Usage
  1. Run the script and provide a URL when prompted.
  2. The script will fetch the content from the provided URL and parse the HTML.
  3. It will then remove HTML tags, extract the main content, and print it to the terminal.
  4. Finally, it will print all the URLs that the page links to.

## Dependencies
The script relies on the requests module, which can be installed via pip:

    pip install requests

## Notes
  1. The script assumes that the provided URL leads to a well-structured HTML page.
  2. Additional testing and validation may be required for specific use cases.
