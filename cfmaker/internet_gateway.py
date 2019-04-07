from cfmaker.resource import Resource

class InternetGateway(Resource):
    props = {
        'Tags': list
    }

    def __init__(self, title, **kwargs):
        super().__init__('AWS::EC2::InternetGateway', title, **kwargs)
