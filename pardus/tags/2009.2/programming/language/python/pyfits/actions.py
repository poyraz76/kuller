#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

tests = "%s/%s/test" % (get.docDIR(), get.srcNAME())

def build():
    pythonmodules.compile()

def install():
    pythonmodules.install()

    shelltools.chmod("test/*", 0644)
    pisitools.insinto(tests, "test/*")
