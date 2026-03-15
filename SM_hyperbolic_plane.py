# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "marimo>=0.20.4",
#     "passagemath-maxima==10.8.2",
#     "passagemath-plot==10.8.2",
#     "passagemath-repl==10.8.2",
#     "passagemath-symbolics==10.8.2",
# ]
# ///

import marimo

__generated_with = "0.20.4"
app = marimo.App(
    css_file="/usr/local/_marimo/custom.css",
    auto_download=["html"],
)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # SageManifolds example notebook using [passagemath](https://github.com/passagemath):  Hyperbolic plane $\mathbb{H}^2$
    """)
    return


@app.cell
def _():
    import marimo as mo
    import passagemath_maxima
    from passagemath_symbolics import (
        RR, SR, sin, cos, atan, atan2, pi, sqrt, exp, oo, diff, factor,
        Manifold, EuclideanSpace, manifolds, Hom, FiniteRankFreeModule, dim, 
        Parallelism, var, solve, acos, function, assume, integral, vector, 
        sum, srange, maxima_calculus, arcsin
    )
    from passagemath_plot import (
        show, sphere, colormaps, parametric_plot3d, text3d, Graphics, animate
    )
    from passagemath_repl import get_display_manager; dm = get_display_manager()
    return Manifold, arcsin, atan2, cos, maxima_calculus, mo, show, sin, sqrt


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    This marimo notebook, adapted from a Jupyter notebook published in https://sagemanifolds.obspm.fr/examples.html, illustrates some differential geometry capabilities of SageMath on the example of the hyperbolic plane.

    The corresponding tools have been developed within the [SageManifolds project](https://sagemanifolds.obspm.fr/). They are now available in Python environments via the modularized distributions of the Sage library developed by the [passagemath](https://github.com/passagemath) project.
    - The SageManifolds functionality is shipped as part of [passagemath-symbolics](https://pypi.org/project/passagemath-symbolics/).
    - The pip-installable package [passagemath-maxima](https://pypi.org/project/passagemath-maxima/) provides the backend for symbolic computation.
    - [passagemath-plot](https://pypi.org/project/passagemath-plot/) provides 2D and 3D plotting facilities.
    - [passagemath-repl](https://pypi.org/project/passagemath-repl/) provides the integration with the marimo notebook.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We  tell Maxima, which is used by SageMath for simplifications of symbolic expressions, that all computations involve real variables:
    """)
    return


@app.cell
def _(maxima_calculus):
    maxima_calculus.eval("domain: real;")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We declare $\mathbb{H}^2$ as a 2-dimensional differentiable manifold:
    """)
    return


@app.cell
def _(Manifold):
    H2 = Manifold(2, 'H2', latex_name=r'\mathbb{H}^2', start_index=1)
    print(H2)
    H2
    return (H2,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We shall introduce charts on $\mathbb{H}^2$ that are related to various models of the hyperbolic plane as submanifolds of $\mathbb{R}^3$. Therefore, we start by declaring $\mathbb{R}^3$ as a 3-dimensional manifold equiped with a global chart: the chart of Cartesian coordinates $(X,Y,Z)$:
    """)
    return


@app.cell
def _(Manifold):
    R3 = Manifold(3, 'R3', latex_name=r'\mathbb{R}^3', start_index=1)
    X3 = R3.chart('X Y Z')
    X3
    return R3, X3


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Hyperboloid model

    The first chart we introduce is related to the **hyperboloid model of $\mathbb{H}^2$**, namely to the representation of $\mathbb{H}^2$ as the upper sheet ($Z>0$) of the hyperboloid of two sheets defined in $\mathbb{R}^3$ by the equation $X^2 + Y^2 - Z^2 = -1$:
    """)
    return


@app.cell
def _(H2):
    X_hyp = H2.chart('X Y')
    X, Y = X_hyp[:]
    X_hyp
    return X, X_hyp, Y


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The corresponding embedding of $\mathbb{H}^2$ in $\mathbb{R}^3$ is
    """)
    return


