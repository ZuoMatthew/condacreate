import os
import uuid
import pytest
import zipfile


from condacreate import CondaException
from condacreate import CondaCreator

@pytest.yield_fixture
def c():
    c = CondaCreator()
    yield c


def test_miniconda_install(c):
    assert c._install_miniconda()
    import ipdb
    ipbd.set_strace()


def test_create(c):
    with pytest.raises(TypeError):
        env_name = str(uuid.uuid4())
        c.create_env(env_name, packages='numpy')

    env_name = 'test_env'
    env_path = os.path.join(c.conda_root, 'envs', env_name)
    assert env_path == c._create_env(env_name, packages=['python=3', 'numpy'], remove=True)

    with pytest.raises(CondaException):
        c._create_env(env_name, packages=['pandas'])


def test_full_create(c):
    env_name = 'test_env'
    env_zip = os.path.join(c.conda_root, 'envs', env_name+'.zip')
    assert env_zip == c.create_env(env_name, packages=['python=3', 'numpy'], remove=True)
    assert os.path.getsize(env_zip) > 500000 # ensures zipfile has non-0 size
    assert zipfile.is_zipfile(env_zip)

    f = zipfile.ZipFile(env_zip, 'r')
    try:
        assert f.getinfo('test_env/bin/python')
    finally:
        f.close()


def test_find_env(c):
    env_name = 'test_env'
    env_zip = os.path.join(c.conda_root, 'envs', env_name+'.zip')
    assert env_zip == c.create_env(env_name)

    # no error here -- the packages have already been installed so we
    # return the env_zip
    env_zip == c.create_env(env_name, packages=['python=3', 'numpy'])
