from cfmaker.resource import Resource

class Vpc(Resource):
    props = {
        'CidrBlock': '',
        'EnableDnsHostnames': True,
        'EnableDnsSupport': True,
        'InstanceTenancy': 'default',
        'Tags': list
    }

    def __init__(self, title, **kwargs):
        super().__init__('AWS::EC2::VPC', title, **kwargs)
