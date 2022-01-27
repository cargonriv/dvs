import setuptools
import runpy
import os

root = os.path.dirname(os.path.realpath(__file__))
version = runpy.run_path(os.path.join(root, "tonic", "version.py"))["version"]

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tonic",
    version=version,
    author="The Neuromorphs of Telluride",
    author_email="lenz.gregor@gmail.com",
    description="Event-based datasets and transformations based on pyTorch vision.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/neuromorphs/tonic",
    include_package_data=False,
    packages=setuptools.find_packages(),
    install_requires=["numpy", "h5py", "importRosbag>=1.0.3", "scipy", "tqdm", "typing_extensions", "librosa"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Intended Audience :: Science/Research",
    ],
)
