"""
        PartNLP
            AUTHORS:
                MOSTAFA & SAMAN
"""
from PartNLP.models.validation.validator import Validator


class LemmatizeValidator(Validator):
    def __init__(self, config):
        super(LemmatizeValidator, self).__init__(config)
        self.config = config

    def isvalid(self):
        """
        :return:
        """
        return True, '', None

    def get_dependencies(self):
        return ['S_TOKENIZE', 'W_TOKENIZE', 'POS']
