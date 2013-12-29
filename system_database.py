# Common database of hostnames, IPs, and MAC addresses for DHCP, DNS,
# and other tools.

DEFAULT_DOMAIN = '__DOMAIN__'
NETWORK = '__ETH1_NETWORK__'
NETWORK_PREFIX = '__ETH1_NETWORK_PREFIX__'
NETMASK_SHORT = '__ETH1_NETMASK_SHORT__'

SYSTEM_DATABASE = [
    { 'host':    '__HOSTNAME__',
      'mac':     '__ETH1_MAC__',
      'ip':      '__ETH1_IP__',
      'aliases': ('ns1',),
      },
    ]
