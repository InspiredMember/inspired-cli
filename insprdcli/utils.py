import os


def ensure_config_dir():
    config_dir = get_config_dir()
    os.makedirs(config_dir, exist_ok=True)
    return config_dir


def ensure_keys_dir():
    keys_dir = get_keys_dir()
    os.makedirs(keys_dir, exist_ok=True)
    return keys_dir


def get_app():
    from .main import InsprdCLI
    app = InsprdCLI()
    app.setup()
    return app


def get_config_dir():
    config_dir = os.environ.get('INSPRD_CONFIG_DIR', '~/.insprd')
    return os.path.expanduser(config_dir)


def get_keys_dir():
    keys_dir = os.environ.get('INSPRD_KEYS_DIR')
    if keys_dir is None:
        keys_dir = os.path.join(get_config_dir(), '.keys')
    return os.path.expanduser(keys_dir)


def write_config_file(file_name, data, template):
    config_dir = ensure_config_dir()
    _write_file(os.path.join(config_dir, file_name), data, template)


def write_key_file(file_name, content):
    keys_dir = ensure_keys_dir()
    _write_file(os.path.join(keys_dir, file_name), {'content': content}, 'generic.jinja2')


def _write_file(file_path, data, template):
    app = get_app()
    with open(file_path, 'w') as f:
        app.render(data, template, out=f)
    app.log.info(f'Wrote file: {file_path}')
