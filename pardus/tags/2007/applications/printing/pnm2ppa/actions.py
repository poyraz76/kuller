#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    pass

def build():
    shelltools.export("CFLAGS", "-DNDEBUG %s" % get.CFLAGS())

    autotools.make('CFLAGS="%s -DLANG_EN"' % get.CFLAGS())

    shelltools.cd("ppa_protocol")
    autotools.make('CFLAGS="%s"' % get.CFLAGS())

def install():
    autotools.rawInstall("BINDIR=%(install)s/usr/bin \
                          CONFDIR=%(install)s/etc    \
                          MANDIR=%(install)s/usr/share/man/man1" % { "install": get.installDIR()})

    pisitools.dobin("utils/Linux/detect_ppa utils/Linux/test_ppa")

    pisitools.insinto("/usr/share/pnm2ppa/lpd", "lpd/*")
    pisitools.insinto("/usr/share/pnm2ppa/pdq", "pdq/*")
    pisitools.doexe("lpd/lpdsetup", "/usr/share/pnm2ppa/lpd")
    pisitools.doexe("sample_scripts/*", "/usr/share/pnm2ppa/sample_scripts")

    pisitools.doexe("pdq/gs-pnm2ppa", "/etc/pdq/drivers/ghostscript")
    pisitools.doexe("pdq/dummy", "/etc/pdq/interfaces")

    pisitools.dohtml("*")

    shelltools.cd("docs/en")
    pisitools.dodoc("CALIBRATION*txt", "COLOR*txt", "PPA*txt", "RELEASE*", "CREDITS", "INSTALL", "LICENSE", "README", "TODO", "sgml/*.sgml")

