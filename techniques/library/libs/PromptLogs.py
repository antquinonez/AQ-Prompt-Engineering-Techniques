import pandas as pd
from typing import Optional
from ResponseParser import ResponseParser
from IDGenerator import IDGenerator

class PromptLogs:
    def __init__(self, response_parser: Optional[ResponseParser] = None) -> None:
        self.response_parser = response_parser
        self.df = pd.DataFrame()
        self.id_generator = IDGenerator()
    
    def extract_dataframe(self) -> None:
        if self.response_parser is not None:
            self.df = self.response_parser.get_df()
            self.df = self.df.set_index('id')
    
    def append(self, response_parser: ResponseParser) -> None:
        additional_df = response_parser.get_df()
        
        # Add the ID column to the additional_df
        additional_df['sid'] = [self.id_generator.get_id() for _ in range(len(additional_df))]
        print ("additional_df: ", additional_df)
        
        self.df = pd.concat([self.df, additional_df])

    def get_df(self) -> pd.DataFrame:
        self.df = self.df.set_index('id')
        return self.df
    
    @property
    def styled_log(self) -> pd.DataFrame:
        df_needed = self.df[['sid', 'id', 'created', 'model', 'usage', 'all_code']]
        df_needed = df_needed.set_index('sid')

        styled_log_df = df_needed.style.set_properties(**{'text-align': 'left'})

        return styled_log_df
