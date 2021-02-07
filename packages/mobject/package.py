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


class Mobject(AutotoolsPackage):
    """A Mochi microservice object store built on Margo, sds-keyval, and other components"""

    homepage = "https://xgitlab.cels.anl.gov/sds/mobject-store"
    url = "https://xgitlab.cels.anl.gov/sds/mobject-store"
    #git = 'https://xgitlab.cels.anl.gov/sds/mobject-store.git'
    git = 'https://github.com/srini009/mobject-store.git'

    version('0.4.2', tag='v0.4.2')
    version('0.4.1', tag='v0.4.1')
    version('0.4', tag='v0.4')
    version('0.3', tag='v0.3')
    version('0.2', tag='v0.2')
    version('0.1', tag='v0.1')
    version('develop', branch='master')
    version('master', branch='master')

    variant('timing', default=False, description="crude timing information")

    depends_on('mpi')
    depends_on('autoconf')
    depends_on('automake')
    depends_on('libtool')

    # Mochi dependencies for normal versions
    depends_on('mochi-margo@0.4:')
    depends_on('mochi-ssg+mpi@0.2', when='@:0.3')
    depends_on('mochi-ssg+mpi@0.4.0:', when='@0.4:')
    depends_on('mochi-ch-placement@0.1:')
    depends_on('mochi-sdskv@0.1:')
    depends_on('mochi-bake@0.1:')
    depends_on('mochi-bake@0.3:0.3.6', when='@:0.4.1')
    depends_on('mochi-bake@0.4:', when='@0.4.2:');

    # Mochi dependencies for develop version
    depends_on('mochi-margo@develop', when='@develop')
    depends_on('mochi-ssg+mpi@develop', when='@develop')
    depends_on('mochi-ch-placement@develop', when='@develop')
    depends_on('mochi-sdskv@develop', when='@develop')
    depends_on('mochi-bake@develop', when='@develop')
    depends_on('mochi-symbiomon@develop', when='@develop')

    patch('0001-crude-timing-information.patch', when="+timing")

    def configure_args(self):
        extra_args = []
        extra_args.extend(['CC=%s' % self.spec['mpi'].mpicc])
        extra_args.extend(['CXX=%s' % self.spec['mpi'].mpicxx])
        return extra_args
