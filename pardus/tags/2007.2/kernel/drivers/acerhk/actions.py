#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

NoStrip = "/"

def build():
    autotools.make()

def install():
    pisitools.doexe("acerhk.ko", "/lib/modules/%s/acerhk/" % get.curKERNEL())
    pisitools.dodoc("README", "COPYING", "NEWS", "doc/*")
