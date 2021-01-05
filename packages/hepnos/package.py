##############################################################################
# Copyright (c) 2013-2017, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/llnl/spack
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


class Hepnos(CMakePackage):
    """Object store for High Energy Physics, build around Mochi components"""

    homepage = "https://xgitlab.cels.anl.gov/sds/hep/HEPnOS"
    url = "https://xgitlab.cels.anl.gov/sds/hep/HEPnOS"
    git = 'https://xgitlab.cels.anl.gov/sds/hep/HEPnOS.git'

    version('0.4.0', tag='v0.4.0')
    version('0.3.2', tag='v0.3.2')
    version('0.3.1', tag='v0.3.1')
    version('0.3.0', tag='v0.3.0')
    version('0.2.0', tag='v0.2.0')
    version('0.1.8', tag='v0.1.8')
    version('0.1.7', tag='v0.1.7')
    version('0.1.6', tag='v0.1.6')
    version('0.1.5', tag='v0.1.5')
    version('0.1.4', tag='v0.1.4')
    version('0.1.3', tag='v0.1.3')
    version('0.1.2', tag='v0.1.2')
    version('0.1.1', tag='v0.1.1')
    version('0.1',   tag='v0.1')
    version('develop', branch='master')
    version('master', branch='master')

    depends_on('mpi')
    depends_on('yaml-cpp@develop')
    depends_on('boost+serialization')
    depends_on('cmake@3.12.0:')
    depends_on('libuuid', when='@0.2.0:')
    # Mochi dependencies for non-develop versions
    depends_on('mochi-ch-placement@0.1:')
    depends_on('mochi-thallium@0.5.2:', when='@0.2.0:')
    depends_on('mochi-margo@0.5.2:', when='@0.1.8') # past 0.1.8, HEPnOS requires thallium
    depends_on('mochi-sdskv@0.1.9:', when='@0.3.1:')
    depends_on('mochi-sdskv@0.1.8:', when='@0.2.0:')
    depends_on('mochi-sdskv@0.1.7:', when='@0.1.8:')
    depends_on('mochi-sdskv@0.1:')
    depends_on('mochi-bake@0.1:0.3.6', when='@:0.1.7') # after 0.1.7, HEPnOS does not require bake
    # Mochi dependencies for develop version
    depends_on('mochi-ch-placement@develop', when='@develop')
    depends_on('mochi-thallium@develop', when='@develop')
    depends_on('mochi-sdskv@develop', when='@develop')

    def cmake_args(self):
        extra_args = ['-DBUILD_SHARED_LIBS=ON']
        extra_args.extend(['-DCMAKE_CXX_COMPILER=%s' % self.spec['mpi'].mpicxx])
        return extra_args
