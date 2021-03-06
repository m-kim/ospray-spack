##############################################################################
# Copyright (c) 2013-2017, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/spack/spack
# Please also see the NOTICE and LICENSE files for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################
from spack import *
import os.path


class Extension2(Package):
    """A package which extends another package. It also depends on another
       package which extends the same package."""

    homepage = "http://www.example.com"
    url      = "http://www.example.com/extension2-1.0.tar.gz"

    extends('extendee')
    depends_on('extension1', type=('build', 'run'))

    version('1.0', 'hash-extension2-1.0')

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        with open(os.path.join(prefix.bin, 'extension2'), 'w+') as fout:
            fout.write(str(spec.version))
