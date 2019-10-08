from .base import CharacterPrompt


class CreatePublisher(object):
    class NamePrompt(CharacterPrompt):
        class Meta(CharacterPrompt.Meta):
            text = 'Enter a name to identify this Publisher:'

    class SigningKeyIDPrompt(CharacterPrompt):
        class Meta(CharacterPrompt.Meta):
            text = 'Enter a name for this Publisher\'s first signing key:'
