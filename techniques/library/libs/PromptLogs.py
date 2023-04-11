import pandas as pd
from typing import Optional
from ResponseParser import ResponseParser

class PromptLogs:
    def __init__(self, response_parser: Optional[ResponseParser] = None) -> None:
        self.response_parser = response_parser
        self.df = pd.DataFrame()
    
    def extract_dataframe(self) -> None:
        if self.response_parser is not None:
            self.df = self.response_parser.get_dataframe()
    
    def append(self, response_parser: ResponseParser) -> None:
        additional_df = response_parser.get_df()
        self.df = pd.concat([self.df, additional_df])

    def get_df(self) -> pd.DataFrame:
        return self.df
    
    @property
    def styled_log(self) -> pd.DataFrame:
        self.df_needed = self.df[['id', 'created', 'model', 'usage', 'all_code']]
        self.styled_log = self.df_needed.style.set_properties(**{'text-align': 'left'})

        return self.styled_log

