# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "cutgeneratingfunctionology[passagemath]==1.5.4",
#     "marimo>=0.20.4",
#     "passagemath-modules==10.8.2",
#     "passagemath-repl==10.8.2",
# ]
# ///

import marimo

__generated_with = "0.20.4"
app = marimo.App(
    width="medium",
    css_file="/usr/local/_marimo/custom.css",
    auto_download=["html"],
)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # cutgeneratingfunctionology

    ... is the study of functions $\pi\colon \mathbb R \to \mathbb R$ that generalize the integer rounding principle underlying the Chvátal–Gomory cuts and Gomory fractional cuts for integer linear optimization problems.

    It is also the name of a [pip-installable Python package](https://pypi.org/project/cutgeneratingfunctionology/) that supports research in this area. (Use `pip install "cutgeneratingfunctionology[passagemath]"`.)
    """)
    return


@app.cell
def _():
    import marimo as mo
    import passagemath_repl
    from cutgeneratingfunctionology import igp
    from passagemath_modules import QQ

    return QQ, igp, mo


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The Gomory fractional cut is the cut-generating function that corresponds to the integer rounding principle applied in a simplex tableau (dictionary) setting. The parameter ($\frac45$ in the example below) is determined from the right-hand-side constant of a row of a fractional basic variable.
    """)
    return


@app.cell
def _(QQ, igp):
    π_gomory_fractional = igp.gomory_fractional(QQ('4/5'))
    igp.plot_with_colored_slopes(π_gomory_fractional).show(figsize=(8,2.5))
    return (π_gomory_fractional,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Is the Gomory fractional cut best possible? The theory of cut-generating functions answers "no"; a function that rises above 1 is never "minimal."

    (Smaller is better for cut-generating functions.)
    """)
    return


@app.cell
def _(igp, π_gomory_fractional):
    igp.minimality_test(π_gomory_fractional)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Here is an improvement of the Gomory fractional cut, the Gomory mixed-integer cut $\pi_{\mathtt{gmic}}$.
    """)
    return


@app.cell
def _(QQ, igp):
    π_gmic = igp.gmic(QQ('4/5'))
    igp.plot_with_colored_slopes(π_gmic).show(figsize=(8,2))
    return (π_gmic,)


@app.cell
def _(igp, π_gmic):
    igp.minimality_test(π_gmic)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    In cutgeneratingfunctionology, we use diagrams such as this one to think about cut-generating functions.
    """)
    return


@app.cell
def _(igp, π_gmic):
    igp.plot_2d_diagram(π_gmic, colorful=True)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    There is a whole zoo of cut-generating functions, including this interesting example.
    """)
    return


@app.cell
def _(igp):
    π_h5281 = igp.hildebrand_5_slope_28_1()
    return (π_h5281,)


@app.cell
def _(igp, π_h5281):
    igp.plot_2d_diagram(π_h5281, colorful=True).show(figsize=12)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Like $\pi_{\mathtt{gmic}}$, this cut-generating function is not just minimal, but actually "extreme."
    """)
    return


@app.cell
def _(igp, π_h5281):
    igp.extremality_test(π_h5281)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    [More information about cut-generating functions](https://www.math.ucdavis.edu/~mkoeppe/art/infinite-group/)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    [More marimo notebooks showing functionality of passagemath, the pip-installable modularized fork of SageMath](https://github.com/passagemath/passagemath-marimo-notebooks)
    """)
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
