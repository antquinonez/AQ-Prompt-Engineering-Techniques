# MessageParser
# Overview
# The MessageParser parses and extracts structured messages from a given input string. Messages are identified based on a predefined pattern of 'role' and 'prompt' separated by a colon.

# Usage
# To use the MessageParser class, create an instance by passing the input string containing the messages. Then, call the parse_messages method to extract the messages.

# Here's an example:
# prompts = """
# system: system: You are a software expert. Use. "```python" style for code blocks. 
# user: Write python code for fibonacci sequence.

# """

# parser = MessageParser(prompts)
# messages = parser.parse_messages()

# for message in messages:
#     print(f"{message['role']}: {message['prompt']}")


import re
from typing import List, Dict

class MessageParser:
    """
    A class to parse messages based on a predefined pattern.

    Attributes:
        input_string (str): The input string containing messages to be parsed.
        message_pattern (Pattern): The compiled regex pattern used to extract messages from the input_string.
    """

    def __init__(self, input_string: str):
        """
        Initialize a MessageParser object with the given input string.

        Args:
            input_string (str): The input string containing messages to be parsed.
        """
        self.input_string = input_string
        self.message_pattern = re.compile(r'^(?P<role>\w+):\s*(?P<content>.*?)\s*$', re.MULTILINE)

    def parse(self) -> List[Dict[str, str]]:
        """
        Parse the messages from the input_string based on the message_pattern.

        Returns:
            List[Dict[str, str]]: A list of dictionaries containing the parsed messages, where each dictionary
                                  has two keys: 'role' and 'content'.
        """
        messages = []
        for match in self.message_pattern.finditer(self.input_string):
            role = match.group('role').strip()
            content = match.group('content').strip()

            if role and content:
                messages.append({
                    'role': role,
                    'content': content
                })

        return messages
