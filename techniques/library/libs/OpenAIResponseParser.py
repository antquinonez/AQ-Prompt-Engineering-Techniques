import openai
import polars as pl
# import pandas as pd

class OpenAIResponseParser:
    def __init__(self, response):

        self.response = response

        self.df = pl.DataFrame(
            {
                "id": [],
                "created": [],
                "model": [],
                "usage": [],
                "content": [],
            }
        )

        self._store_response()

                # "role": [],

    def _store_response(self):
        content = self.response['choices'][0]['message']['content'].strip()

        self.df = self.df.vstack(
            pl.DataFrame(
                {
                    "id": [self.response['id']],
                    "created": [self.response['created']],
                    "model": [self.response['model']],
                    "usage": [self.response['usage']['prompt_tokens']],
                    "content": [content],
                }
            )
        )

        print(self.df)

                    # "role": [response['choices'][0]['message']['role']],


    def get_dataframe(self):
        return self.df.to_pandas()

# # Example usage:
# api_key = "your_openai_api_key"
# handler = OpenAIResponseHandler(api_key)

# prompt1 = "Write a short summary about the history of computer programming."
# handler.request_prompt(prompt1)

# prompt2 = "Describe the main features of the Python programming language."
# handler.request_prompt(prompt2)

# df = handler.get_dataframe()
# print(df)
