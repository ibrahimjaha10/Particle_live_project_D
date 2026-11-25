from importlib.metadata import version

import particle_life


def test_version():
    assert particle_life.__version__ == version("particle-life")
