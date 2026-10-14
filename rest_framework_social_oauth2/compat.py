try:
    # social-auth-core < 6
    from social_core.exceptions import MissingBackend
except ImportError:
    # social-auth-core >= 6 raises AuthConfigurationError for unknown backends
    from social_core.exceptions import AuthConfigurationError as MissingBackend

__all__ = ['MissingBackend']
