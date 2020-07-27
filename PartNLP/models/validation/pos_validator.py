"""
        SEMANTIC SEARCH ENGINE
            AUTHORS:
                MOSTAFA & SAMAN
"""
from PartNLP.models.validation.validator import Validator


class PosValidator(Validator):
    def __init__(self, config):
        super().__init__(config)
        self.config = config

    def isvalid(self):
        """
        :return: True or False, error_message
        """
        return True, '', None

    def update_config_value(self, name, old_value, new_value):
        self.config[name] = new_value

    def get_dependencies(self):
        return ['S_TOKENIZE', 'W_TOKENIZE']
