#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def build():
    autotools.make('CC="%s" CFLAGS="%s"' % (get.CC(),get.CFLAGS()))
    autotools.make()

def install():
    pisitools.doexe("traceroute/traceroute", "/bin/")
    pisitools.dosym("/bin/traceroute", "/bin/tracert")

    pisitools.doman("traceroute/traceroute.8")
    pisitools.dodoc("ChangeLog", "COPYING", "CREDITS", "README", "TODO")
