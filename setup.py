from setuptools import setup

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='Nonparametric-ICA',
    url='https://github.com/dskrill/nonparametric-ica-python',
    author='David Skrill',
    author_email='davidmskrillgmail.com',
    # Needed to actually package something
    packages=['npica'],
    # Needed for dependencies
    install_requires=['numpy','itertools'],
    # *strongly* suggested for sharing
    version='0.1',
    # The license can be anything you like
    license='MIT',
    description='A Python implementation of https://github.com/snormanhaignere/nonparametric-ica',
    # We will also need a readme eventually (there will be a warning)
    # long_description=open('README.txt').read(),
)
