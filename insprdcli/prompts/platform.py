from .base import CharacterPrompt


class PlatformDomainPrompt(CharacterPrompt):
    class Meta(CharacterPrompt.Meta):
        text = 'Select a domain for accessing the Inspired Platform:'
        options = [
            'dev-api.insprd.tech',
            'api.inspired.com',
            '(custom domain)',
        ]
        numbered = True

    def process_input(self):
        self.input = super(PlatformDomainPrompt, self).process_input()
        if self.input == 'dev-api.insprd.tech':
            self.input = 'fgdsawlhnb.execute-api.us-east-1.amazonaws.com/dev'
        elif self.input == 'api.inspired.com':
            raise NotImplemented('Not in production yet')
        elif self.input == '(custom domain)':
            self.input = CharacterPrompt(
                'Enter a custom domain for accessing the Inspired Platform:',
            ).input
        return self.input
