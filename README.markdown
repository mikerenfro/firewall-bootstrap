Mike Renfro's shell script and supporting files to bootstrap a 
firewall with debian-installer capabilities on a new Debian install.
Currently uses:

  * shorewall
  * maradns
  * isc-dhcp-server
  * tftpd-hpa

Installation:

  1. mkdir (target); cd (target)
  2. wget -O firewall-bootstrap.tgz https://github.com/mikerenfro/firewall-bootstrap/tarball/master
  3. tar --strip-components=1 -zxvpf firewall-bootstrap.tgz
  4. ./bootstrap
