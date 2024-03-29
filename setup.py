import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="contiflow",
    version="0.0.1",
    url="http://git01-ifm-min.ad.fh-bielefeld.de/pvserve2/contiflow",
    author="Cem Basoglu",
    author_email="cem.basoglu@fh-bielefeld.de",
    description="Client library for communication with contiflow backend.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='MIT',
    packages=setuptools.find_packages(),
    install_requires=[
        'requests'
    ]
)
