#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "pardus"
datadir = "/usr/share/gfxtheme/pardus"

def build():
    autotools.make('PRODUCT="Pardus 2009.1"')

def install():
    pisitools.insinto(datadir, "bootlogo.dir", "install")
    pisitools.insinto(datadir, "message.dir", "boot")

