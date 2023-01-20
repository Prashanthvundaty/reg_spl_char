
import pip
import unittest
from setuptools import setup

pip_major_version = int(pip.__version__.split(".")[0])
if pip_major_version >= 20:
    from pip._internal.req import parse_requirements
    from pip._internal.network.session import PipSession
elif pip_major_version >= 10:
    from pip._internal.req import parse_requirements
    from pip._internal.download import PipSession
else:
    from pip.req import parse_requirements
    from pip.download import PipSession


################################################################################
def my_test_suite():
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover('argoslabs.test_project.app',
                                        pattern='test*.py')
    return test_suite


################################################################################
def append_safe_req(reqs, req):
    if not req:
        return False
    if req.startswith('https://') or req.startswith('https://'):
        return False
    req = req.split(';')[0]
    if req not in reqs:
        reqs.append(req)


################################################################################
# parse_requirements() returns generator of pip.req.InstallRequirement objects
install_reqs = parse_requirements("argoslabs\\test_project\\app\\requirements.txt", session=PipSession())
#reqs = [str(ir.req) for ir in install_reqs]
reqs = list()
for ir in install_reqs:
    if hasattr(ir, 'req'):
        req = ir.req
    elif hasattr(ir, 'requirement'):
        req = ir.requirement
    else:
        raise LookupError('Cannot get requirement')
    append_safe_req(reqs, str(req))
reqs.extend([])

setup(
    name='argoslabs.test_project.app',
    test_suite='setup.my_test_suite',
    packages=[
        'argoslabs','argoslabs.test_project','argoslabs.test_project.app','argoslabs.test_project.app.tests'
    ],
    version='2.465.2852',
    description='ARGOS-LABS RPA plugin module sample',
    author='Prashanth Kumar V',
    author_email='mcchae@argos-labs.com',
    url='https://www.argos-labs.com',
    license='ARGOS-LABS Proprietary License',
    keywords=['rpa', 'robot', 'module', 'test_project', 'argoslabs', 'app'],
    platforms=['Mac', 'Windows', 'Linux'],
    install_requires=reqs,
    python_requires='>=3.6',
    package_data={'argoslabs.test_project.app': ['icon.*', 'dumpspec.json']},
    zip_safe=False,
    classifiers=[
        'Build :: Date :: 2023-01-20 16:02',
        'Build :: Method :: alabs.ppm',
        'License :: Other/Proprietary License',
        'Natural Language :: English',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows :: Windows 10',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Change :: Log :: Unittest for Linux',
        'Topic :: Change :: Log :: Unittest for Mac',
        'Topic :: Change :: Log :: Unittest for Windows',
        'Topic :: Demo :: Special Char app',
        'Topic :: RPA',
    ],
    entry_points={
        'console_scripts': [
            'argoslabs.test_project.app=argoslabs.test_project.app:main',
        ],
    },
    include_package_data=True,
)
