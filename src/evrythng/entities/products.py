"""
Evrything Docs
https://dashboard.evrythng.com/documentation/api/products
"""
from evrythng import assertions, utils

field_specs = {
    'datatypes': {
        'name': 'str',
        'description': 'str',
        'brand': 'str',
        'categories': 'list_of_str',
        'photos': 'list_of_str',
        'url': 'str',
        'identifiers': 'dict',
        'properties': 'dict',
        'tags': 'list_of_str',
        'customFields': 'dict',
        'scopes': 'dict',
        'type': 'str',
    },
    'required': ('name',),
    'readonly': ('id', 'createdAt', 'updatedAt', 'activatedAt'),
    'writable': ('description', 'brand', 'categories', 'photos', 'url',
                 'identifiers', 'properties', 'tags', 'customFields',
                 'scopes','type'),
}


def create_product_action(type_, product, timestamp=None, identifiers=None,
                          location=None, locationSource=None, context=None,
                          customFields=None, api_key=None, request_kwargs=None):
    """Create an Action for a Product."""
    kwargs = locals()
    del kwargs['request_kwargs']
    kwargs['type'] = kwargs['type_']
    del kwargs['type_']
    api_key = kwargs.pop('api_key', None)
    url = '/products/{}/actions/{}'.format(product, type_)
    return utils.request('POST', url, data=kwargs, api_key=api_key,
                         **(request_kwargs or {}))


def read_product_actions(product, type_, api_key=None, request_kwargs=None):
    """Read Actions for a Collection."""
    assertions.datatype_str('product', product)
    assertions.datatype_str('type_', type_)
    url = '/products/{}/actions/{}'.format(product, type_)
    return utils.request('GET', url, api_key=api_key, **(request_kwargs or {}))


def create_product(name, project_id=None, description=None, type=None, brand=None, categories=None,
                   photos=None, url=None, identifiers=None, properties=None,
                   tags=None, customFields=None, scopes=None, api_key=None,
                   request_kwargs=None):
    kwargs = locals()
    del kwargs['project_id']
    del kwargs['request_kwargs']
    api_key = kwargs.pop('api_key')
    assertions.validate_field_specs(kwargs, field_specs)
    proj = f'?project={project_id}' if project_id else ''
    return utils.request('POST', f'/products{proj}', data=kwargs, api_key=api_key,
                         **(request_kwargs or {}))


def list_products(api_key=None, request_kwargs=None):
    return utils.request('GET', '/products', api_key=api_key,
                         **(request_kwargs or {}))


def read_product(product, api_key=None, request_kwargs=None):
    assertions.datatype_str('product', product)
    url = '/products/{}'.format(product)
    return utils.request('GET', url, api_key=api_key,
                         **(request_kwargs or {}))


def update_product(product, name=None, description=None, type=None, brand=None,
                   categories=None, photos=None, url=None, identifiers=None,
                   properties=None, tags=None, customFields=None, scopes=None, api_key=None,
                   request_kwargs=None):
    kwargs = locals()
    del kwargs['request_kwargs']
    product = kwargs.pop('product')
    api_key = kwargs.pop('api_key')
    assertions.validate_field_specs(kwargs, field_specs)
    url = '/products/{}'.format(product)
    return utils.request('PUT', url, data=kwargs, api_key=api_key,
                         **(request_kwargs or {}))

def create_product_redirect(evrythngId, defaultRedirectUrl, base_url=None, api_key=None, type='product'):
    kwargs = locals()
    api_key = kwargs.pop('api_key')
    base_url = kwargs.pop('base_url')
    assertions.datatype_str('defaultRedirectUrl',defaultRedirectUrl)
    url = '/redirections'
    return utils.request('POST', url, base_url=base_url, data=kwargs, api_key=api_key)

def delete_product(product, api_key=None, request_kwargs=None):
    assertions.datatype_str('product', product)
    url = '/products/{}'.format(product)
    return utils.request('DELETE', url, api_key=api_key,
                         **(request_kwargs or {}))
