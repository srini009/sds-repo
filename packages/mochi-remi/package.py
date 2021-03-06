from spack import *


class MochiRemi(CMakePackage):
    """REMI is a Mochi microservice designed to handle the migration of sets of files
    from a node to another. It uses RDMA and memory mapping to efficiently transfer
    potentially large groups of files at once."""

    homepage = "https://xgitlab.cels.anl.gov/sds/remi"
    url = "https://xgitlab.cels.anl.gov/sds/remi"
    git='https://xgitlab.cels.anl.gov/sds/remi.git'

    version('develop', branch='master')
    version('master', branch='master')
    version('0.2.3', tag='v0.2.3')
    version('0.2.2', tag='v0.2.2')
    version('0.2.1', tag='v0.2.1')
    version('0.2', tag='v0.2')
    version('0.1.1', tag='v0.1.1')
    version('0.1', tag='v0.1')

    depends_on('libuuid')
    depends_on('mochi-thallium@0.6.0:+cereal', when='@0.2.3:')
    depends_on('mochi-thallium@0.4.2:', when='@0.2.2')
    depends_on('mochi-thallium@0.3:', when='@:0.2.1')
    depends_on('mochi-abt-io@0.1:')

    # dependencies for develop version
    depends_on('mochi-thallium@develop', when='@develop')
    depends_on('mochi-abt-io@develop', when='@develop')

    patch('0001-explicitly-request-C-14.patch')

    def cmake_args(self):
        args = ["-DBUILD_SHARED_LIBS:BOOL=ON" ]
        return args