@app.cell
def _(H2, R3, X, Y, sqrt):
    Phi1 = H2.diff_map(R3, [X, Y, sqrt(1+X**2+Y**2)], name='Phi_1', latex_name=r'\Phi_1')
    Phi1.display()
    return (Phi1,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    By plotting the chart $\left(\mathbb{H}^2,(X,Y)\right)$ in terms of the Cartesian coordinates of $\mathbb{R}^3$, we get a graphical view of $\Phi_1(\mathbb{H}^2)$:
    """)
    return


@app.cell
def _(Phi1, X3, X_hyp, show):
    show(X_hyp.plot(X3, mapping=Phi1, number_values=15, color='blue'), 
         aspect_ratio=1, figsize=7)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    A second chart is obtained from the polar coordinates $(r,\varphi)$ associated with $(X,Y)$. In contrast to $(X,Y)$, the polar chart is not defined on the whole $\mathbb{H}^2$, but on the complement $U$ of the segment $\{Y=0, x\geq 0\}$:
    """)
    return


@app.cell
def _(H2, X, X_hyp, Y):
    U = H2.open_subset('U', coord_def={X_hyp: (Y!=0, X<0)})
    print(U)
    return (U,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Note that `(y!=0, x<0)` stands for $y\not=0$ OR $x<0$; the condition $y\not=0$ AND $x<0$ would have been written `[y!=0, x<0]` instead.
    """)
    return


@app.cell
def _(U):
    X_pol = U.chart(r'r:(0,+oo) ph:(0,2*pi):\varphi')
    r, ph = X_pol[:]
    X_pol
    return X_pol, ph, r


@app.cell
def _(X_pol):
    X_pol.coord_range()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We specify the transition map between the charts $\left(U,(r,\varphi)\right)$ and $\left(\mathbb{H}^2,(X,Y)\right)$ as $X=r\cos\varphi$, $Y=r\sin\varphi$:
    """)
    return


@app.cell
def _(X_hyp, X_pol, cos, ph, r, sin):
    pol_to_hyp = X_pol.transition_map(X_hyp, [r*cos(ph), r*sin(ph)])
    pol_to_hyp
    return (pol_to_hyp,)


@app.cell
def _(pol_to_hyp):
    pol_to_hyp.display()
    return


@app.cell
def _(X, Y, atan2, pol_to_hyp, sqrt):
    pol_to_hyp.set_inverse(sqrt(X**2 + Y**2), atan2(Y, X))
    return


@app.cell
def _(pol_to_hyp):
    pol_to_hyp.inverse().display()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The restriction of the embedding $\Phi_1$ to $U$ has then two coordinate expressions:
    """)
    return


@app.cell
def _(Phi1, U):
    Phi1.restrict(U).display()
    return


@app.cell
def _(Phi1, U, X3, X_pol, r, show):
    graph_hyp = X_pol.plot(X3, mapping=Phi1.restrict(U), number_values=15, 
                           ranges={r: (0,3)}, 
                           color='blue')
    show(graph_hyp, aspect_ratio=1, figsize=7)
    return (graph_hyp,)


@app.cell
def _(Phi1):
    Phi1._coord_expression
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Metric and curvature

    The metric on $\mathbb{H}^2$ is that induced by the Minkowksi metric on $\mathbb{R}^3$:
    $$ \eta = \mathrm{d}X\otimes\mathrm{d}X + \mathrm{d}Y\otimes\mathrm{d}Y - \mathrm{d}Z\otimes\mathrm{d}Z $$
    """)
    return


@app.cell
def _(R3):
    eta = R3.lorentzian_metric('eta', latex_name=r'\eta')
    eta[1,1] = 1; eta[2,2] = 1; eta[3,3] = -1
    eta.display()
    return (eta,)


@app.cell
def _(H2, Phi1, eta):
    g = H2.metric('g')
    g.set(Phi1.pullback(eta))
    g.display()
    return (g,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The expression of the metric tensor in terms of the polar coordinates is
    """)
    return


@app.cell
def _(X_pol, g):
    g.display(X_pol.frame(), X_pol)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The Riemann curvature tensor associated with $g$ is
    """)
    return


