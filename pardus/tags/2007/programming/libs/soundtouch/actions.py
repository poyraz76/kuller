#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005, 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "soundtouch-1.3.1"

def setup():
    autotools.configure("--disable-integer-samples \
                         --with-pic")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s pkgdocdir=/usr/share/doc/%s" % (get.installDIR(), get.srcTAG()))
