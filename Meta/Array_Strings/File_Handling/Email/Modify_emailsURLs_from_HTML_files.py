import re
from collections import namedtuple

def parse_tld_file(filename):
    """Parses a file containing top-level domains (TLDs).

    Args:
        filename: The name of the file containing TLDs.

    Returns:
        A list of TLDs.
    """

    tlds = set()
    with open(filename, 'r') as file:
        for line in file:
            tlds.add(line.strip())

    return list(tlds)

def modify_html(input_filename, output_filename, tlds, email_map={"support@test.com": "support@fb.com"}):
    """Reads an HTML file, modifies email addresses and URLs, and writes to a new file.

    Args:
        input_filename: The name of the input HTML file.
        output_filename: The name of the output HTML file.
        tlds: A list of top-level domains (TLDs).
        email_map: A dictionary mapping original email addresses to new ones.
    """

    with open(input_filename, 'r') as input_file, open(output_filename, 'w') as output_file:
        for line in input_file:
            # Modify email addresses
            line = re.sub(r"\b([a-zA-Z0-9_.+-]+\@[a-zA-Z0-9-]+\.[a-zA-Z]+)",
                          lambda match: email_map.get(match.group(0), match.group(0)), line)

            # Modify URLs
            url_pattern = r"(?:https?://)?(?:[a-zA-Z0-9_\-]+\.)+({}))".format("|".join(tlds))
            line = re.sub(url_pattern, lambda match: re.sub(r"\.[a-z]+$", ".fb", match.group(0)), line)

            output_file.write(line)

# Example usage
tlds = parse_tld_file("tlds.txt")
email_map = {"support@test.com": "support@fb.com"}
modify_html("input.html", "output.html", tlds, email_map)


""""
Explanation:

Parse TLDs: The parse_tld_file function reads a file containing TLDs and returns a list of TLDs.
Modify HTML: The modify_html function takes the input filename, output filename, TLD list, and an optional email map as arguments.
It opens the input and output files.
It iterates through each line in the input file.
It uses regular expressions to:
Modify email addresses:
Match email addresses using a pattern \b([a-zA-Z0-9_.+-]+\@[a-zA-Z0-9-]+\.[a-zA-Z]+).
Replace the matched email address with its corresponding new address from the email_map dictionary. If no mapping exists, the original email address is kept.
Modify URLs:
Match URLs using a pattern that includes the provided TLDs and allows optional protocol (http/https).
Replace the top-level domain of the matched URL with ".fb".
The modified line is written to the output file.
Key Improvements:

Separate TLD Parsing: Keeps TLD parsing separate from the main logic for modularity.
Regular Expressions: Uses regular expressions for efficient pattern matching.
Optional Email Map: Allows customization of email address changes.
Error Handling: Consider adding error handling for file I/O or invalid input.
Testing: Implement unit tests to ensure the functionality for various input scenarios.
Complexity:

Time Complexity: O(n), where n is the number of words in the HTML file.
Space Complexity: O(n), for temporary storage of the modified lines.
This approach provides a more structured and efficient solution for modifying email addresses and URLs in HTML files.

"""