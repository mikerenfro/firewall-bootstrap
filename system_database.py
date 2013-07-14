# Common database of hostnames, IPs, and MAC addresses for DHCP, DNS,
# and other tools.

DEFAULT_DOMAIN = '__DOMAIN__'
LOC_NETWORK = '__LOC_NETWORK__'
LOC_NETWORK_PREFIX = '__LOC_NETWORK_PREFIX__'
LOC_NETMASK_SHORT = '__LOC_NETMASK_SHORT__'
DMZ_NETWORK = '__DMZ_NETWORK__'
DMZ_NETWORK_PREFIX = '__DMZ_NETWORK_PREFIX__'
DMZ_NETMASK_SHORT = '__DMZ_NETMASK_SHORT__'

SYSTEM_DATABASE_LOC = [
    { 'host':    '__HOSTNAME__',
      'mac':     '__ETH1_MAC__',
      'ip':      '__ETH1_IP__',
      },
    ]

SYSTEM_DATABASE_DMZ = [
    { 'host':    '__HOSTNAME__-dmz',
      'mac':     '__ETH2_MAC__',
      'ip':      '__ETH2_IP__',
      'aliases': ('ns1',),
      },
    ]
