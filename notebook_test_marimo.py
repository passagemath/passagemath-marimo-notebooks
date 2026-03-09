# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "marimo>=0.20.4",
#     "passagemath-plot~=10.8.2rc4",
#     "passagemath-repl~=10.8.2rc4",
#     "passagemath-symbolics~=10.8.2rc4",
# ]
# ///

import marimo

__generated_with = "0.20.4"
app = marimo.App(
    css_file="/usr/local/_marimo/custom.css",
    auto_download=["html"],
)

with app.setup:
    import marimo as mo
    import passagemath_plot
    from passagemath_symbolics import var, assume, sqrt, exp, integral, pi, oo, erf, erfc
    from passagemath_repl import get_display_manager
    dm = get_display_manager()


@app.cell
def _():
    v, u, v_th, rho, x, y = var('v u v_th rho x y')
    assume(v_th > 0); assume(v > 0); assume(u, 'real')
    f = rho / (sqrt(pi)*v_th) * exp(-(v-u)**2/(v_th**2))
    I0 = 1/rho * integral(f, v, -oo, 0)
    dm.preferences.text = 'latex'
    I0.simplify_rational()
    return I0, x


@app.cell
def _(I0):
    dm.preferences.text = 'ascii_art'
    I0
    return


@app.cell
def _(I0):
    dm.preferences.text = 'unicode_art'
    I0
    return


@app.cell
def _(I0):
    dm.preferences.text = 'plain'
    I0
    return


@app.cell
def _():
    # 3D plot
    from passagemath_symbolics import EuclideanSpace, sin, Integer, RealNumber
    E = EuclideanSpace(names=('xi', 'yi', 'zi',)); (xi, yi, zi,) = E._first_ngens(3)
    vi = E.vector_field(-yi, xi, sin(xi*yi*zi), name='vi')
    p = E((Integer(3),-Integer(2),Integer(1)), name='p')
    vp = vi.at(p)
    a3dplot = vi.plot(max_range=RealNumber('1.5'), scale=RealNumber('0.5'))
    a3dplot
    return (a3dplot,)


@app.cell
def _(a3dplot):
    # 3D plot with .show()
    a3dplot.show()
    print("see plot above")
    return


@app.cell
def _(x):
    # 2D plot
    from passagemath_plot import plot
    a2dplot = plot(x**2, (x,0,5))
    a2dplot
    return (a2dplot,)


@app.cell
def _(a2dplot, a3dplot):
    a3dplot.show()
    a2dplot.show()
    print("see plot above")
    return


@app.cell
def _(a2dplot):
    # Interactive matplotlib 2D plot
    mo.mpl.interactive(a2dplot.matplotlib())
    return


@app.cell
def _():
    from sage.repl.rich_output.output_catalog import OutputImageGif
    OutputImageGif.example()
    return


@app.cell
def _():
    from sage.repl.rich_output.output_catalog import OutputImageJpg
    OutputImageJpg.example()
    return


@app.cell
def _():
    from sage.repl.rich_output.output_catalog import OutputImageSvg
    OutputImageSvg.example()
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