@app.cell
def _(g):
    Riem = g.riemann()
    print(Riem)
    return (Riem,)


@app.cell
def _(Riem, X_pol):
    Riem.display(X_pol.frame(), X_pol)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The Ricci tensor and the Ricci scalar:
    """)
    return


@app.cell
def _(g):
    Ric = g.ricci()
    print(Ric)
    return (Ric,)


@app.cell
def _(Ric, X_pol):
    Ric.display(X_pol.frame(), X_pol)
    return


@app.cell
def _(g):
    Rscal = g.ricci_scalar()
    print(Rscal)
    return (Rscal,)


@app.cell
def _(Rscal):
    Rscal.display()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Hence we recover the fact that $(\mathbb{H}^2,g)$ is a space of **constant negative curvature**.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    In dimension 2, the Riemann curvature tensor is entirely determined by the Ricci scalar $R$ according to

    $$R^i_{\ \, jlk} = \frac{R}{2} \left( \delta^i_{\ \, k} g_{jl} - \delta^i_{\ \, l} g_{jk} \right)$$

    Let us check this formula here, under the form $R^i_{\ \, jlk} = -R g_{j[k} \delta^i_{\ \, l]}$:
    """)
    return


@app.cell
def _(H2, Riem, Rscal, g):
    delta = H2.tangent_identity_field()
    Riem == - Rscal*(g*delta).antisymmetrize(2,3)  # 2,3 = last positions of the type-(1,3) tensor g*delta
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Similarly the relation $\mathrm{Ric} = (R/2)\; g$ must hold:
    """)
    return


@app.cell
def _(Ric, Rscal, g):
    Ric == (Rscal/2)*g
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Poincaré disk model

    The Poincaré disk model of $\mathbb{H}^2$ is obtained by stereographic projection from the point $S=(0,0,-1)$ of the hyperboloid model to the plane $Z=0$. The radial coordinate $R$ of the image of a point of polar coordinate $(r,\varphi)$ is
    $$ R = \frac{r}{1+\sqrt{1+r^2}}.$$
    Hence we define the Poincaré disk chart on $\mathbb{H}^2$ by
    """)
    return


@app.cell
def _(U):
    X_Pdisk = U.chart(r'R:(0,1) ph:(0,2*pi):\varphi')
    R, ph_Pdisk = X_Pdisk[:]
    X_Pdisk
    return R, X_Pdisk, ph_Pdisk


@app.cell
def _(X_Pdisk):
    X_Pdisk.coord_range()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    and relate it to the hyperboloid polar chart by
    """)
    return


@app.cell
def _(X_Pdisk, X_pol, ph, r, sqrt):
    pol_to_Pdisk = X_pol.transition_map(X_Pdisk, [r/(1+sqrt(1+r**2)), ph])
    pol_to_Pdisk
    return (pol_to_Pdisk,)


@app.cell
def _(pol_to_Pdisk):
    pol_to_Pdisk.display()
    return


@app.cell
def _(R, ph_Pdisk, pol_to_Pdisk):
    pol_to_Pdisk.set_inverse(2*R/(1-R**2), ph_Pdisk)
    pol_to_Pdisk.inverse().display()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    A view of the Poincaré disk chart via the embedding $\Phi_1$:
    """)
    return


@app.cell
def _(Phi1, R, U, X3, X_Pdisk, show):
    show(X_Pdisk.plot(X3, mapping=Phi1.restrict(U), ranges={R: (0,0.9)}, color='blue',
                      number_values=15), 
         aspect_ratio=1, figsize=7)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The expression of the metric tensor in terms of coordinates $(R,\varphi)$:
    """)
    return


@app.cell
def _(X_Pdisk, g):
    g.display(X_Pdisk.frame(), X_Pdisk)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We may factorize each metric component:
    """)
    return


