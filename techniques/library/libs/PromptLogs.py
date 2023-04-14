import pandas as pd
from typing import Optional
from ResponseParser import ResponseParser
from IDGenerator import IDGenerator

class PromptLogs:
    def __init__(self) -> None:
        self.df = pd.DataFrame()
        self.id_generator = IDGenerator()


    def extract_dataframe(self) -> None:
        if self.response_parser is not None:
            self.df = self.response_parser.get_df()
            self.df = self.df.set_index('id')


    def append(self, messages:list, response_parser: ResponseParser) -> None:
        print(messages)
        
        # Add brackets and remove the first and last characters
        messages_str = str(messages)
        messages_str_with_brackets = "[" + messages_str[1:-1] + "]"  

        additional_df = response_parser.get_df()
        
        # Add the ID column to the additional_df
        additional_df['sid'] = [self.id_generator.get_id() for _ in range(len(additional_df))]
        additional_df['prompts'] = messages_str_with_brackets
        
        print("df:", self.df)
        
        # # Check if 'sid' values in both dataframes are not equal before concatenating
        # if len(self.df) > 1:
        #     if not self.df['sid'].equals(additional_df['sid']):
        #         self.df = pd.concat([self.df, additional_df])


        self.df = pd.concat([self.df, additional_df])


    def get_df(self) -> pd.DataFrame:
        self.df = self.df.set_index('id')
        return self.df
    
    @property
    def styled_log(self) -> pd.DataFrame:
        df_needed = self.df[['sid', 'id', 'created', 'model', 'usage', 'prompts', 'all_code', 'content']]
        df_needed = df_needed.set_index('sid')

        styled_log_df = df_needed.style.set_properties(**{'text-align': 'left'})

        return styled_log_df
