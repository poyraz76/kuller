#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2011 TUBITAK/BILGEM
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.configure()

    pisitools.dosed("src/Makefile", "-ldl", "")
    pisitools.dosed("src/Makefile", "-lsvn_repos-1", "")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc("COPYING", "README", "AUTHORS", "ChangeLog")
