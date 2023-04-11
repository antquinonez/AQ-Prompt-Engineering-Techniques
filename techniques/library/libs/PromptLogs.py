import pandas as pd
from typing import Optional
from ResponseParser import ResponseParser

class PromptLogs:
    def __init__(self, response_parser: Optional[ResponseParser] = None) -> None:
        self.response_parser = response_parser
        self.df = pd.DataFrame()
    
    def extract_dataframe(self) -> None:
        if self.response_parser is not None:
            self.df = self.response_parser.get_df()
            self.df = self.df.set_index('id')
    
    def append(self, response_parser: ResponseParser) -> None:
        additional_df = response_parser.get_df()
        # additional_df = additional_df.reset_index()
        self.df = pd.concat([self.df, additional_df])

    def get_df(self) -> pd.DataFrame:
        self.df = self.df.set_index('id')
        return self.df
    
    @property
    def styled_log(self) -> pd.DataFrame:
        df_needed = self.df[['id', 'created', 'model', 'usage', 'all_code']]
        df_needed = df_needed.set_index('id')

        styled_log_df = df_needed.style.set_properties(**{'text-align': 'left'})

        return styled_log_df
