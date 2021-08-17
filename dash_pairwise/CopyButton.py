# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class CopyButton(Component):
    """A CopyButton component.
CopyButton is an button that when clicked copies text to the clipboard.
 It has an input value which is the content to be copied.
Additional properties of typical Dash components

Keyword arguments:
- children (list of a list of or a singular dash component, string or numbers | a list of or a singular dash component, string or number; optional): Array that holds components to render
- id (string; required): The ID used to identify this component in Dash callbacks.
- disabled (string | boolean; optional): Indicates wheather the user can interact with the element
- value (string; optional): The value to copy.
- n_clicks (number; default 0): Number of times the button has been clicked.
- n_clicks_timestamp (number; default -1): Last time the button was clicked.
- className (string; optional): Often used with CSS to style elements with common properties."""
    @_explicitize_args
    def __init__(self, children=None, id=Component.REQUIRED, disabled=Component.UNDEFINED, value=Component.UNDEFINED, n_clicks=Component.UNDEFINED, n_clicks_timestamp=Component.UNDEFINED, className=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'disabled', 'value', 'n_clicks', 'n_clicks_timestamp', 'className']
        self._type = 'CopyButton'
        self._namespace = 'dash_pairwise'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'disabled', 'value', 'n_clicks', 'n_clicks_timestamp', 'className']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in ['id']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(CopyButton, self).__init__(children=children, **args)
