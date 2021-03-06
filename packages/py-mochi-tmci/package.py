from spack import *


class PyMochiTmci(PythonPackage):
    """Python Mochi library to enable generic, C++ level access to Tensorflow memory"""

    homepage = "https://xgitlab.cels.anl.gov/sds/tmci"
    url      = "https://xgitlab.cels.anl.gov/sds/tmci.git"
    git      = "https://xgitlab.cels.anl.gov/sds/tmci.git"

    version('master', branch="master", preferred=True)
    version('develop', branch="master")

    variant('theta', default=False,
            description='Option to enable when building on Theta')

    depends_on('python@3:')
    depends_on('py-tensorflow@2.0.0:', type=('build', 'link', 'run'))
    depends_on('py-pybind11', type=('build'))

    @run_before('build')
    def move_file(self):
        if '+theta' in self.spec:
            src = self.stage.source_path+'/theta/tensorflow.json'
            dst = self.stage.source_path+'/tensorflow.json'
            copy(src, dst)