@app.cell
def _(X_Pdisk, g):
    for i in [1,2]:
        g[X_Pdisk.frame(), i, i, X_Pdisk].factor()
    g.display(X_Pdisk.frame(), X_Pdisk)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Cartesian coordinates on the Poincaré disk

    Let us introduce Cartesian coordinates $(u,v)$ on the Poincaré disk; since the latter has a unit radius, this amounts to defining the following chart on $\mathbb{H}^2$:
    """)
    return


@app.cell
def _(H2):
    X_Pdisk_cart = H2.chart('u:(-1,1) v:(-1,1)', 
                            coord_restrictions=lambda u,v: u**2+v**2 < 1)
    u, v = X_Pdisk_cart[:]
    X_Pdisk_cart
    return X_Pdisk_cart, u, v


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    On $U$, the Cartesian coordinates $(u,v)$ are related to the polar coordinates $(R,\varphi)$ by the standard formulas:
    """)
    return


@app.cell
def _(R, X_Pdisk, X_Pdisk_cart, cos, ph_Pdisk, sin):
    Pdisk_to_Pdisk_cart = X_Pdisk.transition_map(X_Pdisk_cart, 
                                                 [R*cos(ph_Pdisk), R*sin(ph_Pdisk)])
    Pdisk_to_Pdisk_cart
    return (Pdisk_to_Pdisk_cart,)


@app.cell
def _(Pdisk_to_Pdisk_cart):
    Pdisk_to_Pdisk_cart.display()
    return


@app.cell
def _(Pdisk_to_Pdisk_cart, atan2, sqrt, u, v):
    Pdisk_to_Pdisk_cart.set_inverse(sqrt(u**2+v**2), atan2(v, u)) 
    Pdisk_to_Pdisk_cart.inverse().display()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The embedding of $\mathbb{H}^2$ in $\mathbb{R}^3$ associated with the Poincaré disk model is naturally defined as
    """)
    return


@app.cell
def _(H2, R3, X3, X_Pdisk_cart, u, v):
    Phi2 = H2.diff_map(R3, {(X_Pdisk_cart, X3): [u, v, 0]},
                       name='Phi_2', latex_name=r'\Phi_2')
    Phi2.display()
    return (Phi2,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Let us use it to draw the Poincaré disk in $\mathbb{R}^3$:
    """)
    return


@app.cell
def _(Phi2, X3, X_Pdisk_cart, show):
    graph_disk_uv = X_Pdisk_cart.plot(X3, mapping=Phi2, number_values=15)
    show(graph_disk_uv, figsize=7)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    On $U$, the change of coordinates $(r,\varphi) \rightarrow (u,v)$ is obtained by combining the changes $(r,\varphi) \rightarrow (R,\varphi)$ and $(R,\varphi) \rightarrow (u,v)$:
    """)
    return


@app.cell
def _(Pdisk_to_Pdisk_cart, pol_to_Pdisk):
    pol_to_Pdisk_cart = Pdisk_to_Pdisk_cart * pol_to_Pdisk
    pol_to_Pdisk_cart
    return (pol_to_Pdisk_cart,)


@app.cell
def _(pol_to_Pdisk_cart):
    pol_to_Pdisk_cart.display()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Still on $U$, the change of coordinates $(X,Y) \rightarrow (u,v)$ is obtained by combining the changes $(X,Y) \rightarrow (r,\varphi)$ with $(r,\varphi) \rightarrow (u,v)$:
    """)
    return


@app.cell
def _(pol_to_Pdisk_cart, pol_to_hyp):
    hyp_to_Pdisk_cart_U = pol_to_Pdisk_cart * pol_to_hyp.inverse()
    hyp_to_Pdisk_cart_U
    return (hyp_to_Pdisk_cart_U,)


