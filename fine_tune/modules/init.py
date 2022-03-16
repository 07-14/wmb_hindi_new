

from token_classification import TokenClassification


modules = {
    'masked_lm': MaskedLM,
    'multiple_choice': MultipleChoice,
    'text_classification': TextClassification,
    'token_classification': TokenClassification,
    'xsent_retrieval': XSentRetrieval
}


def get_modules(name=None):
    if name:
        return modules[name]
    return modules.values()
