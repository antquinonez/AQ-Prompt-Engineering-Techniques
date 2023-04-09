import openai
import pandas as pd
# Set display options
pd.set_option('display.max_columns', None)  # Display all columns
pd.set_option('display.expand_frame_repr', False)  # Prevent line break in DataFrame
pd.set_option('display.max_colwidth', None)  # Display the full content of cells


class OpenAIResponseParser:
    def __init__(self, response):

        self.response = response

        self.df = pd.DataFrame(
            {
                "id": [],
                "created": [],
                "model": [],
                "usage": [],
                "all_code": [],
                "code_blocks": [],
                "content": [],
            }
        )

        self._store_response()

    def _store_response(self):
        content = self.response['choices'][0]['message']['content'].strip()

        import re

        pattern = re.compile(r"```python([\s\S]*?)```")
        code_blocks = re.findall(pattern, content)
        print ("code_blocks:", code_blocks)

        all_code = ""
        for code_block in code_blocks:
            all_code  += code_block.strip() + "\n"
            
        self.df = pd.concat(
            [
                self.df,
                pd.DataFrame(
                    {
                        "id": [self.response['id']],
                        "created": [self.response['created']],
                        "model": [self.response['model']],
                        "usage": [self.response['usage']['prompt_tokens']],
                        "all_code": [all_code],
                        "code_blocks": [code_blocks],
                        "content": [content],
                    }
                )
            ],
            ignore_index=True,
        )

        print(self.df)

    def get_dataframe(self):
        return self.df

# Example usage:
# api_key = "your_openai_api_key"
# handler = OpenAIResponseHandler(api_key)

# prompt1 = "Write a short summary about the history of computer programming."
# handler.request_prompt(prompt1)

# prompt2 = "Describe the main features of the Python programming language."
# handler.request_prompt(prompt2)

# df = handler.get_dataframe()
# print(df)
