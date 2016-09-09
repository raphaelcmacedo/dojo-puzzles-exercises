class Url(object):

    def __init__(self, protocol = '', host = '', domain = '', path = '', parameters = '', user = '', password = ''):
        self.protocol = protocol
        self.host = host
        self.domain = domain
        self.path = path
        self.parameters = parameters
        self.user = user
        self.password = password

    def __eq__(self, other):
        return (isinstance(other, self.__class__)
                and self.__dict__ == other.__dict__)

    def __ne__(self, other):
        return not self.__eq__(other)


