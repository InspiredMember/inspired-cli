from .base import CharacterPrompt


OPT_CUSTOM = '(custom domain)'
OPT_DEV = 'dev (platform-v1.insprd.tech)'
OPT_PROD = 'prod (not implemented yet)'


class PlatformDomainPrompt(CharacterPrompt):
    class Meta(CharacterPrompt.Meta):
        text = 'Select a domain for accessing the Inspired Platform:'
        options = [
            OPT_DEV,
            OPT_PROD,
            OPT_CUSTOM,
        ]
        numbered = True

    def process_input(self):
        self.input = super(PlatformDomainPrompt, self).process_input()
        if self.input == OPT_DEV:
            self.input = 'platform-v1.insprd.tech'
        elif self.input == OPT_PROD:
            raise NotImplemented('Not implemented yet')
        elif self.input == OPT_CUSTOM:
            self.input = CharacterPrompt(
                'Enter a custom domain for accessing the Inspired Platform:',
            ).input
        return self.input
