from .base import CharacterPrompt


class CreatePublisher(object):
    class CreateCodePrompt(CharacterPrompt):
        class Meta(CharacterPrompt.Meta):
            text = 'Enter the Publisher Create Code provided by Inspired:'

    class EmailPrompt(CharacterPrompt):
        class Meta(CharacterPrompt.Meta):
            text = 'Enter an email address to associate with this Publisher:'

    class NamePrompt(CharacterPrompt):
        class Meta(CharacterPrompt.Meta):
            text = 'Enter a name to identify this Publisher:'

    class SigningKeyIDPrompt(CharacterPrompt):
        class Meta(CharacterPrompt.Meta):
            text = 'Enter a name for this Publisher\'s first signing key:'
