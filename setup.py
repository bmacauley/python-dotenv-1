import os
from setuptools import setup, find_packages

ROOT = os.path.abspath(os.path.dirname(__file__))

setup(
    name='dotenv',
    version='1.0.0',
    description='Load environment variables from file',
    long_description=open(os.path.join(ROOT, 'README.md')).read(),
    author='Konstantinos Pachnis',
    author_email='konstantinos@bugeffect.com',
    url='https://git.bugeffect.com/python-dotenv.git',
    license='BSD 3-Clause',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: BSD 3-Clause License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Utilities',
    ]
)
