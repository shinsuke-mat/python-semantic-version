import re


class Version():
    version_reg_num = r'0|[1-9]\d*'
    version_reg = \
        re.compile(r'^({0})\.({0})\.({0})$'.format(version_reg_num))

    def __init__(self, version_str):
        match = self.version_reg.match(version_str)
        if not match:
            raise ValueError

        self.major = int(match.groups()[0])
        self.minor = int(match.groups()[1])
        self.patch = int(match.groups()[2])
