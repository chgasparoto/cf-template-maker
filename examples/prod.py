import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

from cfmaker import Template
from cfmaker.resource import Resource, Tag, Ref
from cfmaker.vpc import Vpc
from cfmaker.internet_gateway import InternetGateway
from cfmaker.vpc_ig_attachment import VpcGatewayAttachment
from cfmaker.nacl import Nacl, NaclEntry

t = Template()
t.set_description('Service VPC')

vpc = Vpc('VPC',
    CidrBlock='10.0.0.0/16',
    EnableDnsHostnames='true',
    EnableDnsSupport='true',
    InstanceTenancy='default',
    Tags=[Tag('Environment', 'Production'), Tag('Name', 'Production-ServiceVPC')]
)

ig = InternetGateway('InternetGateway',
    Tags=[Tag('Environment', 'Production'), Tag('Name', 'Production-InternetGateway')]
)

vpc_ig_attachment = VpcGatewayAttachment('VpcGatewayAttachment',
    InternetGatewayId=Ref(ig),
    VpcId=Ref(vpc)
)

nacl = Nacl('VpcNetworkAcl',
    VpcId=Ref(vpc),
    Tags=[Tag('Environment', 'Production'), Tag('Name', 'Production-NetworkAcl')]
)
inbound_rule = NaclEntry('VpcNetworkAclInboundRule',
    CidrBlock='0.0.0.0/0',
    Egress='false',
    NetworkAclId=Ref(nacl),
    PortRange=dict(From='443', To='443'),
    Protocol='6',
    RuleAction='allow',
    RuleNumber=100
)
outbound_rule = NaclEntry('VpcNetworkAclOutboundRule',
    CidrBlock='0.0.0.0/0',
    Egress='true',
    NetworkAclId=Ref(nacl),
    Protocol='6',
    RuleAction='allow',
    RuleNumber=200
)

# Add resources
t.add_resource(vpc)
t.add_resource(ig)
t.add_resource(vpc_ig_attachment)
t.add_resource(nacl)
t.add_resource(inbound_rule)
t.add_resource(outbound_rule)

# Add metadatas
t.add_metadata('DependsOn', [])
t.add_metadata('Environment', 'Production')
t.add_metadata('StackName', 'Production-VPC')

# Add outputs
t.add_output('InternetGateway', ig)
t.add_output('VPCID', vpc)

# Generates CF template
print(t.to_json())
