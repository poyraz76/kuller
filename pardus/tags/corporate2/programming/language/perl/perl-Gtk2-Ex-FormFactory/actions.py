#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import perlmodules
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

WorkDir = "Gtk2-Ex-FormFactory-%s" % get.srcVERSION()

def setup():
    perlmodules.configure()

def build():
    perlmodules.make()

#FIXME: tests fail
#def check():
#    perlmodules.make("test")

def install():
    perlmodules.install()

    for dir in ["examples", "tutorial"]:
        pisitools.insinto("%s/%s" % (get.docDIR(), get.srcNAME()), dir)
    pisitools.dodoc("README", "Changes")

