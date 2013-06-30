Mike Renfro's shell script and supporting files to bootstrap a 
firewall with debian-installer capabilities on a new Debian install.
Currently uses:

  * shorewall
  * bind9
  * isc-dhcp-server
  * tftpd-hpa

Assumptions:

  * Debian installed with correct hostname and domain already set
  * eth0 is the Internet-facing interface, eth1 is the internal interface
  * DNS, DHCP, and PXE services will be offered via eth1
  * eth1 IP will default to 192.168.0.1, netmask 255.255.255.0 (see step 4
    below if you need to change these defaults)

Installation:

  1. mkdir (target); cd (target)
  2. wget -O firewall-bootstrap.tgz https://github.com/mikerenfro/firewall-bootstrap/tarball/wheezy/bind
  3. tar --strip-components=1 -zxvpf firewall-bootstrap.tgz
  4. Edit support files as needed. bootstrap contains an upstream DNS entry,
     an IP range for DHCP leases, plus the IP address, netmask, network, and
     broadcast address for eth1. mirror-netboot contains the URL to a Debian
     mirror.
  5. ./bootstrap

Post-installation:

  * Verify that PXE booting works on a system connected to eth1. You
    can configure this yourself, or else add an entry to
    /usr/local/lib/python2.7/dist-packages/system_database.py for the client
    system and re-run dns-regen and dhcp-regen.
  * The PXE boots default to 32-bit installations. If you want to change this
    to 64-bit installations,
    `cd /srv/tftp/pxelinux.cfg ; ln -sf debian-installer-amd64 default`
