#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="qgit"

def setup():
    shelltools.system("qmake-qt4")

def build():
    autotools.make("CXXFLAGS='%s' LFLAGS='%s'" % (get.CXXFLAGS(), get.LDFLAGS()))

def install():
    autotools.rawInstall("INSTALL_ROOT=%s" % get.installDIR())

    pisitools.insinto("/usr/share/pixmaps", "src/resources/qgit.png")

    pisitools.dodoc("README")
