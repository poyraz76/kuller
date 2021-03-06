#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import perlmodules
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import get

WorkDir="Font-TTF-%s" % get.srcVERSION()

def setup():
    for d in ("COPYING", "README.TXT", "TODO", "Changes"):
        shelltools.chmod(d, 0644)

    perlmodules.configure()

def build():
    perlmodules.make()

def check():
    autotools.make("test")

def install():
    perlmodules.install()

    pisitools.removeDir("/usr/lib/perl5/%s" % get.curPERL())

    pisitools.dodoc("COPYING", "README*", "TODO", "Changes")
