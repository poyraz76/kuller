#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006,2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def install():
    # Executable
    pisitools.dodir("/usr/bin")
    shelltools.copy("asciidoc.py","%s/usr/bin/asciidoc" % get.installDIR())

    # Config
    pisitools.dodir("/etc/asciidoc")
    shelltools.copy("*.conf","%s/etc/asciidoc/" % get.installDIR())

    # Shared files
    pisitools.dodir("/usr/share/asciidoc")
    for dir in ["doc","docbook-xsl","examples","filters","images","stylesheets"]:
        shelltools.copy("%s" % dir ,"%s/usr/share/asciidoc/%s" % (get.installDIR(),dir))

    # Filters
    for filter in ["code-filter.conf","code-filter.py"]:
        pisitools.dosym("/usr/share/asciidoc/filters/%s" % filter, "/etc/asciidoc/filters/%s" % filter)

    # Stylesheets
    pisitools.dodir("/etc/asciidoc/stylesheets")
    shelltools.copy("stylesheets/*.css","%s/etc/asciidoc/stylesheets/" % get.installDIR())

    # vi support
    pisitools.insinto("/usr/share/vim/vim70/ftplugin","vim/ftdetect/*")
    pisitools.insinto("/usr/share/vim/vim70/syntax","vim/syntax/*")

    # Documentation
    pisitools.dodoc("BUGS","CHANGELOG","COPYING","README", "docbook-xsl/asciidoc-docbook-xsl.txt")
    pisitools.dohtml("doc/*html")
    pisitools.doman("doc/asciidoc.1")
