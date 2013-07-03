#!/usr/bin/env python

import netaddr, sys

if sys.argv[1]=='network':
    print str(netaddr.IPNetwork(sys.argv[2]).network)
elif sys.argv[1]=='netmask':
    print str(netaddr.IPNetwork(sys.argv[2]).netmask)
elif sys.argv[1]=='broadcast':
    print str(netaddr.IPNetwork(sys.argv[2]).broadcast)
else:
    raise NameError('Invalid argument')