@app.cell
def _(hyp_to_Pdisk_cart_U):
    hyp_to_Pdisk_cart_U.display()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We use the above expression to extend the change of coordinates $(X,Y) \rightarrow (u,v)$ from $U$ to the whole manifold $\mathbb{H}^2$:
    """)
    return


@app.cell
def _(X, X_Pdisk_cart, X_hyp, Y, hyp_to_Pdisk_cart_U):
    hyp_to_Pdisk_cart = X_hyp.transition_map(X_Pdisk_cart, hyp_to_Pdisk_cart_U(X,Y))
    hyp_to_Pdisk_cart
    return (hyp_to_Pdisk_cart,)


@app.cell
def _(hyp_to_Pdisk_cart):
    hyp_to_Pdisk_cart.display()
    return


@app.cell
def _(hyp_to_Pdisk_cart, u, v):
    hyp_to_Pdisk_cart.set_inverse(2*u/(1-u**2-v**2), 2*v/(1-u**2-v**2))
    hyp_to_Pdisk_cart.inverse().display()
    return


@app.cell
def _(Phi2, U, X3, X_pol, graph_hyp, r, show):
    graph_Pdisk = X_pol.plot(X3, mapping=Phi2.restrict(U), ranges={r: (0, 20)}, 
                             number_values=15, 
                             label_axes=False)
    show(graph_hyp + graph_Pdisk, aspect_ratio=1, figsize=7)
    return (graph_Pdisk,)


@app.cell
def _(X_Pdisk_cart, X_pol, r):
    X_pol.plot(X_Pdisk_cart, ranges={r: (0, 20)}, number_values=15)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Metric tensor in Poincaré disk coordinates $(u,v)$
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    From now on, we are using the Poincaré disk chart $(\mathbb{H}^2,(u,v))$ as the default one on $\mathbb{H}^2$:
    """)
    return


@app.cell
def _(H2, X_Pdisk_cart):
    H2.set_default_chart(X_Pdisk_cart)
    H2.set_default_frame(X_Pdisk_cart.frame())
    return


@app.cell
def _(X_hyp, g):
    g.display(X_hyp.frame())
    return


@app.cell
def _(g):
    g.display()
    return


@app.cell
def _(g):
    g[1,1].factor(); g[2,2].factor()
    g.display()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Hemispherical model

    The **hemispherical model of $\mathbb{H}^2$** is obtained by the inverse stereographic projection from the point $S = (0,0,-1)$ of the Poincaré disk to the unit sphere $X^2+Y^2+Z^2=1$. This induces a spherical coordinate chart on $U$:
    """)
    return


@app.cell
def _(U):
    X_spher = U.chart(r'th:(0,pi/2):\theta ph:(0,2*pi):\varphi')
    th_spher, ph_spher = X_spher[:]
    X_spher
    return X_spher, ph_spher, th_spher


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    From the stereographic projection from $S$, we obtain that $\sin\theta = \frac{2R}{1+R^2}$.

    Hence the transition map:
    """)
    return


@app.cell
def _(R, X_Pdisk, X_spher, arcsin, ph):
    Pdisk_to_spher = X_Pdisk.transition_map(X_spher, [arcsin(2*R/(1+R**2)), ph])
    Pdisk_to_spher
    return (Pdisk_to_spher,)


@app.cell
def _(Pdisk_to_spher):
    Pdisk_to_spher.display()
    return


@app.cell
def _(Pdisk_to_spher, cos, ph_spher, sin, th_spher):
    Pdisk_to_spher.set_inverse(sin(th_spher)/(1+cos(th_spher)), ph_spher)
    Pdisk_to_spher.inverse().display()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    In the spherical coordinates $(\theta,\varphi)$, the metric takes the following form:
    """)
    return


@app.cell
def _(X_spher, g):
    g.display(X_spher.frame(), X_spher)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The embedding of $\mathbb{H}^2$ in $\mathbb{R}^3$ associated with the hemispherical model is naturally:
    """)
    return


@app.cell
def _(H2, R3, X3, X_spher, cos, ph_spher, sin, th_spher):
    Phi3 = H2.diff_map(R3, {(X_spher, X3): [sin(th_spher)*cos(ph_spher), 
                                            sin(th_spher)*sin(ph_spher), 
                                            cos(th_spher)]},
                       name='Phi_3', latex_name=r'\Phi_3')
    Phi3.display()
    return (Phi3,)


