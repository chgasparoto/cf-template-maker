def Tag(name, value):
    return { 'Key': name, 'Value': value }

def Ref(resource):
    return { 'Ref': resource.title }

class Resource:
    def __init__(self, res_type, title, **kwargs):
        self.type = res_type
        self.title = title
        self.properties = kwargs

    def set_property(self, name, prop):
        self.properties[name] = prop

    def set_title(self, title):
        self.title = title

    def render(self):
        d = {}
        d['Type'] = self.type
        d['Properties'] = {}
        d['Properties'] = self.properties

        return d
