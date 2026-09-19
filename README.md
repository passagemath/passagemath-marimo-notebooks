# passagemath-marimo-notebooks: Example marimo notebooks

## Example notebooks for passagemath distributions

🐙[passagemath](https://github.com/passagemath/passagemath) provides the full functionality of SageMath
and more in pip-installable modularized packages (distributions), which can also be used separately.

| Notebook                                                                                                                                                                                                                       | Description                                                                                                                                                                                                                         |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [passagemath-cmr.py](passagemath-cmr.py) <br>[![Open in molab](https://molab.marimo.io/molab-shield.svg)](https://molab.marimo.io/https://github.com/passagemath/passagemath-marimo-notebooks/blob/main/passagemath-cmr.py)    | Seymour's decomposition of totally unimodular matrices and regular matroids, using the [Combinatorial Matrix Recognition](https://discopt.github.io/cmr/) library via [![PyPI: passagemath-cmr](https://img.shields.io/pypi/v/passagemath-cmr.svg?label=🐙passagemath-cmr)](https://pypi.python.org/pypi/passagemath-cmr). |
| [passagemath-repl.py](passagemath-repl.py) <br>[![Open in molab](https://molab.marimo.io/molab-shield.svg)](https://molab.marimo.io/https://github.com/passagemath/passagemath-marimo-notebooks/blob/main/passagemath-repl.py) | Test notebook for rich output in Marimo, facilitated by [![PyPI: passagemath-repl](https://img.shields.io/pypi/v/passagemath-repl.svg?label=🐙passagemath-repl)](https://pypi.python.org/pypi/passagemath-repl).                                                                                                             |


## SageManifolds notebooks

These marimo notebooks, adapted from some of the Jupyter notebooks published in https://sagemanifolds.obspm.fr/examples.html, demonstrate some differential geometry capabilities of SageMath.

The corresponding tools have been developed within
the [SageManifolds](https://sagemanifolds.obspm.fr) project. They are now available in Python environments via the modularized distributions of the Sage library developed by the [passagemath](https://github.com/passagemath) project.
- The SageManifolds functionality is shipped as part of [![PyPI: passagemath-symbolics](https://img.shields.io/pypi/v/passagemath-symbolics.svg?label=🐙passagemath-symbolics)](https://pypi.python.org/pypi/passagemath-symbolics).
- The pip-installable package [![PyPI: passagemath-maxima](https://img.shields.io/pypi/v/passagemath-maxima.svg?label=🐙passagemath-maxima)](https://pypi.python.org/pypi/passagemath-maxima) provides the backend for symbolic computation.
- [![PyPI: passagemath-plot](https://img.shields.io/pypi/v/passagemath-plot.svg?label=🐙passagemath-plot)](https://pypi.python.org/pypi/passagemath-plot) provides 2D and 3D plotting facilities.
- [![PyPI: passagemath-repl](https://img.shields.io/pypi/v/passagemath-repl.svg?label=🐙passagemath-repl)](https://pypi.python.org/pypi/passagemath-repl) provides the integration with the marimo notebook.

| Notebook                                                                                                                                                         | Description                                                                                                                                                                                 |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [SM_sphere_S2.py](SM_sphere_S2.py) <br>[![Open in molab](https://molab.marimo.io/molab-shield.svg)](https://molab.marimo.io/notebooks/nb_LTtuUofpxnkemmZShfehFT) | The sphere $\mathbb{S}^2$ with multiple domains and charts, transition maps, scalar and vector fields, tangent spaces, curves, plot of charts and vector fields, embedding, pullback, Riemannian metric. |
| [SM_hyperbolic_plane.py](SM_hyperbolic_plane.py) <br>[![Open in molab](https://molab.marimo.io/molab-shield.svg)](https://molab.marimo.io/notebooks/nb_bfBNvHiNDMtg1wsQyct52P) | Hyperbolic plane $H^2$: many charts associated with various models of $H^2$, embedding, pullback, curvature, changes of chart, graphics. |
| [SM_sphere_S3_Hopf.py](SM_sphere_S3_Hopf.py) [![Open in molab](https://molab.marimo.io/molab-shield.svg)](https://molab.marimo.io/notebooks/nb_KZSJhQ7AwoNWdDqGqdYzh8) | The sphere $\mathbb{S}^3$ with various charts, quaternions, and Hopf fibration. |
| [SM_Kerr_surfaces.py](SM_Kerr_surfaces.py) <br>[![Open in molab](https://molab.marimo.io/molab-shield.svg)](https://molab.marimo.io/notebooks/nb_LnRFetdWJJazCt5Tc3bMjc) | Black hole spacetimes: Kerr spacetime with rational polynomial, Kerr and Kerr-Schild coordinates, Kretschmann scalar, animated plot of the horizons and ergosurfaces. |

## Notebooks for downstream packages

The passagemath project [curates](https://github.com/passagemath/passagemath/issues/248) a [library of user packages that make use of the Sage library](https://github.com/passagemath#passagemath-in-the-mathematical-software-landscape) and makes them ready for the Scientific Python ecosystem. Here are some notebooks that illustrate the functionality of some of these projects.

| Notebook                                                                                                                                                         | Description                                                                                                                                                                                 |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [cutgeneratingfunctionology.py](cutgeneratingfunctionology.py) <br>[![Open in molab](https://molab.marimo.io/molab-shield.svg)](https://molab.marimo.io/notebooks/nb_ZBG1ni5sECEQuz5eFukzA2) | Study of functions that generalize the integer rounding principle underlying the Chvátal–Gomory cuts and Gomory fractional cuts for integer linear optimization problems. |
