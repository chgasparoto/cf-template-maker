import json

def encode_to_dict(obj):
    if hasattr(obj, 'to_dict'):
        # Calling encode_to_dict to ensure object is
        # nomalized to a base dictionary all the way down.
        return encode_to_dict(obj.to_dict())
    elif isinstance(obj, (list, tuple)):
        new_lst = []
        for o in list(obj):
            new_lst.append(encode_to_dict(o))
        return new_lst
    elif isinstance(obj, dict):
        props = {}
        for name, prop in obj.items():
            props[name] = encode_to_dict(prop)

        return props
    # This is useful when dealing with external libs using
    # this format. Specifically awacs.
    elif hasattr(obj, 'JSONrepr'):
        return encode_to_dict(obj.JSONrepr())
    return obj

class Template:
    def __init__(self, version=None):
        self.version = version or '2010-09-09'
        self.description = 'Generated by python'
        self.outputs = {}
        self.resources = {}
        self.metadata = {}

    def set_description(self, desc):
        self.description = desc

    def add_resource(self, resource):
        if resource.title in self.resources:
            self.handle_duplicate_key(resource.title)
        self.resources[resource.title] = resource.render()

    def add_metadata(self, name, value):
        self.metadata[name] = value

    def add_output(self, name, resource):
        d = {}
        d['Value'] = {}
        d['Value']['Ref'] = resource.title
        self.outputs[name] = d

    def to_json(self, indent=4, sort_keys=True, separators=(',', ': ')):
        return json.dumps(self.to_dict(), indent=indent,
                          sort_keys=sort_keys, separators=separators)

    def to_dict(self):
        t = {}
        if self.description:
            t['Description'] = self.description
        if self.metadata:
            t['Metadata'] = self.metadata
        if self.outputs:
            t['Outputs'] = self.outputs
        if self.version:
            t['AWSTemplateFormatVersion'] = self.version
        t['Resources'] = self.resources

        return encode_to_dict(t)

    def handle_duplicate_key(self, key):
        raise ValueError('duplicate key "%s" detected' % key)