from spack import *


class MochiCollector(CMakePackage):
    """COLLECTOR is a Mochi microservice designed to capture and export metrics in 
    time-series data format over RDMA. It is primarily intended for remote-monitoring
    purposes."""

    homepage = "https://github.com/srini009/collector"
    url = "https://github.com/srini009/collector"
    git='https://github.com/srini009/collector.git'

    version('develop', branch='master')

    variant('aggregator', default=True, description='Aggregate time-series data')

    depends_on('libuuid')
    depends_on('mochi-margo@develop')
    depends_on('mochi-aggregator@develop', when='+aggregator')
    depends_on('mercury@master')
    #depends_on('argobots@main')
    depends_on('argobots@1.0:')
    depends_on('mochi-abt-io@develop')

    def cmake_args(self):
        args = ["-DBUILD_SHARED_LIBS:BOOL=ON -DENABLE_EXAMPLES=ON" ]
        if '+aggregator' in self.spec:
            args.append('-DENABLE_AGGREGATOR=ON')
        return args
