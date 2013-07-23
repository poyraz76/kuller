#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools

def install():
    pythonmodules.install()

    # man files are copying to /usr/man/man1 directory
    pisitools.removeDir("/usr/man")

    pisitools.doman("scons.1", "sconsign.1", "scons-time.1")
    pisitools.dodoc("CHANGES*", "LICENSE*", "README*", "RELEASE*")