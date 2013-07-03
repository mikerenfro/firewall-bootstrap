# Common database of hostnames, IPs, and MAC addresses for DHCP, DNS,
# and other tools.

DEFAULT_DOMAIN = '__DOMAIN__'
DEFAULT_NETWORK = '__NETWORK__'
DEFAULT_NETWORK_PREFIX = '__NETWORK_PREFIX__'
DEFAULT_NETMASK_SHORT = '__NETMASK_SHORT__'

SYSTEM_DATABASE = [
    { 'host':    '__HOSTNAME__',
      'mac':     '__ETH1_MAC__',
      'ip':      '__ETH1_IP__',
      'aliases': ('ns1',),
      },
    ]
