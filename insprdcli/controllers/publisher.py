import os
import sys

from cement import Controller, ex

from insprd.client import PublisherClient
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
            publisher_email = CreatePublisher.EmailPrompt().input
            signing_key_id = CreatePublisher.SigningKeyIDPrompt().input
        except Exception as e:
            self.app.log.error(e)
            sys.exit(1)

        pk = rsa.create_private_key()

        #TODO register new publisher with Inspired Platform
        client = PublisherClient(
            platform_domain,
            signing_key_data=rsa.serialize_private_key(pk),
            signing_key_id=signing_key_id,
        )

        try:
            response = client.create(publisher_name, publisher_email)
        except Exception as e:
            self.app.log.error(e)
            sys.exit(1)
        else:
            self.app.log.info(response)

        write_key_file(signing_key_id, rsa.serialize_private_key(pk).decode('utf-8'))
        write_key_file(f'{signing_key_id}.pub', rsa.serialize_public_key(pk).decode('utf-8'))

        publishers = self.app.config.get_section_dict('insprd').get('publishers', {})

        publishers[publisher_name] = {
            'platform_domain': platform_domain,
            'publisher_id' : response.get('id'),
            'signing_key_id': signing_key_id,
        }

        write_config_file('publishers', {'publishers': publishers}, 'publishers.jinja2')

        self.app.log.info(f'Created new Publisher "{publisher_name}"')
