from spack import *


class MochiAggregator(CMakePackage):
    """AGGREGATOR is a Mochi microservice designed to aggregator 
    time-series data format over RDMA. It is primarily intended for remote-monitoring
    purposes."""

    homepage = "https://github.com/srini009/aggregator"
    url = "https://github.com/srini009/aggregator"
    git='https://github.com/srini009/aggregator.git'

    version('develop', branch='master')

    depends_on('libuuid')
    depends_on('mochi-margo@develop')
    depends_on('mercury@master')
    #depends_on('argobots@main')
    depends_on('mpi')
    depends_on('argobots@1.0:')
    depends_on('mochi-abt-io@develop')

    def cmake_args(self):
        args = ["-DBUILD_SHARED_LIBS:BOOL=ON -DENABLE_EXAMPLES=ON" ]
	args.append('-DCMAKE_C_COMPILER=%s' % self.spec['mpi'].mpicc)
        return args
