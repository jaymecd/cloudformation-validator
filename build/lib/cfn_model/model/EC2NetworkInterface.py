from cfn_model import ModelElement

class EC2NetworkInterface(ModelElement):

    def __init__(self, cfn_model):
        '''
        Initialize
        :param cfn_model: 
        '''
        ModelElement.__init__(self, cfn_model)

        self.groupSet= []
        self.ipv6Addresses= []
        self.privateIpAddresses= []
        self.tags= []
        self.security_groups= []
        self.resource_type = 'AWS::EC2::NetworkInterface'


