![tonic](tonic-logo-padded.png)
[![PyPI](https://img.shields.io/pypi/v/tonic)](https://pypi.org/project/tonic/)
[![Github actions CI pipeline](https://github.com/neuromorphs/tonic/actions/workflows/ci-pipeline.yml/badge.svg)](https://github.com/neuromorphs/tonic/actions/workflows/ci-pipeline.yml)
[![codecov](https://codecov.io/gh/neuromorphs/tonic/branch/develop/graph/badge.svg?token=Q0BMYGUSZQ)](https://codecov.io/gh/neuromorphs/tonic)
[![Documentation Status](https://readthedocs.org/projects/tonic/badge/?version=latest)](https://tonic.readthedocs.io/en/latest/?badge=latest)
[![contributors](https://img.shields.io/github/contributors-anon/neuromorphs/tonic)](https://github.com/neuromorphs/tonic/pulse)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/neuromorphs/tonic/main?labpath=docs%2Ftutorials)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.5079802.svg)](https://doi.org/10.5281/zenodo.5079802)


**Tonic** is a tool to facilitate the download, manipulation and loading of event-based/spike-based data. It's like PyTorch Vision but for neuromorphic data!

:rocket: **Stable version 1 out now!** [Check out the release notes here](https://tonic.readthedocs.io/en/latest/about/release_notes.html).

## Documentation
You can find the full documentation on Tonic [on this site](https://tonic.readthedocs.io/en/latest/index.html).

* [Never worked with events?](https://tonic.readthedocs.io/en/latest/getting_started/intro-event-cameras.html) Start here.
* [A first example](https://tonic.readthedocs.io/en/latest/tutorials/nmnist.html) to get a feeling for how Tonic works.
* [Run tutorials in your browser](https://mybinder.org/v2/gh/neuromorphs/tonic/main?labpath=docs%2Ftutorials) quick and easy.
* [List of datasets](https://tonic.readthedocs.io/en/latest/reference/datasets.html).
* [List of transformations](https://tonic.readthedocs.io/en/latest/reference/transformations.html).
* [About](https://tonic.readthedocs.io/en/latest/about/about.html) this project.
* [Release notes](https://tonic.readthedocs.io/en/latest/about/release_notes.html) on version changes.

## Install
```bash
pip install tonic
```
If you prefer conda, please check out the [conda forge repository](https://github.com/conda-forge/tonic-feedstock).

## Quickstart
If you're looking for a minimal example to run, this is it!

```python
import tonic
import tonic.transforms as transforms

sensor_size = tonic.datasets.NMNIST.sensor_size
transform = transforms.Compose([transforms.Denoise(filter_time=10000),
                                transforms.ToFrame(sensor_size=sensor_size, n_time_bins=3),])

testset = tonic.datasets.NMNIST(save_to='./data',
                                train=False,
                                transform=transform)

from torch.utils.data import DataLoader
testloader = DataLoader(testset, shuffle=True)

events, target = next(iter(testloader))
```

## Discussion
Have a question about how something works? Ideas for improvement? Feature request? Please get in touch here on GitHub via the [Discussions](https://github.com/neuromorphs/tonic/discussions) page!

## Contributing
Please check out the [contributions](https://tonic.readthedocs.io/en/latest/about/contribute.html) page for details.

## Citation
If you find this package helpful, please consider citing it:

```BibTex
@software{lenz_gregor_2021_5079802,
  author       = {Lenz, Gregor and
                  Chaney, Kenneth and
                  Shrestha, Sumit Bam and
                  Oubari, Omar and
                  Picaud, Serge and
                  Zarrella, Guido},
  title        = {Tonic: event-based datasets and transformations.},
  month        = jul,
  year         = 2021,
  note         = {{Documentation available under 
                   https://tonic.readthedocs.io}},
  publisher    = {Zenodo},
  version      = {0.4.0},
  doi          = {10.5281/zenodo.5079802},
  url          = {https://doi.org/10.5281/zenodo.5079802}
}
```
