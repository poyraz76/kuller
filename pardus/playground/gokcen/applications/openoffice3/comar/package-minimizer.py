#!/usr/bin/python

import os

unopkg = "/opt/OpenOffice.org/bin/unopkg"
extPath = "/opt/OpenOffice.org/lib/ooo-3.1/share/extension/install"
extName = "sun-presentation-minimizer"

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system("%s add --shared --force %s/%s.oxt" % (unopkg, extPath, extName))

def preRemove():
    os.system("%s remove --shared %s" % (unopkg, extName))
