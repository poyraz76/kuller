#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir="tcl8.5b2/unix"

def setup():
    autotools.configure("--with-encoding=utf-8 \
                         --enable-threads \
                         --enable-man-compression=gzip \
                         --enable-man-symlinks \
                         --enable-64bit")

def build():
    autotools.make()

def install():
    shelltools.system("make DESTDIR=%s install" % get.installDIR())

    # Collect private headers, 3rd party apps like Tile depends on this
    shelltools.cd("..")
    pisitools.dodir("/usr/include/tcl-private/generic")
    pisitools.dodir("/usr/include/tcl-private/unix")
    shelltools.copy("unix/*.h","%s/usr/include/tcl-private/unix" % get.installDIR())
    shelltools.copy("generic/*.h", "%s/usr/include/tcl-private/generic" % get.installDIR())

    # Remove duplicated headers
    pisitools.remove("/usr/include/tcl-private/generic/tcl.h")
    pisitools.remove("/usr/include/tcl-private/generic/tclDecls.h")
    pisitools.remove("/usr/include/tcl-private/generic/tclPlatDecls.h")

    # Expect package needs these symlinks
    pisitools.dosym("/usr/include/tcl-private/unix/tclUnixPort.h","/usr/include/tcl-private/generic/tclUnixPort.h")
    pisitools.dosym("/usr/include/tcl-private/unix/tclUnixThrd.h","/usr/include/tcl-private/generic/tclUnixThrd.h")

    # Remove tmp path from tclConfig.sh
    pisitools.dosed("%s/usr/lib/tclConfig.sh" % get.installDIR(),"%s/unix" % get.curDIR() ,"/usr/lib/")
    pisitools.dosed("%s/usr/lib/tclConfig.sh" % get.installDIR(),"%s" % get.curDIR() ,"/usr/include/tcl-private")

    # Some apps need compat headers
    pisitools.dodir("/usr/include/tcl-private/compat")
    shelltools.copy("compat/*.h", "%s/usr/include/tcl-private/compat" % get.installDIR())

    pisitools.dosym("/usr/bin/tclsh8.5","/usr/bin/tclsh")
