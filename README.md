# passagemath-marimo-notebooks: Example marimo notebooks

## Test notebook for rich output

[notebook_test_marimo.py](notebook_test_marimo.py)

## SageManifolds notebooks

These marimo notebooks, adapted from Jupyter notebooks published in https://sagemanifolds.obspm.fr/examples.html, demonstrate some differential geometry capabilities of SageMath.

The corresponding tools have been developed within
the [SageManifolds](https://sagemanifolds.obspm.fr) project. They are now available in Python environments via the modularized distributions of the Sage library developed by the [passagemath](https://github.com/passagemath) project.
- The SageManifolds functionality is shipped as part of [passagemath-symbolics](https://pypi.org/project/passagemath-symbolics/).
- The pip-installable package [passagemath-maxima](https://pypi.org/project/passagemath-maxima/) provides the backend for symbolic computation.
- [passagemath-plot](https://pypi.org/project/passagemath-plot/) provides 2D and 3D plotting facilities.
- [passagemath-repl](https://pypi.org/project/passagemath-repl/) provides the integration with the marimo notebook.

| Notebook                                                                                                                                                         | Description                                                                                                                                                                                 |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [SM_sphere_S2.py](SM_sphere_S2.py) <br>[![Open in molab](https://molab.marimo.io/molab-shield.svg)](https://molab.marimo.io/notebooks/nb_LTtuUofpxnkemmZShfehFT) | The 2-sphere with multiple domains and charts, transition maps, scalar and vector fields, tangent spaces, curves, plot of charts and vector fields, embedding, pullback, Riemannian metric. |
| [SM_Kerr_surfaces.py](SM_Kerr_surfaces.py) <br>[![Open in molab](https://molab.marimo.io/molab-shield.svg)](https://molab.marimo.io/notebooks/nb_LnRFetdWJJazCt5Tc3bMjc) | Black hole spacetimes: Kerr spacetime with rational polynomial, Kerr and Kerr-Schild coordinates, Kretschmann scalar, animated plot of the horizons and ergosurfaces. |

## Notebooks for downstream packages

The passagemath project curates a [library of user packages that make use of the Sage library](https://github.com/passagemath#passagemath-in-the-mathematical-software-landscape) and makes them ready for the Scientific Python ecosystem. Here are some notebooks that illustrate the functionality of some of these projects.

| Notebook                                                                                                                                                         | Description                                                                                                                                                                                 |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [cutgeneratingfunctionology.py](cutgeneratingfunctionology.py) <br>[![Open in molab](https://molab.marimo.io/molab-shield.svg)](https://molab.marimo.io/notebooks/nb_ZBG1ni5sECEQuz5eFukzA2) | Study of functions that generalize the integer rounding principle underlying the Chvátal–Gomory cuts and Gomory fractional cuts for integer linear optimization problems. |