@app.cell
def _(Phi3, X3, X_pol, graph_Pdisk, graph_hyp, r, show):
    graph_spher = X_pol.plot(X3, mapping=Phi3, ranges={r: (0, 20)}, number_values=15, 
                             color='orange', label_axes=False)
    show(graph_hyp + graph_Pdisk + graph_spher, aspect_ratio=1,  
         figsize=7)
    return (graph_spher,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Poincaré half-plane model

    The **Poincaré half-plane model of $\mathbb{H}^2$** is obtained by stereographic projection from the point $W=(-1,0,0)$ of the hemispherical model to the plane $X=1$. This induces a new coordinate chart on $\mathbb{H}^2$ by setting $(x,y)=(Y,Z)$ in the plane $X=1$:
    """)
    return


@app.cell
def _(H2):
    X_hplane = H2.chart('x y:(0,+oo)')
    x, y = X_hplane[:]
    X_hplane
    return X_hplane, x, y


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The coordinate transformation $(\theta,\varphi)\rightarrow (x,y)$ is easily deduced from the stereographic projection from the point $W$:
    """)
    return


@app.cell
def _(X_hplane, X_spher, cos, ph_spher, sin, th_spher):
    spher_to_hplane = X_spher.transition_map(
        X_hplane, 
        [2*sin(th_spher)*sin(ph_spher)/(1+sin(th_spher)*cos(ph_spher)),
         2*cos(th_spher)/(1+sin(th_spher)*cos(ph_spher))]
    )
    spher_to_hplane
    return (spher_to_hplane,)


@app.cell
def _(spher_to_hplane):
    spher_to_hplane.display()
    return


@app.cell
def _(Pdisk_to_spher, spher_to_hplane):
    Pdisk_to_hplane = spher_to_hplane * Pdisk_to_spher
    Pdisk_to_hplane
    return (Pdisk_to_hplane,)


@app.cell
def _(Pdisk_to_hplane):
    Pdisk_to_hplane.display()
    return


@app.cell
def _(Pdisk_to_Pdisk_cart, Pdisk_to_hplane):
    Pdisk_cart_to_hplane_U = Pdisk_to_hplane * Pdisk_to_Pdisk_cart.inverse()
    Pdisk_cart_to_hplane_U
    return (Pdisk_cart_to_hplane_U,)


@app.cell
def _(Pdisk_cart_to_hplane_U):
    Pdisk_cart_to_hplane_U.display()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Let us use the above formula to define the transition map $(u,v)\rightarrow (x,y)$ on the whole manifold $\mathbb{H}^2$ (and not only on $U$):
    """)
    return


@app.cell
def _(Pdisk_cart_to_hplane_U, X_Pdisk_cart, X_hplane, u, v):
    Pdisk_cart_to_hplane = X_Pdisk_cart.transition_map(X_hplane, 
                                                       Pdisk_cart_to_hplane_U(u,v))
    Pdisk_cart_to_hplane
    return (Pdisk_cart_to_hplane,)


@app.cell
def _(Pdisk_cart_to_hplane):
    Pdisk_cart_to_hplane.display()
    return


@app.cell
def _(Pdisk_cart_to_hplane, x, y):
    Pdisk_cart_to_hplane.set_inverse((4-x**2-y**2)/(x**2+(2+y)**2), 4*x/(x**2+(2+y)**2))
    Pdisk_cart_to_hplane.inverse().display()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Since the coordinates $(x,y)$ correspond to $(Y,Z)$ in the plane $X=1$, the embedding of $\mathbb{H}^2$ in $\mathbb{R}^3$ naturally associated with the Poincaré half-plane model is
    """)
    return


@app.cell
def _(H2, R3, X3, X_hplane, x, y):
    Phi4 = H2.diff_map(R3, {(X_hplane, X3): [1, x, y]}, 
                       name='Phi_4', latex_name=r'\Phi_4')
    Phi4.display()
    return (Phi4,)


