import openai
import pandas as pd

class OpenAIResponseParser:
    def __init__(self, response):

        self.response = response

        self.df = pd.DataFrame(
            {
                "id": [],
                "created": [],
                "model": [],
                "usage": [],
                "content": [],
            }
        )

        self._store_response()

    def _store_response(self):
        content = self.response['choices'][0]['message']['content'].strip()

        self.df = pd.concat(
            [
                self.df,
                pd.DataFrame(
                    {
                        "id": [self.response['id']],
                        "created": [self.response['created']],
                        "model": [self.response['model']],
                        "usage": [self.response['usage']['prompt_tokens']],
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
