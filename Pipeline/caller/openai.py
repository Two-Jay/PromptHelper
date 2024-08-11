from enum import Enum

class Models_Catalog(Enum):
    pass

    def __init__(self, model_name: str, model_description: str):
        self.model_name = model_name
        self.model_description = model_description

    def __str__(self):
        return self.model_name
    
    def __repr__(self):
        return self.model_name

    @staticmethod
    def get_model_list():
        return [model.value for model in OAI_models]

class OAI_models(Models_Catalog):
    GPT_4_TURBO = "gpt-4o-mini"
    GPT_4_O = "gpt-4o"
    GPT_4 = "gpt-4-turbo"
