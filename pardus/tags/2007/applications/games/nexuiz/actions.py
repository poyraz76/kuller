#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get 

# we get sources from the release zipfile

def setup():
    pisitools.dosed("darkplaces/makefile.inc", "pardusFLAGS", get.CFLAGS())

def build():
    shelltools.cd("darkplaces")
    for f in ["cl-nexuiz", "sdl-nexuiz", "sv-nexuiz"]:
        autotools.make("%s DP_FS_BASEDIR=/usr/share/quake1" % f)

def install():
    for f in ["nexuiz-glx", "nexuiz-sdl", "nexuiz-dedicated"]:
        pisitools.dobin("darkplaces/%s" % f)

    pisitools.dosym("nexuiz-sdl", "/usr/bin/nexuiz")

