try:
    from django.template.loaders import forms
    NEW_FORM_RENDERING = True
except ImportError:
    NEW_FORM_RENDERING = False


_loaders = [
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    ]


if NEW_FORM_RENDERING:
    _loaders += ['django.template.loaders.forms.Loader']


TEMPLATE_LOADERS = [
    ('django.template.loaders.cached.Loader', _loaders),
]
