#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "rt2500-cvs-%s" % get.srcVERSION().split("_", 1)[1]

def setup():
    pisitools.dosed("Module/Makefile", "\$\(shell uname -r\)", get.curKERNEL())
    pisitools.dosed("Module/Makefile", "\$\(shell uname -r", '$(shell echo %s' % get.curKERNEL())

def build():
    shelltools.export("BUILD_PARAMS", "-C /usr/src/linux-%s" % get.curKERNEL())
    shelltools.cd("Module")
    autotools.make("KERNDIR=/lib/modules/%s/build" % get.curKERNEL())

def install():
    pisitools.dodoc("Module/README", "Module/TESTING", "Module/iwpriv_usage.txt", "THANKS", "FAQ", "CHANGELOG")
    shelltools.cd("Module")
    pisitools.insinto("/lib/modules/%s/extra" % get.curKERNEL(), "*.ko")
    pisitools.insinto("/etc/Wireless/RT2500STA", "RT2500STA.dat")

