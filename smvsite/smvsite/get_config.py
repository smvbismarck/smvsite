from os import environ


class ConfigError(Exception):
    pass


def get_env_config(env_var, default=None):
    try:
        env_config = environ[env_var]
    except KeyError:
        if default is not None:
            env_config = default
        else:
            raise ConfigError("Please specify the", env_var, "as enviroment variable")
    return env_config
