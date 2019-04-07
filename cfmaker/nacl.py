from cfmaker.resource import Resource

class Nacl(Resource):
    props = {
        'VpcId': '',
        'Tags': list
    }

    def __init__(self, title, **kwargs):
        super().__init__('AWS::EC2::NetworkAcl', title, **kwargs)


class NaclEntry(Resource):
    props = {
        'CidrBlock': '',
        'Egress': '',
        'NetworkAclId': '',
        'PortRange': dict,
        'Protocol': '',
        'RuleAction': '',
        'RuleNumber': 0
    }

    def __init__(self, title, **kwargs):
        super().__init__('AWS::EC2::NetworkAclEntry', title, **kwargs)
