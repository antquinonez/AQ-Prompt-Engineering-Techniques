# Response Parser
# The ResponseParser is a utility class designed to parse and store the responses from the
# OpenAI API, specifically for code generation tasks. The main goal is to provide a
# user-friendly way to access and analyze the content of the API responses, including code
# blocks and other relevant information.

# Features
# - Parse and store API response data in a pandas DataFrame for easy manipulation and
#   analysis.
# - Extract code blocks from the response content and store them separately.
# - Apply styling to the DataFrame for better readability.

import pandas as pd
import re
from typing import List, Dict, Any


class ResponseParser:
    def __init__(self, response: Dict[str, Any]) -> None:
        """
        Initialize OpenAIResponseParser with API response.

        :param response: API response from OpenAI.
        """
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
        self._style()


    def _style(self) -> None:
        """
        Apply styling to the DataFrame.
        """
        self.df_needed = self.df[['id', 'created', 'model', 'usage', 'all_code']]
        self.styled_log = self.df_needed.style.set_properties(**{'text-align': 'left'})


    def _store_response(self) -> None:
        """
        Store the response content into the DataFrame.
        """
        content = self.response['choices'][0]['message']['content'].strip()

        pattern = re.compile(r"```python([\s\S]*?)```")
        code_blocks = re.findall(pattern, content)

        all_code = ""
        for code_block in code_blocks:
            all_code  += code_block.strip() + "\n"

        df = pd.DataFrame(
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

        # concatenate the new DataFrame with the existing DataFrame
        self.df = pd.concat( [self.df, df], ignore_index=False,)
        
        # format an all_code string
        def format_text(text):
            return text.replace('\n', '<br>').replace(' ', '&nbsp;')
        
        # Apply the formatting function to the all_code column
        self.df['all_code'] = self.df['all_code'].apply(format_text)

        # I don't get why this is broken, but it doesn't matter for now...or ever?
        # # format a code block
        # def format_list(code_blocks:list):
        #     code_block_string = ""

        #     for block in code_blocks:
        #         block.replace('\n', '<br>').replace(' ', '&nbsp;')
        #         code_block_string += block
                 
        # # Apply the formatting function to the code_blocks column
        # self.df['code_blocks'] = self.df['code_blocks'].apply(format_list)


    def get_df(self) -> pd.DataFrame:
        """
        Get the DataFrame containing the API response.

        :return: DataFrame containing the API response.
        """
        # self.df = self.df.set_index('id')
        return self.df
