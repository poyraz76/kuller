#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.rawConfigure("--prefix=/usr")

def build():
    autotools.make()

def install():
    autotools.rawInstall("dstdir=%s/usr/share slnkdir=%s/usr/bin" % (get.installDIR(),get.installDIR()))

    pisitools.removeDir("/usr/share/pixmaps/")
    pisitools.insinto("/usr/share/pixmaps/","desktop-icons/128x128/apps/amsn.png")

    pisitools.removeDir("/usr/share/amsn/plugins/winflash")
    pisitools.removeDir("/usr/share/amsn/plugins/QuickTimeTcl3.1")
    pisitools.removeDir("/usr/share/amsn/plugins/applescript")
    pisitools.removeDir("/usr/share/amsn/plugins/tclCarbonNotification")
    pisitools.removeDir("/usr/share/amsn/plugins/tclAE2.0")
    pisitools.removeDir("/usr/share/amsn/utils/macosx")
    pisitools.removeDir("/usr/share/amsn/desktop-icons")
    pisitools.removeDir("/usr/share/amsn/utils/tcl_siren/src")
    pisitools.remove("/usr/share/amsn/utils/linux/capture/libng/libng.a")
    pisitools.remove("/usr/share/amsn/utils/TkCximage/src/CxImage/libCxImage.a")
    pisitools.remove("/usr/share/amsn/utils/webcamsn/src/libmimic.a")

    # Default browser firefox
    pisitools.dosed("%s/usr/share/amsn/config.tcl" % get.installDIR(), "mozilla", "firefox");

    # Default file browser konqueror
    pisitools.dosed("%s/usr/share/amsn/config.tcl" % get.installDIR(), "my_filemanager open", "konqueror");

    pisitools.removeDir("/usr/share/amsn/docs")
    pisitools.dodoc("CREDITS","GNUGPL","HELP","README","TODO")
