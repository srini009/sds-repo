from spack import *


class MochiSymbiomon(CMakePackage):
    """SYMBIOMON is a Mochi microservice designed to capture and export metrics in 
    time-series data format over RDMA. It is primarily intended for remote-monitoring
    purposes."""

    homepage = "https://github.com/srini009/symbiomon"
    url = "https://github.com/srini009/symbiomon"
    git='https://github.com/srini009/symbiomon.git'

    version('develop', branch='master')

    depends_on('libuuid')
    depends_on('mochi-margo@develop')
    depends_on('mercury@master')
    depends_on('argobots@main')
    depends_on('mochi-abt-io@0.5:')

    def cmake_args(self):
        args = ["-DBUILD_SHARED_LIBS:BOOL=ON" ]
        return args
