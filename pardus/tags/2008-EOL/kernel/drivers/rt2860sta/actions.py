#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt
#

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "2008_0918_RT2860_Linux_STA_v1.8.0.0"

def build():
    autotools.make()

def install():
    pisitools.insinto("/lib/modules/%s/extra/" % get.curKERNEL(), "os/linux/rt2860sta.ko")
    pisitools.dodoc("README_STA", "iwpriv_usage.txt")
    pisitools.newdoc("RT2860STA.dat", "RT2860STA.dat.example")
