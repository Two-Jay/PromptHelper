from enum import Enum
from abc import ABCMeta, abstractmethod

class Models_Catalog(Enum):
    __metaclass__ = ABCMeta
    pass

    def __init__(self, model_name: str):
        self.model_name = model_name

    def __str__(self):
        return self.model_name
    
    def __repr__(self):
        return self.model_name

    @classmethod
    def get_model_list(cls):
        return [model.model_name for model in cls]

    @staticmethod
    @abstractmethod
    def validate_api_key(api_key: str):
        return False
    
class OAI_models(Models_Catalog):
    GPT_4_TURBO = "gpt-4o-mini"
    GPT_4_O = "gpt-4o"
    GPT_4 = "gpt-4-turbo"

class Google_models(Models_Catalog):
    GEMINI_1_5 = "gemini-1.5"
    GEMINI_1_11 = "gemini-1.11"
    GEMINI_3_5 = "gemini-3.5"
    GEMINI_3_11 = "gemini-3.11"
 
class Anthropic_models(Models_Catalog):
    CLAUDE_3_OPUS = "claude-3-opus-20240229"
    CLAUDE_3_HAIKU = "claude-3-haiku-20240307"
    CLAUDE_3_SONNET = "claude-3-sonnet-20240229"

def is_oai_model(model_name: str):
    return model_name in OAI_models.get_model_list()

def is_google_model(model_name: str):
    return model_name in Google_models.get_model_list()

def is_anthropic_model(model_name: str):
    return model_name in Anthropic_models.get_model_list()

def is_valid_model(model_name: str, company: str = None):
    match company:
        case "oai":
            return is_oai_model(model_name)
        case "google":
            return is_google_model(model_name)
        case "anthropic":
            return is_anthropic_model(model_name)
        case "all":
            return is_oai_model(model_name) or is_google_model(model_name) or is_anthropic_model(model_name)
        case None:
            return False
        case _:
            return False

def get_model_enum(model_name: str):
    for enum_class in [OAI_models, Google_models, Anthropic_models]:
        try:
            return enum_class(model_name)
        except ValueError:
            continue
    return None
    
def get_all_valid_models():
    return [model.value for model in OAI_models] \
        + [model.value for model in Google_models] \
        + [model.value for model in Anthropic_models]
