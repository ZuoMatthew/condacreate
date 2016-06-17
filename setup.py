import versioneer
from os.path import exists
from setuptools import setup


setup(name='condacreate',
      version=versioneer.get_version(),
      cmdclass=versioneer.get_cmdclass(),
      description='Programmatically create conda envs ',
      url='http://github.com/quasiben/condacreate/',
      maintainer='Benjamin Zaitlen',
      maintainer_email='quasiben@gmail.com',
      license='BSD',
      packages=['condacreate'],
      long_description=(open('README.rst').read() if exists('README.rst')
                        else ''),
      zip_safe=False)
