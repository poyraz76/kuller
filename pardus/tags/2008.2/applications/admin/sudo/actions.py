#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2007  TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="sudo-%s" % get.srcVERSION().replace("_","")

def setup():
    shelltools.export("CFLAGS", "%s -Wall -fpie -DLDAP_DEPRECATED" % get.CFLAGS())
    shelltools.export("LDFLAGS","%s -pie" % get.LDFLAGS())

    autotools.configure("--libexecdir=/usr/libexec/sudo \
                         --with-noexec=/usr/libexec/sudo/sudo_noexec.so \
                         --with-logfac=auth \
                         --with-insults \
                         --with-all-insults \
                         --with-ignore-dot \
                         --with-tty-tickets \
                         --enable-shell-sets-home \
                         --with-sudoers-mode=0440 \
                         --with-pam \
                         --with-ldap \
                         --with-env-editor \
                         --without-secure-path")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # for LDAP
    pisitools.dobin("sudoers2ldif")

    pisitools.domo("tr.po","tr", "sudo.mo")

    pisitools.dodoc("BUGS", "CHANGES", "README", "TROUBLESHOOTING")
