#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (c) TUBITAK / UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "nice-%s" % get.srcVERSION()

def setup():
    autotools.configure("--disable-static \
                         --with-gstreamer \
                         --with-html-dir=/%s/%s/html"
                         % (get.docDIR(), get.srcTAG()))

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "COPYING*", "NEWS", "README")