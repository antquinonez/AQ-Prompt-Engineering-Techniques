import openai
import polars as pl

class OpenAIResponseHandler:
    def __init__(self, api_key):
        openai.api_key = api_key
        self.df = pl.DataFrame(
            {
                "id": [],
                "created": [],
                "model": [],
                "usage": [],
                "content": [],
            }
        )

                # "role": [],

    def store_response(self, response):
        content = response['choices'][0]['message']['content'].strip()

        self.df = self.df.vstack(
            pl.DataFrame(
                {
                    "id": [response['id']],
                    "created": [response['created']],
                    "model": [response['model']],
                    "usage": [response['usage']['prompt_tokens']],
                    "content": [content],
                }
            )
        )

                    # "role": [response['choices'][0]['message']['role']],

    def request_prompt(self, prompt, model='text-davinci-002', max_tokens=150):
        response = openai.Completion.create(
            engine=model,
            prompt=prompt,
            max_tokens=max_tokens,
            n=1,
            stop=None,
            temperature=0.5,
        )
        self.store_response(response)

    def get_dataframe(self):
        return self.df

# # Example usage:
# api_key = "your_openai_api_key"
# handler = OpenAIResponseHandler(api_key)

# prompt1 = "Write a short summary about the history of computer programming."
# handler.request_prompt(prompt1)

# prompt2 = "Describe the main features of the Python programming language."
# handler.request_prompt(prompt2)

# df = handler.get_dataframe()
# print(df)
