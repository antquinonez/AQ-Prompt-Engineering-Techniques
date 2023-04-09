# OpenAI Response Parser
# The OpenAIResponseParser is a utility class designed to parse and store the responses from the OpenAI API, specifically for code generation tasks. The main goal is to provide a user-friendly way to access and analyze the content of the API responses, including code blocks and other relevant information.

# Features
# - Parse and store API response data in a pandas DataFrame for easy manipulation and analysis.
# - Extract code blocks from the response content and store them separately.
# - Apply styling to the DataFrame for better readability.

import pandas as pd
from typing import List, Dict, Any


class OpenAIResponseParser:
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
        self.style = self.df.style.set_properties(**{'text-align': 'left'})

    def _store_response(self) -> None:
        """
        Store the response content into the DataFrame.
        """
        content = self.response['choices'][0]['message']['content'].strip()

        import re

        pattern = re.compile(r"```python([\s\S]*?)```")
        code_blocks = re.findall(pattern, content)

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

    def get_dataframe(self) -> pd.DataFrame:
        """
        Get the DataFrame containing the API response.

        :return: DataFrame containing the API response.
        """
        return self.df
