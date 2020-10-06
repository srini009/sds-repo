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
#
# Installing py-sdskv:
#
#     spack install py-sdskv
#
from spack import *

class PyMochiSdskv(PythonPackage):
    """Python wrapper for the Mochi KV library"""

    homepage = "https://xgitlab.cels.anl.gov/sds/py-sdskv"
    url      = "https://xgitlab.cels.anl.gov/sds/py-sdskv"
    git      = "https://xgitlab.cels.anl.gov/sds/py-sdskv.git"

    version('develop',  branch="master")
    version('master',  branch="master")
    version('0.1.4', tag='v0.1.4')
    version('0.1.3', tag='v0.1.3')
    version('0.1.2', tag='v0.1.2')
    version('0.1.1', tag='v0.1.1')
    version('0.1', tag='v0.1')

    depends_on('py-pkgconfig', type=('build'))
    depends_on('py-pybind11', type=('build'))
    depends_on('mochi-sdskv@0.1:')
    depends_on('mochi-sdskv@0.1.3:', when='@0.1.3:')
    depends_on('mochi-sdskv@develop', when='@develop')
    depends_on('py-mochi-margo@0.1:', when='@:0.1.1')
    depends_on('py-mochi-margo@develop', when='@develop')
    depends_on('py-mochi-margo@0.2.4:', when='@0.1.2:')
