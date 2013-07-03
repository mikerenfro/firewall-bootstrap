Mike Renfro's shell script and supporting files to bootstrap a 
firewall with debian-installer capabilities on a new Debian install.
Currently uses:

  * shorewall
  * bind9
  * isc-dhcp-server
  * tftpd-hpa
  * openbsd-inetd and micro-httpd (for preseeded installs)

Assumptions:

  * Debian 7.1 (wheezy) installed with correct hostname and domain already
    set
  * eth0 is the Internet-facing interface, eth1 is the internal interface
  * DNS, DHCP, and PXE services will be offered via eth1
  * eth1 IP will default to 192.168.0.1 on network 192.168.0.0/24 (see step
    4 below if you need to change these defaults)

Installation:

  1. mkdir (target); cd (target)
  2. wget -O firewall-bootstrap.tgz https://github.com/mikerenfro/firewall-bootstrap/tarball/master
  3. tar --strip-components=1 -zxvpf firewall-bootstrap.tgz
  4. Edit support files as needed. bootstrap contains an upstream DNS entry,
     an IP range for DHCP leases, plus the IP address and CIDR netmask for
     eth1 (currently untested for values other than 24). mirror-netboot
     contains the URL to a Debian mirror.
  5. ./bootstrap

Post-installation:

  * Verify that PXE booting works on a system connected to eth1. You
    can configure this yourself, or else add an entry to
    /usr/local/lib/python2.7/dist-packages/system_database.py for the client
    system and re-run dns-regen and dhcp-regen.
  * By default, the bootstrap script will disable NAT. If you need to enable
    NAT, copy /etc/shorewall/masq.bak to /etc/shorewall/masq and restart
    shorewall.
  * The PXE boots default to 32-bit installations. If you want to change this
    to 64-bit installations,
    `cd /srv/tftp/pxelinux.cfg ; ln -sf debian-installer-amd64 default`
