#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006,2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="metis-4.0"

def build():
    autotools.make()

def install():
    pisitools.insinto("/usr/lib", "libmetis.so*")

    for header in ["metis.h","defs.h","struct.h","macros.h","rename.h","proto.h"]:
        shelltools.chmod("Lib/%s" % header, 0644)
        pisitools.insinto("/usr/include/metis","Lib/%s" % header)

    pisitools.dodoc("CHANGES")
