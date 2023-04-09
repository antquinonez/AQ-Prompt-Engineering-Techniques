import re

class MessageParser:
    def __init__(self, input_string: str):
        self.input_string = input_string
        self.message_pattern = re.compile(r'^(?P<role>\w+):\s*(?P<content>.*?)\s*$', re.MULTILINE)

    def parse_messages(self):
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

# # Example usage
# example_string = """
# User: Hi there!
# Agent: Hello, how can I help you today?
# User: I need assistance with my account.
# Agent: Sure, please provide your account number.
# """

# parser = MessageParser(example_string)
# messages = parser.parse_messages()
# print(messages)
