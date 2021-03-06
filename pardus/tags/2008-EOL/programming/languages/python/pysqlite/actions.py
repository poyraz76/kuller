#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# (C) TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def install():
    pythonmodules.install()

    pisitools.rename("/usr/share/doc/pysqlite2-doc",get.srcTAG())

    pisitools.dodoc("LICENSE", "PKG-INFO", "doc/*")
