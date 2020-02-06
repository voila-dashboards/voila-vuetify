# voila-vuetify

[![Join the Gitter Chat](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/QuantStack/Lobby?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
[![Version](https://img.shields.io/pypi/v/voila-vuetify.svg)](https://pypi.python.org/project/voila-vuetify)
[![Conda Version](https://img.shields.io/conda/vn/conda-forge/voila-vuetify.svg)](https://anaconda.org/conda-forge/voila-vuetify)

## Installation

`voila-vuetify` can be installed from PyPI

```
pip install voila-vuetify
```

or from conda:

```
conda install -c conda-forge voila-vuetify
```

## Usage

To use the `vuetify` template, just pass `--template=vuetify-default` to the `voila` command line.

The example notebook also requires bqplot and ipyvuetify:

```
pip install bqplot ipyvuetify voila-vuetify
voila --template vuetify-default bqplot_vuetify_example.ipynb
```

![voila-vuetify](https://user-images.githubusercontent.com/46192475/59274938-9c144f00-8c5b-11e9-961e-c33854b6e50a.gif)

## License

We use a shared copyright model that enables all contributors to maintain the
copyright on their contributions.

This software is licensed under the BSD-3-Clause license. See the
[LICENSE](LICENSE) file for details.
