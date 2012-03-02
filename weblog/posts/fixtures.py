import random
from autofixture.base import AutoFixture

TAGS = ('Lorem ipsum', 'amet', 'ipsum')

class PostFixture(AutoFixture):
    
    def get_value(self, field):
        if field.name == 'tags':
            return random.choice(TAGS)
        return super(PostFixture, self).get_value(field)
