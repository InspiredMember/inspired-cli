import os
import sys

from cement import Controller, ex

from insprd.utils import rsa

from ..prompts.platform import PlatformDomainPrompt
from ..prompts.publisher import CreatePublisher
from ..utils import write_config_file, write_key_file


class Publisher(Controller):
    class Meta:
        label = 'publisher'
        description = 'Inspired Publisher Functions'
        stacked_on = 'base'
        stacked_type = 'nested'

    @ex(
        help='create new publisher account',
        arguments=[
        ],
    )
    def create(self):
        try:
            platform_domain = PlatformDomainPrompt().input
            publisher_name = CreatePublisher.NamePrompt().input
            publisher_id = None
            signing_key_id = CreatePublisher.SigningKeyIDPrompt().input
        except Exception as e:
            self.app.log.error(e)
            sys.exit(1)

        if publisher_id is None:
            publisher_id = 'abcdefgh12345678'

        pk = rsa.create_private_key()

        #TODO register new publisher with Inspired Platform

        write_key_file(signing_key_id, rsa.serialize_private_key(pk).decode('utf-8'))
        write_key_file(f'{signing_key_id}.pub', rsa.serialize_public_key(pk).decode('utf-8'))

        publishers = self.app.config.get_section_dict('insprd').get('publishers', {})

        publishers[publisher_name] = {
            'platform_domain': platform_domain,
            'publisher_id' : publisher_id,
            'signing_key_id': signing_key_id,
        }

        write_config_file('publishers', {'publishers': publishers}, 'publishers.jinja2')

        self.app.log.info(f'Created new Publisher "{publisher_name}"')
