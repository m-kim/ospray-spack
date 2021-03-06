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
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install ispc
#
# You can edit this file again by typing:
#
#     spack edit ispc
#
# See the Spack documentation for more information on packaging.
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
from spack import *
from llnl.util.filesystem import mkdirp, join_path, touch, ancestor
from llnl.util.filesystem import working_dir, install_tree, install
import os

class Ispc(Package):
    """FIXME: Put a proper description of your package here."""

    homepage = "https://ispc.github.io/"
    url      = "https://github.com/ispc"
    # version('1.9.2', git='https://github.com/ispc/ispc.git', tag='v1.9.2')
    # depends_on('llvm+clang@5.0.1', type=('build', 'link'))

    version('1.9.1', git='https://github.com/ispc/ispc.git', tag='v1.9.1')
    depends_on('llvm+clang@3.9.0', type=('build', 'link'))

    
    def install(self, spec, prefix):
        make("gcc")
        #sanity_check_prefix looks for directories other than .spack to confirm
        #install is complete
        print(self.stage.source_path)
        mkdirp(prefix.bin)
        os.rename(join_path(self.stage.source_path, self.name), join_path(prefix.bin , self.name))
        
    def setup_environment(self, spack_env, run_env):
        run_env.prepend_path('ISPC_HOME',self.prefix)