@app.cell
def _(Phi4, U, X3, X_pol, graph_Pdisk, graph_hyp, graph_spher, r, show):
    graph_hplane = X_pol.plot(X3, mapping=Phi4.restrict(U), ranges={r: (0, 1.5)}, 
                              number_values=15, color='brown', label_axes=False)
    show(graph_hyp + graph_Pdisk + graph_spher + graph_hplane, 
         aspect_ratio=1, figsize=8)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Let us draw the grid of the hyperboloidal coordinates $(r,\varphi)$ in terms of the half-plane coordinates $(x,y)$:
    """)
    return


@app.cell
def _(Pdisk_to_hplane, pol_to_Pdisk):
    pol_to_hplane = Pdisk_to_hplane * pol_to_Pdisk
    return


@app.cell
def _(X_hplane, X_pol, ph, r, show):
    show(X_pol.plot(X_hplane, ranges={r: (0,24)}, 
                    style={r: '-', ph: '--'}, number_values=15, 
                    plot_points=200, color='brown'), 
         xmin=-5, xmax=5, ymin=0, ymax=5, 
         aspect_ratio=1)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The solid curves are those along which $r$ varies while $\varphi$ is kept constant. Conversely, the dashed curves are those along which $\varphi$ varies, while $r$ is kept constant. We notice that the former curves are arcs of circles orthogonal to the half-plane boundary $y=0$, hence they are geodesics of $(\mathbb{H}^2,g)$. This is not surprising since they correspond to the intersections of the hyperboloid with planes through the origin (namely the plane $\varphi=\mathrm{const}$). The point $(x,y) = (0,2)$ corresponds to $r=0$.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We may also depict the Poincaré disk coordinates $(u,v)$ in terms of the half-plane coordinates $(x,y)$:
    """)
    return


@app.cell
def _(X_Pdisk_cart, u, v):
    X_Pdisk_cart.plot(ranges={u: (-1, 0), v: (-1, 0)}, 
                      style={u: '-', v: '--'}) + \
    X_Pdisk_cart.plot(ranges={u: (-1, 0), v: (0., 1)}, 
                      style={u: '-', v: '--'}, color='orange') + \
    X_Pdisk_cart.plot(ranges={u: (0, 1), v: (-1, 0)}, 
                        style={u: '-', v: '--'}, color='pink') + \
    X_Pdisk_cart.plot(ranges={u: (0, 1), v: (0, 1)}, 
                      style={u: '-', v: '--'}, color='violet')
    return


@app.cell
def _(X_Pdisk_cart, X_hplane, show, u, v):
    show(X_Pdisk_cart.plot(X_hplane, ranges={u: (-1, 0), v: (-1, 0)}, 
                           style={u: '-', v: '--'}) + \
         X_Pdisk_cart.plot(X_hplane, ranges={u: (-1, 0), v: (0, 1)}, 
                           style={u: '-', v: '--'}, color='orange') + \
         X_Pdisk_cart.plot(X_hplane, ranges={u: (0, 1), v: (-1, 0)}, 
                           style={u: '-', v: '--'}, color='pink') + \
         X_Pdisk_cart.plot(X_hplane, ranges={u: (0, 1), v: (0, 1)}, 
                           style={u: '-', v: '--'}, color='violet'),
         xmin=-5, xmax=5, ymin=0, ymax=5, aspect_ratio=1)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The expression of the metric tensor in the half-plane coordinates $(x,y)$ is
    """)
    return


@app.cell
def _(X_hplane, g):
    g.display(X_hplane.frame(), X_hplane)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Summary

    9 charts have been defined on $\mathbb{H}^2$:
    """)
    return


@app.cell
def _(H2):
    H2.atlas()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    There are actually 6 main (top) charts, the other ones being subcharts:
    """)
    return


@app.cell
def _(H2):
    H2.top_charts()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The expression of the metric tensor in each of these charts is
    """)
    return


@app.cell
def _(H2, g, show):
    for chart in H2.top_charts():
        show(g.display(chart.frame(), chart))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    For each of these charts, the non-vanishing (and non-redundant w.r.t. the symmetry on the last 2 indices) **Christoffel symbols of $g$** are
    """)
    return


@app.cell
def _(H2, g, show):
    for chart_1 in H2.top_charts():
        show(chart_1)
        show(g.christoffel_symbols_display(chart=chart_1))
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
