#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "ralink-firmware"
NoStrip = "/"

firmwareDir = "/lib/firmware"

def install():
    for f in shelltools.ls("./"):
        pisitools.insinto(firmwareDir, f)

