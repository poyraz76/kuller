#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import get

WorkDir = "python-xlib-0.14rc1"

examples = "%s/%s/examples" % (get.docDIR(), get.srcTAG())
utils = "%s/%s/utils" % (get.docDIR(), get.srcTAG())

def setup():
    shelltools.chmod("examples/*", 0644)
    shelltools.chmod("utils/*", 0644)

def build():
    pythonmodules.compile()

    # we need texi to create ps
    # for d in ["doc/html", "doc/info", "doc/ps"]:
    for d in ["doc/html", "doc/info"]:
        shelltools.cd(d)
        autotools.make()
        shelltools.cd("../..")

def install():
    pythonmodules.install()

    pisitools.dohtml("doc/html/")
    pisitools.dodoc("doc/ps/python-xlib.ps", "TODO", "COPYING", "NEWS", "README")
    pisitools.doinfo("doc/info/*.info*")

    pisitools.insinto(examples, "examples/*")
    pisitools.insinto(utils, "utils/*")

    pythonmodules.fixCompiledPy()
