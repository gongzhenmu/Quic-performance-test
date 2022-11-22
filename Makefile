############################################################################
##
##     This file is part of Purdue CS 536.
##
##     Purdue CS 536 is free software: you can redistribute it and/or modify
##     it under the terms of the GNU General Public License as published by
##     the Free Software Foundation, either version 3 of the License, or
##     (at your option) any later version.
##
##     Purdue CS 536 is distributed in the hope that it will be useful,
##     but WITHOUT ANY WARRANTY; without even the implied warranty of
##     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##     GNU General Public License for more details.
##
##     You should have received a copy of the GNU General Public License
##     along with Purdue CS 536. If not, see <https://www.gnu.org/licenses/>.
##
#############################################################################

####################################################################
############### Set up Mininet and Controller ######################
####################################################################

SCRIPTS = scripts

.PHONY: mininet controller cli netcfg host-h1 host-h2

mininet:
	$(SCRIPTS)/mn-stratum

mininet-india:
	$(SCRIPTS)/mn-stratum --link=tc,bw=10,delay=500ms

mininet-germany:
	$(SCRIPTS)/mn-stratum --link=tc,bw=500,delay=10ms

mininet-prereqs:
	docker exec -it mn-stratum bash -c \
		"apt-get update ; \
		 apt-get -y --allow-unauthenticated install iptables python-scapy ; \
		 apt-get install python3-pip"

	$(SCRIPTS)/utils/mn-stratum/exec-script h1 \
		"iptables -A OUTPUT -p tcp --tcp-flags RST RST -j DROP"
	$(SCRIPTS)/utils/mn-stratum/exec-script h2 \
		"iptables -A OUTPUT -p tcp --tcp-flags RST RST -j DROP"

controller:
	ONOS_APPS=gui,proxyarp,drivers.bmv2,lldpprovider,hostprovider,fwd \
	$(SCRIPTS)/onos

cli:
	$(SCRIPTS)/onos-cli

netcfg:
	$(SCRIPTS)/onos-netcfg cfg/netcfg.json

host-h1:
	$(SCRIPTS)/utils/mn-stratum/exec h1

host-h2:
	$(SCRIPTS)/utils/mn-stratum/exec h2
