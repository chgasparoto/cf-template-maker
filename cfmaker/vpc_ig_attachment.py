from cfmaker.resource import Resource


class VpcGatewayAttachment(Resource):
    props = {
        'VpcId': '',
        'InternetGatewayId': ''
    }

    def __init__(self, title, **kwargs):
        super().__init__('AWS::EC2::VPCGatewayAttachment', title, **kwargs)
