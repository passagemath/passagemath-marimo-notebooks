# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "marimo>=0.20.4",
#     "passagemath-maxima==10.8.2",
#     "passagemath-plot==10.8.2",
#     "passagemath-repl==10.8.2",
#     "passagemath-symbolics[maxima,plot,test]==10.8.2",
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
    # SageManifolds example notebook using [passagemath](https://github.com/passagemath): The sphere $\mathbb{S}^2$
    """)
    return


@app.cell
def _():
    import marimo as mo
    import passagemath_maxima
    from passagemath_symbolics import (
        RR, SR, sin, cos, atan, atan2, pi, sqrt, exp, oo, diff, factor,
        Manifold, EuclideanSpace, manifolds, Hom, FiniteRankFreeModule, dim, 
    )
    from passagemath_plot import show, sphere
    from passagemath_repl import get_display_manager; dm = get_display_manager()
    return (
        EuclideanSpace,
        FiniteRankFreeModule,
        Hom,
        Manifold,
        RR,
        SR,
        atan,
        atan2,
        cos,
        diff,
        dim,
        exp,
        factor,
        manifolds,
        mo,
        oo,
        pi,
        show,
        sin,
        sphere,
        sqrt,
    )


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    This marimo notebook, adapted from a Jupyter notebook published in https://sagemanifolds.obspm.fr/examples.html, demonstrates some differential geometry capabilities of SageMath on the example of the 2-dimensional sphere.

    The corresponding tools have been developed within
    the [SageManifolds](https://sagemanifolds.obspm.fr) project. They are now available in Python environments via the modularized distributions of the Sage library developed by the [passagemath](https://github.com/passagemath) project.
    - The SageManifolds functionality is shipped as part of [passagemath-symbolics](https://pypi.org/project/passagemath-symbolics/).
    - The pip-installable package [passagemath-maxima](https://pypi.org/project/passagemath-maxima/) provides the backend for symbolic computation.
    - [passagemath-plot](https://pypi.org/project/passagemath-plot/) provides 2D and 3D plotting facilities.
    - [passagemath-repl](https://pypi.org/project/passagemath-repl/) provides the integration with the marimo notebook.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## $\mathbb{S}^2$ from the manifold catalog
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The 2-sphere, with predefined charts and embedding in the Euclidean 3-space, can be obtained directly from SageMath's manifold catalog:
    """)
    return


@app.cell
def _(manifolds):
    S2 = manifolds.Sphere(2)
    S2
    return (S2,)


@app.cell
def _(S2):
    print(S2)
    return


@app.cell
def _(S2):
    S2.spherical_coordinates()
    return


@app.cell
def _(S2):
    S2.metric().display()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## $\mathbb{S}^2$ defined from scratch as a 2-dimensional smooth manifold
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    For the purpose of introducing generic smooth manifolds in SageMath, we shall not use the above predefined object. Instead we shall construct $\mathbb{S}^2$ from scratch, by invoking the generic function `Manifold`:
    """)
    return


@app.cell
def _(Manifold):
    S2_1 = Manifold(2, 'S^2', latex_name='\\mathbb{S}^2', start_index=1)
    return (S2_1,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The first argument, `2`, is the dimension of the manifold, while the second argument is the symbol used to label the manifold.

    The argument `start_index` sets the index range to be used on the manifold for labelling components w.r.t. a basis or a frame: `start_index=1` corresponds to $\{1,2\}$; the default value is `start_index=0` and yields $\{0,1\}$.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The function `Manifold` has actually many options.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    By default `Manifold` constructs a smooth manifold over $\mathbb{R}$:
    """)
    return


@app.cell
def _(S2_1):
    print(S2_1)
    return


@app.cell
def _(S2_1):
    S2_1
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    $\mathbb{S}^2$ is in the category of smooth manifolds over $\mathbb{R}$:
    """)
    return


@app.cell
def _(S2_1):
    S2_1.category()
    return


@app.cell
def _(S2_1):
    print(S2_1.category())
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    At the moment, the real field $\mathbb{R}$ is modeled by 53-bit floating-point approximations, but this plays no role in the manifold implementation:
    """)
    return


@app.cell
def _(S2_1):
    print(S2_1.base_field())
    return


@app.cell
def _(RR, S2_1):
    S2_1.base_field() is RR
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Coordinate charts on $\mathbb{S}^2$

    The function `Manifold` generates a manifold with no-predefined coordinate chart, so that the manifold (user) **atlas** is empty:
    """)
    return


@app.cell
def _(S2_1):
    S2_1.atlas()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Let us introduce some charts. At least two charts are necessary to cover the sphere. Let us choose the charts associated with the **stereographic projections** to the equatorial plane from the North pole and the South pole respectively. We first introduce the open subsets covered by these two charts:
    $$ U := \mathbb{S}^2\setminus\{N\}, $$
    $$ V := \mathbb{S}^2\setminus\{S\}, $$
    where $N$ is a point of $\mathbb{S}^2$, which we shall call the **North pole**, and $S$ is the point of $U$ of stereographic coordinates $(0,0)$, which we call the **South pole**:
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    To find the method to create an open subset, we type `U = S2_1.<TAB>` to get the list of possible methods by autocompletion:
    """)
    return


@app.cell
def _(S2_1):
    U = S2_1.open_subset('U')
    print(U)
    return (U,)


@app.cell
def _(S2_1):
    V = S2_1.open_subset('V')
    print(V)
    return (V,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    As an open subset of a smooth manifold, $U$ is itself a smooth manifold:
    """)
    return


@app.cell
def _(U):
    print(U.category())
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We declare that $\mathbb{S}^2 = U \cup V$:
    """)
    return


@app.cell
def _(S2_1, U, V):
    S2_1.declare_union(U, V)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The **stereographic chart** on $U$ is constructed from the stereographic projection from the North pole onto the equatorial plane: in the [Wikipedia figure](https://en.wikipedia.org/wiki/Stereographic_projection), the stereographic coordinates $(x,y)$ of the point $P\in U$ are the Cartesian coordinates of the point $P'$ in the equatorial plane.

    We call this chart `stereoN` and construct it via the method `chart`:
    """)
    return


@app.cell
def _(U):
    stereoN = U.chart(names=['x', 'y']); x, y = stereoN[:]
    return stereoN, x, y


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The function `chart()` has no argument other than to specify the coordinate names, which implies that the coordinate symbols will be `x` and `y` and that each coordinate range is $(-\infty,+\infty)$. As we will see below, for other cases, an argument must be passed to `chart()`  to specify each coordinate symbol and range, as well as some specific LaTeX symbol.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The chart created by the above command:
    """)
    return


@app.cell
def _(stereoN):
    stereoN
    return


@app.cell
def _(stereoN):
    print(stereoN)
    return


@app.cell
def _(stereoN):
    stereoN.coord_range()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The coordinates can be accessed individually, either by means of their indices in the chart ( following the convention `start_index=1` set in the manifold's definition) or by their names as Python variables:
    """)
    return


@app.cell
def _(stereoN):
    stereoN[1]
    return


@app.cell
def _(stereoN, y):
    y is stereoN[2]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The coordinates are SageMath symbolic expressions:
    """)
    return


@app.cell
def _(y):
    type(y)
    return


@app.cell
def _(y):
    y.parent()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### Stereographic coordinates from the South Pole

    We introduce on $V$ the coordinates $(x',y')$ corresponding to the stereographic projection from the South pole:
    """)
    return


@app.cell
def _(V):
    stereoS = V.chart("xp:x' yp:y'"); xp, yp = stereoS[:]
    return stereoS, xp, yp


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    In this case, the string argument passed to `chart` stipulates that the text-only names of the coordinates are xp and yp (same as the Python variables names defined afterwards), while their LaTeX names are $x'$ and $y'$.
    """)
    return


@app.cell
def _(stereoS):
    stereoS
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    At this stage, the user's atlas on the manifold is made of two charts:
    """)
    return


@app.cell
def _(S2_1):
    S2_1.atlas()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    To complete the construction of the manifold structure, we have
    to specify the <strong>transition map</strong> between the charts `stereoN` = $(U,(x,y))$ and `stereoS` = $(V,(x',y'))$; it is given by standard inversion formulas:
    """)
    return


@app.cell
def _(stereoN, stereoS, x, xp, y, yp):
    stereoN_to_S = stereoN.transition_map(stereoS, 
                                          (x/(x**2+y**2), y/(x**2+y**2)), 
                                          intersection_name='W',
                                          restrictions1=(x**2 + y**2 != 0), 
                                          restrictions2=(xp**2 + yp**2 != 0))
    stereoN_to_S.display()
    return (stereoN_to_S,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    In the above declaration, 'W' is the name given to the chart-overlap subset: $W := U\cap V$, the condition $x^2+y^2 \not=0$  defines $W$ as a subset of $U$, and the condition $x'^2+y'^2\not=0$ defines $W$ as a subset of $V$.

    The inverse coordinate transformation is computed by means of the method `inverse()`:
    """)
    return


@app.cell
def _(stereoN_to_S):
    stereoS_to_N = stereoN_to_S.inverse()
    stereoS_to_N.display()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <p>In the present case, the situation is of course perfectly symmetric regarding the coordinates $(x,y)$ and $(x',y')$.</p>
    <p>At this stage, the user's atlas has four charts:</p>
    """)
    return


@app.cell
def _(S2_1):
    S2_1.atlas()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Let us store $W = U\cap V$ into a Python variable for future use:
    """)
    return


@app.cell
def _(U, V):
    W = U.intersection(V)
    return (W,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Similarly we store the charts $(W,(x,y))$ (the restriction of  $(U,(x,y))$ to $W$) and $(W,(x',y'))$ (the restriction of $(V,(x',y'))$ to $W$) into Python variables:
    """)
    return


@app.cell
def _(W, stereoN):
    stereoN_W = stereoN.restrict(W)
    stereoN_W
    return (stereoN_W,)


@app.cell
def _(S2_1, stereoN_W):
    stereoN_W is S2_1.atlas()[2]
    return


@app.cell
def _(W, stereoS):
    stereoS_W = stereoS.restrict(W)
    stereoS_W
    return (stereoS_W,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Coordinate charts are endowed with a method `plot()`. For instance,
    we may plot the chart $(W, (x',y'))$ in terms of itself, as a grid:
    """)
    return


@app.cell
def _(stereoS_W):
    stereoS_W.plot()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    More interestingly, let us plot the stereographic chart $(x',y')$ in terms of the stereographic chart $(x,y)$ on the domain $W$ where both systems overlap. We split the plot in four parts to avoid the singularity at $(x',y')=(0,0)$ and
    ask for the coordinate lines along which $x'$ (resp. $y'$) varies to be colored in purple (resp. cyan):
    """)
    return


@app.cell
def _(stereoN, stereoS_W, xp, yp):
    graph = (stereoS_W.plot(stereoN, ranges={xp:[-6,-0.02], yp:[-6,-0.02]},
                              color={xp: 'purple', yp: 'cyan'}) 
             + stereoS_W.plot(stereoN, ranges={xp:[-6,-0.02], yp:[0.02,6]},
                              color={xp: 'purple', yp: 'cyan'})
             + stereoS_W.plot(stereoN, ranges={xp:[0.02,6], yp:[-6,-0.02]},
                              color={xp: 'purple', yp: 'cyan'})
             + stereoS_W.plot(stereoN, ranges={xp:[0.02,6], yp:[0.02,6]},
                              color={xp: 'purple', yp: 'cyan'}))
    graph.show(xmin=-1.5, xmax=1.5, ymin=-1.5, ymax=1.5)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Spherical coordinates

    The standard **spherical coordinates** $(\theta,\phi)$ are defined on the open domain $A\subset W \subset \mathbb{S}^2$ that is the complement of the "origin meridian"; since the latter is the half-circle defined by $y=0$ and $x\geq 0$, we declare:
    """)
    return


@app.cell
def _(W, stereoN_W, stereoS_W, x, xp, y, yp):
    A = W.open_subset('A', coord_def={stereoN_W: (y!=0, x<0), 
                                      stereoS_W: (yp!=0, xp<0)})
    print(A)
    return (A,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The restriction of the stereographic chart from the North pole to $A$ is
    """)
    return


@app.cell
def _(A, stereoN_W):
    stereoN_A = stereoN_W.restrict(A)
    stereoN_A
    return (stereoN_A,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We then declare the chart $(A,(\theta,\phi))$ by specifying the intervals $(0,\pi)$ and $(0,2\pi)$ spanned by respectively $\theta$ and $\phi$:
    """)
    return


@app.cell
def _(A):
    spher = A.chart(r'th:(0,pi):\theta ph:(0,2*pi):\phi'); th, ph = spher[:]
    spher
    return ph, spher, th


@app.cell
def _(spher):
    spher.coord_range()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The specification of the spherical coordinates is completed by providing the transition map with the stereographic chart $(A,(x,y))$:
    """)
    return


@app.cell
def _(cos, ph, sin, spher, stereoN_A, th):
    spher_to_stereoN = spher.transition_map(stereoN_A, 
                                            (sin(th)*cos(ph)/(1-cos(th)),
                                             sin(th)*sin(ph)/(1-cos(th))))
    spher_to_stereoN.display()
    return (spher_to_stereoN,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We also provide the inverse transition map:
    """)
    return


@app.cell
def _(atan, atan2, pi, spher_to_stereoN, sqrt, x, y):
    spher_to_stereoN.set_inverse(2*atan(1/sqrt(x**2+y**2)), atan2(-y,-x)+pi)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The check is passed, modulo some lack of trigonometric simplifications in the first two lines.
    """)
    return


@app.cell
def _(spher_to_stereoN):
    spher_to_stereoN.inverse().display()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The transition map $(A,(\theta,\phi))\rightarrow (A,(x',y'))$ is obtained by combining the transition maps $(A,(\theta,\phi))\rightarrow (A,(x,y))$ and $(A,(x,y))\rightarrow (A,(x',y'))$ via the operator `*`:
    """)
    return


@app.cell
def _(A, spher_to_stereoN, stereoN_to_S):
    stereoN_to_S_A = stereoN_to_S.restrict(A)
    spher_to_stereoS = stereoN_to_S_A * spher_to_stereoN
    spher_to_stereoS.display()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Similarly, the transition map $(A,(x',y'))\rightarrow (A,(\theta,\phi))$ is obtained by combining the transition maps $(A,(x',y'))\rightarrow (A,(x,y))$ and $(A,(x,y))\rightarrow (A,(\theta,\phi))$:
    """)
    return


@app.cell
def _(A, spher_to_stereoN, stereoN_to_S):
    stereoS_to_N_A = stereoN_to_S.inverse().restrict(A)
    stereoS_to_spher = spher_to_stereoN.inverse() * stereoS_to_N_A 
    stereoS_to_spher.display()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The user atlas of $\mathbb{S}^2$ is now
    """)
    return


@app.cell
def _(S2_1):
    S2_1.atlas()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Let us draw the grid of spherical coordinates $(\theta,\phi)$ in terms of stereographic coordinates from the North pole $(x,y)$:
    """)
    return


@app.cell
def _(pi, spher, stereoN, th):
    spher.plot(stereoN, number_values=15, ranges={th: (pi/8,pi)})
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Points on $\mathbb{S}^2$

    To create a point on $\mathbb{S}^2$, we use SageMath's ***parent / element*** syntax, i.e. the call operator `S2(...)` acting on the parent `S2`, with the point's coordinates in some chart as argument.

    For instance, we declare the **North pole** (resp. the **South pole**) as the point of coordinates $(0,0)$ in the chart $(V,(x',y'))$ (resp. in the chart $(U,(x,y))$):
    """)
    return


@app.cell
def _(S2_1, stereoS):
    N = S2_1((0, 0), chart=stereoS, name='N')
    print(N)
    return (N,)


@app.cell
def _(S2_1, stereoN):
    S = S2_1((0, 0), chart=stereoN, name='S')
    print(S)
    return (S,)


@app.cell
def _(N):
    N.parent()
    return


@app.cell
def _(S):
    S.parent()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <p>We have of course</p>
    """)
    return


@app.cell
def _(N, S2_1):
    N in S2_1
    return


@app.cell
def _(N, U):
    N in U
    return


@app.cell
def _(N, V):
    N in V
    return


@app.cell
def _(A, N):
    N in A
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Let us introduce some point $p$ of stereographic coordinates $(x,y) = (1,2)$:
    """)
    return


@app.cell
def _(S2_1, stereoN):
    p = S2_1((1, 2), chart=stereoN, name='p')
    return (p,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    $p$ lies in the open subset $A$:
    """)
    return


@app.cell
def _(A, p):
    p in A
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### Charts acting on points
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    By definition, a chart maps points to pairs of real numbers (the point's coordinates):
    """)
    return


@app.cell
def _(p, stereoN):
    stereoN(p)  # by definition of p
    return


@app.cell
def _(p, stereoS):
    stereoS(p)
    return


@app.cell
def _(p, spher):
    spher(p)
    return


@app.cell
def _(N, stereoS):
    stereoS(N)
    return


@app.cell
def _():
    #stereoN(N)   ## raises an error
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Maps between manifolds: the embedding of $\mathbb{S}^2$ into $\mathbb{R}^3$

    Let us first declare $\mathbb{R}^3$ as the 3-dimensional Euclidean space, denoting the Cartesian coordinates by
    $(X,Y,Z)$:
    """)
    return


@app.cell
def _(EuclideanSpace):
    R3 = EuclideanSpace(name='R^3', names=['X', 'Y', 'Z'], latex_name=r'\mathbb{R}^3', 
                        metric_name='h')
    cartesian = R3.cartesian_coordinates()
    cartesian
    return R3, cartesian


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    As an Euclidean space, `R3` is considered by Sage as a smooth manifold:
    """)
    return


@app.cell
def _(R3):
    print(R3.category())
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The embedding $\Phi: \mathbb{S}^2 \longmapsto \mathbb{R}^3$ is then defined via the method `diff_map` by providing the standard formulas relating the stereographic coordinates to the ambient Cartesian ones when considering the **stereographic projection** from the point $(0,0,1)$ (North pole) or $(0, 0, -1)$ (South pole) to the equatorial plane $Z=0$:
    """)
    return


@app.cell
def _(R3, S2_1, cartesian, stereoN, stereoS, x, xp, y, yp):
    Phi = S2_1.diff_map(R3, {
        (stereoN, cartesian): [2 * x / (1 + x**2 + y**2), 
                               2 * y / (1 + x**2 + y**2), 
                               (x**2 + y**2 - 1) / (1 + x**2 + y**2)], 
        (stereoS, cartesian): [2 * xp / (1 + xp**2 + yp**2), 
                               2 * yp / (1 + xp**2 + yp**2), 
                               (1 - xp**2 - yp**2) / (1 + xp**2 + yp**2)]
    }, name='Phi', latex_name='\\Phi')
    return (Phi,)


@app.cell
def _(Phi):
    Phi.display()
    return


@app.cell
def _(Phi):
    Phi.parent()
    return


@app.cell
def _(Phi):
    print(Phi.parent())
    return


@app.cell
def _(Hom, Phi, R3, S2_1):
    Phi.parent() is Hom(S2_1, R3)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    $\Phi$ maps points of $\mathbb{S}^2$ to points of $\mathbb{R}^3$:
    """)
    return


@app.cell
def _(N, Phi):
    N1 = Phi(N)
    print(N1)
    N1
    return (N1,)


@app.cell
def _(N1, cartesian):
    cartesian(N1)
    return


@app.cell
def _(Phi, S):
    S1 = Phi(S)
    print(S1)
    S1
    return (S1,)


@app.cell
def _(S1, cartesian):
    cartesian(S1)
    return


@app.cell
def _(Phi, p):
    p1 = Phi(p)
    print(p1)
    p1
    return (p1,)


@app.cell
def _(cartesian, p1):
    cartesian(p1)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    $\Phi$ has been defined in terms of the stereographic charts $(U,(x,y))$ and $(V,(x',y'))$, but we may ask its expression in terms of spherical coordinates. This triggers a computation involving the transition map $(A,(x,y))\rightarrow (A,(\theta,\phi))$:
    """)
    return


@app.cell
def _(Phi, cartesian, stereoN_A):
    Phi.display(stereoN_A, cartesian)
    return


@app.cell
def _(Phi, cartesian, spher):
    Phi.display(spher, cartesian)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Let us use $\Phi$ to draw the grid of spherical coordinates $(\theta,\phi)$ in terms of the Cartesian coordinates $(X,Y,Z)$ of $\mathbb{R}^3$:
    """)
    return


@app.cell
def _(Phi, cartesian, spher):
    graph_spher = spher.plot(chart=cartesian, mapping=Phi, number_values=11, 
                             color='blue', label_axes=False)
    graph_spher
    return (graph_spher,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We may also use the embedding $\Phi$ to display the stereographic coordinate grid in terms of the Cartesian coordinates in $\mathbb{R}^3$. First for the stereographic coordinates from the North pole:
    """)
    return


@app.cell
def _(Phi, cartesian, stereoN):
    graph_1 = stereoN.plot(chart=cartesian, mapping=Phi, number_values=25,      
                           label_axes=False)
    graph_1
    return (graph_1,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <p>and then have a view with the stereographic coordinates from the South pole superposed (in green):</p>
    """)
    return


@app.cell
def _(Phi, cartesian, graph_1, stereoS):
    graph_2 = graph_1 + stereoS.plot(chart=cartesian, mapping=Phi, number_values=25, color='green', label_axes=False)
    graph_2
    return (graph_2,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We may add the points $N$, $S$ and $p$ to the graphic, thanks to the method `plot` of points:
    """)
    return


@app.cell
def _(N, Phi, S, cartesian, graph_2, p):
    graph_3 = graph_2 + N.plot(chart=cartesian, mapping=Phi, color='red', 
                               label_offset=0.05)
    graph_3 = graph_3 + S.plot(chart=cartesian, mapping=Phi, color='green', 
                               label_offset=0.05)
    graph_3 = graph_3 + p.plot(chart=cartesian, mapping=Phi, color='blue', 
                               label_offset=0.05)
    graph_3
    return (graph_3,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Tangent spaces

    The **tangent space** to the manifold $\mathbb{S}^2$ at the point $p$ is
    """)
    return


@app.cell
def _(S2_1, p):
    Tp = S2_1.tangent_space(p)
    print(Tp)
    Tp
    return (Tp,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    $T_p \mathbb{S}^2$ is a vector space over $\mathbb{R}$ (represented here by Sage's symbolic ring SR):
    """)
    return


@app.cell
def _(Tp):
    print(Tp.category())
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <p>Its dimension equals the manifold's dimension:</p>
    """)
    return


@app.cell
def _(Tp, dim):
    dim(Tp)
    return


@app.cell
def _(S2_1, Tp, dim):
    dim(Tp) == dim(S2_1)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The tangent space at $p$ is the **fiber over** $p$ of the **tangent bundle** $T\mathbb{S}^2$:
    """)
    return


@app.cell
def _(S2_1, Tp, p):
    Tp is S2_1.tangent_bundle().fiber(p)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The vector space $T_p \mathbb{S}^2$ is endowed with bases inherited from the coordinate frames defined around $p$:
    """)
    return


@app.cell
def _(Tp):
    Tp.bases()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    On the contrary, since $(V,(x',y'))$ is the only chart defined so far around the point $N$,
    we have a unique predefined basis in $T_N \mathbb{S}^2$:
    """)
    return


@app.cell
def _(N, S2_1):
    T_N = S2_1.tangent_space(N)
    T_N.bases()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    To shorten some writings, there is the concept of default basis:
    """)
    return


@app.cell
def _(Tp):
    Tp.default_basis()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    An element of $T_p\mathbb{S}^2$ is constructed via SageMath's *parent/element* syntax, i.e. via the call method of the parent:
    """)
    return


@app.cell
def _(Tp):
    v = Tp((-2, 3), name='v')
    print(v)
    return (v,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Equivalently, one can use the method `tangent_vector` of manifolds:
    """)
    return


@app.cell
def _(S2_1, p, v):
    v == S2_1.tangent_vector(p, -2, 3, name='v')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    One has of course:
    """)
    return


@app.cell
def _(Tp, v):
    v in Tp
    return


@app.cell
def _(v):
    v.parent()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The vector $v$ expanded in the default basis of $T_p \mathbb{S}^2$:
    """)
    return


@app.cell
def _(v):
    v.display()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Expansion in other bases:
    """)
    return


@app.cell
def _(Tp, v):
    v.display(Tp.bases()[1])
    return


@app.cell
def _(Tp, v):
    v.display(Tp.bases()[2])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Tangent vectors are endowed with a method `plot`:
    """)
    return


@app.cell
def _(Phi, cartesian, graph_3, v):
    graph_4 = graph_3 + v.plot(chart=cartesian, mapping=Phi, scale=0.2, width=0.5)
    graph_4
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Differential of a smooth map

    The differential of the map $\Phi$ at the point $p$ is
    """)
    return


@app.cell
def _(Phi, p):
    dPhi_p = Phi.differential(p)
    print(dPhi_p)
    dPhi_p
    return (dPhi_p,)


@app.cell
def _(dPhi_p):
    dPhi_p.domain()
    return


@app.cell
def _(dPhi_p):
    dPhi_p.codomain()
    return


@app.cell
def _(dPhi_p):
    dPhi_p.parent()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The image by $\mathrm{d}\Phi_p$ of the vector $v\in T_p\mathbb{S}^2$ introduced above is
    """)
    return


@app.cell
def _(dPhi_p, v):
    dPhi_p(v)
    return


@app.cell
def _(dPhi_p, v):
    print(dPhi_p(v))
    return


@app.cell
def _(Phi, R3, dPhi_p, p, v):
    dPhi_p(v) in R3.tangent_space(Phi(p))
    return


@app.cell
def _(dPhi_p, v):
    dPhi_p(v).display()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Algebra of scalar fields

    The set $C^\infty(\mathbb{S}^2)$ of all smooth functions $\mathbb{S}^2\rightarrow \mathbb{R}$ has naturally the structure of a commutative algebra over $\mathbb{R}$. $C^\infty(\mathbb{S}^2)$ is therefore returned by the method `scalar_field_algebra()` of manifolds:
    """)
    return


@app.cell
def _(S2_1):
    CS = S2_1.scalar_field_algebra()
    CS
    return (CS,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Since the algebra internal product is the pointwise multiplication, it is clearly commutative, so that $C^\infty(\mathbb{S}^2)$ belongs to Sage's category of commutative algebras:
    """)
    return


@app.cell
def _(CS):
    print(CS.category())
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The base ring of the algebra $C^\infty(\mathbb{S}^2)$ is the field $\mathbb{R}$, which is represented here by Sage's Symbolic Ring (SR):
    """)
    return


@app.cell
def _(CS):
    CS.base_ring()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Elements of $C^\infty(\mathbb{S}^2)$ are of course (smooth) scalar fields:
    """)
    return


@app.cell
def _(CS):
    print(CS.an_element())
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <p>This example element is the constant scalar field that takes the value 2:</p>
    """)
    return


@app.cell
def _(CS):
    CS.an_element().display()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <p>A specific element is the zero one:</p>
    """)
    return


@app.cell
def _(CS):
    f = CS.zero()
    print(f)
    return (f,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Scalar fields map points of $\mathbb{S}^2$ to real numbers:
    """)
    return


@app.cell
def _(N, S, f, p):
    f(N), f(S), f(p)
    return


@app.cell
def _(f):
    f.display()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <p>Another specific element is the algebra unit element, i.e. the constant scalar field 1:</p>
    """)
    return


@app.cell
def _(CS):
    f_1 = CS.one()
    print(f_1)
    return (f_1,)


@app.cell
def _(N, S, f_1, p):
    (f_1(N), f_1(S), f_1(p))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    A generic scalar field is defined by its coordinate expression in some chart(s); for instance:
    """)
    return


@app.cell
def _(S2_1, stereoN, x, y):
    f_2 = S2_1.scalar_field({stereoN: 1 / (1 + x**2 + y**2)}, name='f')
    f_2.display()
    return (f_2,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We see that Sage has used the transition map between the two stereographic charts on $W$ to express $f$ in terms of the coordinates $(x',y')$ on $W$. Let us this expression to extend $f$ to the whole of $V$:
    """)
    return


@app.cell
def _(W, f_2, stereoS):
    f_2.add_expr_by_continuation(stereoS, W)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Then $f$ is well defined in all $\mathbb{S}^2 = U \cup V$:
    """)
    return


@app.cell
def _(f_2):
    f_2.display()
    return


@app.cell
def _(N, f_2):
    f_2(N)
    return


@app.cell
def _(f_2):
    f_2.parent()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <p>Scalar fields map the manifold's points to real numbers:</p>
    """)
    return


@app.cell
def _(N, f_2):
    f_2(N)
    return


@app.cell
def _(S, f_2):
    f_2(S)
    return


@app.cell
def _(f_2, p):
    f_2(p)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We may define the restrictions of $f$ to the open subsets $U$ and $V$:
    """)
    return


@app.cell
def _(U, f_2):
    fU = f_2.restrict(U)
    fU.display()
    return (fU,)


@app.cell
def _(V, f_2):
    fV = f_2.restrict(V)
    fV.display()
    return (fV,)


@app.cell
def _(S, fU, p):
    fU(p), fU(S)
    return


@app.cell
def _(fU):
    fU.parent()
    return


@app.cell
def _(fV):
    fV.parent()
    return


@app.cell
def _(U, fU):
    CU = U.scalar_field_algebra()
    fU.parent() is CU
    return (CU,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    A scalar field on $\mathbb{S}^2$ can be coerced to a scalar field on $U$, the coercion being simply the restriction:
    """)
    return


@app.cell
def _(CS, CU):
    CU.has_coerce_map_from(CS)
    return


@app.cell
def _(CU, fU, f_2):
    fU == CU(f_2)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The arithmetic of scalar fields (operations in the algebra $C^\infty(\mathbb{S}^2)$):
    """)
    return


@app.cell
def _(f_2):
    g = f_2 * f_2 - 2 * f_2
    g.set_name('g')
    g.display()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Vector fields

    The set $\mathfrak{X}(\mathbb{S}^2)$ of all smooth vector fields on $\mathbb{S}^2$ is a module over the algebra $C^\infty(\mathbb{S}^2)$. It is obtained by the method `vector_field_module()`:
    """)
    return


@app.cell
def _(S2_1):
    XS = S2_1.vector_field_module()
    XS
    return (XS,)


@app.cell
def _(XS):
    print(XS)
    return


@app.cell
def _(XS):
    XS.base_ring()
    return


@app.cell
def _(XS):
    XS.category()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    $\mathfrak{X}(\mathbb{S}^2)$ is not a free module:
    """)
    return


@app.cell
def _(FiniteRankFreeModule, XS):
    isinstance(XS, FiniteRankFreeModule)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    because $\mathbb{S}^2$ is not a parallelizable manifold:
    """)
    return


@app.cell
def _(S2_1):
    S2_1.is_manifestly_parallelizable()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    On the contrary, the set $\mathfrak{X}(U)$ of smooth vector fields on $U$ is a free module:
    """)
    return


@app.cell
def _(FiniteRankFreeModule, U):
    XU = U.vector_field_module()
    isinstance(XU, FiniteRankFreeModule)
    return (XU,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    because $U$ is parallelizable:
    """)
    return


@app.cell
def _(U):
    U.is_manifestly_parallelizable()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Due to the introduction of the stereographic coordinates $(x,y)$ on $U$, a basis has already been defined on the free module $\mathfrak{X}(U)$, namely the coordinate basis $(\partial/\partial x, \partial/\partial y)$:
    """)
    return


@app.cell
def _(XU):
    XU.print_bases()
    return


@app.cell
def _(XU):
    eU = XU.default_basis()
    eU
    return (eU,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <p>Similarly</p>
    """)
    return


@app.cell
def _(V):
    XV = V.vector_field_module()
    eV = XV.default_basis()
    eV
    return (eV,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    From the point of view of the open set $U$, `eU` is also the default vector frame:
    """)
    return


@app.cell
def _(U, eU):
    eU is U.default_frame()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Similarly:
    """)
    return


@app.cell
def _(V, eV):
    eV is V.default_frame()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `eU` is also the default vector frame on $\mathbb{S}^2$ (although not defined on the whole $\mathbb{S}^2$), for it is the first vector frame defined on an open subset of $\mathbb{S}^2$:
    """)
    return


@app.cell
def _(S2_1, eU):
    eU is S2_1.default_frame()
    return


@app.cell
def _(S2_1):
    S2_1.frames()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Let us introduce a vector field on $\mathbb{S}^2$ by providing its components in the
    frame `eU`:
    """)
    return


@app.cell
def _(S2_1, eU):
    v_1 = S2_1.vector_field(1, -2, frame=eU, name='v')
    v_1.display(eU)
    return (v_1,)


@app.cell
def _(v_1):
    v_1.parent()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    On $W$, we can express $v$ in terms of the $(x',y')$ coordinates:
    """)
    return


@app.cell
def _(W, stereoS, v_1):
    v_1.restrict(W).display(stereoS.restrict(W).frame(), stereoS.restrict(W))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We extend the definition of $v$ to $V$ thanks to the above expression:
    """)
    return


@app.cell
def _(W, eV, stereoS, v_1):
    v_1.add_comp_by_continuation(eV, W, chart=stereoS)
    v_1.display(eV)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    At this stage, the vector field $v$ is defined on the whole manifold $\mathbb{S}^2$: it has expressions in each of the two frames `eU` and `eV`, which cover $\mathbb{S}^2$.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    According to the hairy ball theorem, $v$ has to vanish somewhere. This occurs at the North pole:
    """)
    return


@app.cell
def _(N, v_1):
    vN = v_1.at(N)
    print(vN)
    return (vN,)


@app.cell
def _(vN):
    vN.display()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    $v|_N$ is the zero vector of the tangent vector space $T_N\mathbb{S}^2$:
    """)
    return


@app.cell
def _(vN):
    vN.parent()
    return


@app.cell
def _(N, S2_1, vN):
    vN.parent() is S2_1.tangent_space(N)
    return


@app.cell
def _(N, S2_1, vN):
    vN == S2_1.tangent_space(N).zero()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    On the contrary, $v$ is non-zero at the South pole:
    """)
    return


@app.cell
def _(S, v_1):
    vS = v_1.at(S)
    print(v_1)
    return (vS,)


@app.cell
def _(vS):
    vS.display()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Let us plot the vector field $v$ is terms of the stereographic chart $(U,(x,y))$, with the South pole $S$ superposed:
    """)
    return


@app.cell
def _(S, stereoN, v_1):
    v_1.plot(chart=stereoN, chart_domain=stereoN, max_range=4, number_values=5, scale=0.5, aspect_ratio=1) + S.plot(stereoN, size=30, label_offset=0.2)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The vector field appears homogeneous because its components w.r.t. the frame $\left(\frac{\partial}{\partial x}, \frac{\partial}{\partial y}\right)$ are constant:
    """)
    return


@app.cell
def _(stereoN, v_1):
    v_1.display(stereoN.frame())
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    On the contrary, once drawn in terms of the stereographic chart $(V, (x',y'))$, $v$ does no longer appears homogeneous:
    """)
    return


@app.cell
def _(N, stereoS, v_1):
    v_1.plot(chart=stereoS, chart_domain=stereoS, max_range=4, scale=0.02, aspect_ratio=1) + N.plot(chart=stereoS, size=30, label_offset=0.2)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Finally, a 3D view of the vector field $v$ is obtained via the embedding $\Phi$:
    """)
    return


@app.cell
def _(Phi, cartesian, graph_spher, spher, v_1):
    graph_v = v_1.plot(chart=cartesian, mapping=Phi, chart_domain=spher, number_values=11, scale=0.2)
    graph_spher + graph_v
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Similarly, let us draw the first vector field of the stereographic frame from the North pole, namely $\frac{\partial}{\partial x}$:
    """)
    return


@app.cell
def _(stereoN):
    stereoN.frame()
    return


@app.cell
def _(stereoN):
    ex = stereoN.frame()[1]
    ex
    return (ex,)


@app.cell
def _(Phi, cartesian, ex, graph_spher, spher):
    graph_ex = ex.plot(chart=cartesian, mapping=Phi, chart_domain=spher,
                       number_values=11, scale=0.4, width=1, 
                       label_axes=False)
    graph_spher + graph_ex
    return (graph_ex,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    For the second vector field of the stereographic frame from the North pole, namely $\frac{\partial}{\partial y}$, we get
    """)
    return


@app.cell
def _(stereoN):
    ey = stereoN.frame()[2]
    ey
    return (ey,)


@app.cell
def _(Phi, cartesian, ey, graph_spher, spher):
    graph_ey = ey.plot(chart=cartesian, mapping=Phi, chart_domain=spher,
                       number_values=11, scale=0.4, width=1, color='red', 
                       label_axes=False)
    graph_spher + graph_ey
    return (graph_ey,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We may combine the two graphs, to get a 3D view of the vector frame associated with the stereographic coordinates from the North pole:
    """)
    return


@app.cell
def _(N, Phi, S, cartesian, graph_ex, graph_ey, graph_spher, sphere):
    graph_frame = graph_spher + graph_ex + graph_ey \
                  + N.plot(cartesian, mapping=Phi, label_offset=0.05, size=5) \
                  + S.plot(cartesian, mapping=Phi, label_offset=0.05, size=5)
    graph_frame + sphere(color='lightgrey', opacity=0.4)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Vector fields acting on scalar fields

    $v$ and $f$ are both fields defined on the whole sphere (respectively a vector field and a scalar field). By the very definition of a vector field, $v$ acts on $f$:
    """)
    return


@app.cell
def _(f_2, v_1):
    vf = v_1(f_2)
    print(vf)
    vf.display()
    return (vf,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Values of $v(f)$ at the North pole, at the South pole and at point $p$:
    """)
    return


@app.cell
def _(N, vf):
    vf(N)
    return


@app.cell
def _(S, vf):
    vf(S)
    return


@app.cell
def _(p, vf):
    vf(p)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 1-forms

    A 1-form on $\mathbb{S}^2$ is a field of linear forms on the tangent spaces. For instance it can be the differential of a scalar field:
    """)
    return


@app.cell
def _(f_2):
    f_2.display()
    return


@app.cell
def _(diff, f_2):
    df = diff(f_2)
    print(df)
    return (df,)


@app.cell
def _(df):
    df.display()  # display w.r.t. the default frame
    return


@app.cell
def _(df, eV):
    df.display(eV)
    return


@app.cell
def _(df, spher):
    df.display(spher.frame())
    return


@app.cell
def _(df, spher):
    df.display(spher.frame(), spher)  # asking for the components to be shown in the spherical chart
    return


@app.cell
def _(df):
    print(df.parent())
    return


@app.cell
def _(df):
    df.parent()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <p><span id="cell_outer_146">The 1-form acting on a vector field:</span></p>
    """)
    return


@app.cell
def _(df, v_1):
    print(df(v_1))
    df(v_1).display()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Let us check the identity $\mathrm{d}f(v) = v(f)$:
    """)
    return


@app.cell
def _(df, f_2, v_1):
    df(v_1) == v_1(f_2)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Similarly, we have $\mathcal{L}_v f = v(f)$:
    """)
    return


@app.cell
def _(f_2, v_1):
    f_2.lie_derivative(v_1) == v_1(f_2)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Curves in $\mathbb{S}^2$

    In order to define curves in $\mathbb{S}^2$, we first introduce the field of real numbers $\mathbb{R}$ as a 1-dimensional smooth manifold with a canonical coordinate chart:
    """)
    return


@app.cell
def _(SR, manifolds):
    R1 = manifolds.RealLine(names=('t',))
    t = SR.var('t')
    print(R1)
    return R1, t


@app.cell
def _(R1):
    print(R1.category())
    return


@app.cell
def _(R1, dim):
    dim(R1)
    return


@app.cell
def _(R1):
    R1.atlas()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Let us define a <strong>loxodrome of the sphere</strong> in terms of its parametric equation with respect to the chart `spher` = $(A,(\theta,\phi))$
    """)
    return


@app.cell
def _(S2_1, atan, exp, oo, spher, t):
    c = S2_1.curve({spher: [2 * atan(exp(-t / 10)), t]}, (t, -oo, +oo), name='c')
    return (c,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Curves in $\mathbb{S}^2$ are considered as morphisms from the manifold $\mathbb{R}$ to the manifold $\mathbb{S}^2$:
    """)
    return


@app.cell
def _(c):
    c.parent()
    return


@app.cell
def _(c):
    c.display()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The curve $c$ can be plotted in terms of stereographic coordinates $(x,y)$:
    """)
    return


@app.cell
def _(c, stereoN):
    c.plot(chart=stereoN, aspect_ratio=1)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We recover the well-known fact that the graph of a loxodrome in terms of stereographic coordinates is a <strong>logarithmic spiral</strong>.

    Thanks to the embedding $\Phi$, we may also plot $c$ in terms of the Cartesian coordinates of $\mathbb{R}^3$:
    """)
    return


@app.cell
def _(Phi, c, graph_spher):
    graph_c = c.plot(mapping=Phi, max_range=40, plot_points=200, 
                     thickness=2, label_axes=False)
    graph_spher + graph_c
    return (graph_c,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <p>The <strong>tangent vector field</strong> (or <strong>velocity vector</strong>) to the curve $c$ is</p>
    """)
    return


@app.cell
def _(c):
    vc = c.tangent_vector_field()
    vc
    return (vc,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    $c'$ is a vector field <em>along</em> $\mathbb{R}$ taking its values in tangent spaces to $\mathbb{S}^2$:
    """)
    return


@app.cell
def _(vc):
    print(vc)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The set of vector fields along $\mathbb{R}$ taking their values on $\mathbb{S}^2$ via the differential mapping $c: \mathbb{R} \rightarrow \mathbb{S}^2$ is denoted by $\mathfrak{X}(\mathbb{R},c)$; it is a module over the algebra $C^\infty(\mathbb{R})$:
    """)
    return


@app.cell
def _(vc):
    vc.parent()
    return


@app.cell
def _(vc):
    vc.parent().category()
    return


@app.cell
def _(vc):
    vc.parent().base_ring()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    A coordinate view of $c'$:
    """)
    return


@app.cell
def _(vc):
    vc.display()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Let us plot the vector field $c'$ in terms of the stereographic chart $(U,(x,y))$:
    """)
    return


@app.cell
def _(c, show, stereoN, vc):
    show(vc.plot(chart=stereoN, number_values=30, scale=0.5, color='red') +
         c.plot(chart=stereoN), aspect_ratio=1)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    A 3D view of $c'$ is obtained via the embedding $\Phi$:
    """)
    return


@app.cell
def _(Phi, cartesian, graph_c, graph_spher, t, vc):
    graph_vc = vc.plot(chart=cartesian, mapping=Phi, ranges={t: (-20, 20)}, 
                       number_values=30, scale=0.5, color='red', 
                       label_axes=False)
    graph_spher + graph_c + graph_vc
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Riemannian metric on $\mathbb{S}^2$

    The standard metric on $\mathbb{S}^2$ is that induced by the Euclidean metric of $\mathbb{R}^3$. The latter
    is obtained by:
    """)
    return


@app.cell
def _(R3):
    h = R3.metric()
    h.display()
    return (h,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The metric $g$ on $\mathbb{S}^2$ is the pullback of $h$ by the embedding $\Phi$:
    """)
    return


@app.cell
def _(Phi, S2_1, h):
    g_1 = S2_1.metric('g')
    g_1.set(Phi.pullback(h))
    print(g_1)
    return (g_1,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Note that we could have defined $g$ intrinsically, i.e. by providing its components in the two frames `stereoN` and `stereoS`. Instead, we have chosen to get it as the pullback of $h$, since the pullback computation is implemented in SageMath.

    The metric is a symmetric tensor field of type (0,2):
    """)
    return


@app.cell
def _(g_1):
    print(g_1.parent())
    return


@app.cell
def _(g_1):
    g_1.tensor_type()
    return


@app.cell
def _(g_1):
    g_1.symmetries()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The expression of the metric in terms of the default frame on $\mathbb{S}^2$ (stereoN):
    """)
    return


@app.cell
def _(g_1):
    g_1.display()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We may factorize the metric components:
    """)
    return


@app.cell
def _(eU, factor, g_1):
    g_1.apply_map(factor, frame=eU, keep_other_components=True)
    g_1.display()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    A matrix view of the components of $g$ in the manifold's default frame:
    """)
    return


@app.cell
def _(g_1):
    g_1[:]
    return


@app.cell
def _(g_1):
    g_1[1, 1]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Display in terms of the vector frame `eV` =  $(V, (\partial_{x'}, \partial_{y'}))$:
    """)
    return


@app.cell
def _(eV, factor, g_1):
    g_1.apply_map(factor, frame=eV, keep_other_components=True)
    g_1.display(eV)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Expression of the metric tensor in terms of spherical coordinates:
    """)
    return


@app.cell
def _(g_1, spher):
    g_1.display(spher.frame(), chart=spher)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The metric acts on vector field pairs, resulting in a scalar field:
    """)
    return


@app.cell
def _(g_1, v_1):
    print(g_1(v_1, v_1))
    return


@app.cell
def _(g_1, v_1):
    g_1(v_1, v_1).parent()
    return


@app.cell
def _(g_1, v_1):
    g_1(v_1, v_1).display()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The **Levi-Civita connection** associated with the metric $g$:
    """)
    return


@app.cell
def _(g_1):
    nabla = g_1.connection()
    print(nabla)
    nabla
    return (nabla,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    As a test, we verify that $\nabla_g$ acting on $g$ results in zero:
    """)
    return


@app.cell
def _(g_1, nabla):
    nabla(g_1).display()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The nonzero Christoffel symbols of $g$ (skipping those that can be deduced by symmetry on the last two indices) w.r.t. two charts:
    """)
    return


@app.cell
def _(g_1, stereoN):
    g_1.christoffel_symbols_display(chart=stereoN)
    return


@app.cell
def _(g_1, spher):
    g_1.christoffel_symbols_display(chart=spher)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    $\nabla_g$ acting on the vector field $v$:
    """)
    return


@app.cell
def _(nabla, v_1):
    print(nabla(v_1))
    return


@app.cell
def _(nabla, stereoN, v_1):
    nabla(v_1).display(stereoN.frame())
    return


@app.cell
def _(nabla, v_1):
    nabla(v_1)[:]
    return


@app.cell
def _(nabla, v_1):
    nabla(v_1)[1, 2]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Curvature

    The Riemann tensor associated with the metric $g$:
    """)
    return


@app.cell
def _(g_1):
    Riem = g_1.riemann()
    print(Riem)
    Riem.display()
    return (Riem,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The components of the Riemann tensor in the default frame on $\mathbb{S}^2$:
    """)
    return


@app.cell
def _(Riem):
    Riem.display_comp()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <p>The components in the frame associated with spherical coordinates:</p>
    """)
    return


@app.cell
def _(Riem, spher):
    Riem.display_comp(spher.frame(), chart=spher)
    return


@app.cell
def _(Riem):
    print(Riem.parent())
    return


@app.cell
def _(Riem):
    Riem.symmetries()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The Riemann tensor associated with the Euclidean metric $h$ on $\mathbb{R}^3$ is identically zero:
    """)
    return


@app.cell
def _(h):
    h.riemann().display()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The Ricci tensor and the Ricci scalar:
    """)
    return


@app.cell
def _(g_1):
    Ric = g_1.ricci()
    Ric.display()
    return (Ric,)


@app.cell
def _(g_1):
    R = g_1.ricci_scalar()
    R.display()
    return (R,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Hence we recover the fact that $(\mathbb{S}^2,g)$ is a Riemannian manifold of constant positive curvature.

    In dimension 2, the Riemann curvature tensor is entirely determined by the Ricci scalar $R$ according to
    $$ R^i_{\ \, jlk} = \frac{R}{2} \left( \delta^i_{\ \, k} g_{jl} - \delta^i_{\ \, l} g_{jk} \right)$$
    Let us check this formula here, under the form $R^i_{\ \, jlk} = -R g_{j[k} \delta^i_{\ \, l]}$:
    """)
    return


@app.cell
def _(R, Riem, S2_1, g_1):
    delta = S2_1.tangent_identity_field()
    Riem == -R * (g_1 * delta).antisymmetrize(2, 3)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Similarly the relation $\mathrm{Ric} = (R/2)\; g$ must hold:
    """)
    return


@app.cell
def _(R, Ric, g_1):
    Ric == R / 2 * g_1
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Manifold orientation and volume 2-form
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    In order to introduce the volume 2-form associated with the metric $g$, we need to define an orientation on $\mathbb{S}^2$ first. We choose the orientation so that the vector frame $(\partial/\partial x', \partial/\partial y')$ of the stereographic coordinates from the South pole is right-handed. This is somewhat natural, because the triplet $(\partial/\partial x', \partial/\partial y', n)$, where $n$ is the unit outward normal to $\mathbb{S}^2$, is right-handed with respect to the standard orientation of $\mathbb{R}^3$. On the contrary the triplet
    $(\partial/\partial x, \partial/\partial y, n)$ formed from stereographic coordinates from the North pole is left-handed (see the above plot). Actually, we can check that $(\partial/\partial x, \partial/\partial y)$
    and $(\partial/\partial x', \partial/\partial y')$ lead to two opposite orientations, because the transition map
    $(x, y) \mapsto (x', y')$ has a negative Jacobian determinant:
    """)
    return


@app.cell
def _(stereoN_to_S):
    stereoN_to_S.jacobian_det()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We define the orientation via the method `set_orientation()` with a list of right-handed vector frames, whose domains form an open cover of $\mathbb{S}^2$. We therefore provide `eV` = $(\partial/\partial x', \partial/\partial y')$ (domain: $V$) and the "reversed" frame $(\partial/\partial y, \partial/\partial x)$ on $U$:
    """)
    return


@app.cell
def _(U, eU):
    reU = U.vector_frame('f', (eU[2], eU[1]))
    reU[1].display(eU), reU[2].display(eU)
    return (reU,)


@app.cell
def _(S2_1, eV, reU):
    S2_1.set_orientation([eV, reU])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The **volume 2-form** or **Levi-Civita tensor** associated with $g$ is then
    """)
    return


@app.cell
def _(g_1):
    eps = g_1.volume_form()
    print(eps)
    eps.display()
    return (eps,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Notice the minus sign in the the above expression, which reflects the fact that the default frame $(\partial/\partial x, \partial/\partial y)$ is left-handed. On the contrary, we have
    """)
    return


@app.cell
def _(eV, eps):
    eps.display(eV)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    A nicer display is obtained by factorizing the components:
    """)
    return


@app.cell
def _(eV, eps, factor, stereoS):
    eps.apply_map(factor, frame=eV, keep_other_components=True)
    eps.display(stereoS.frame())
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The frame associated with spherical coordinates is right-handed and we recover the standard expression of the volume 2-form:
    """)
    return


@app.cell
def _(eps, spher):
    eps.display(spher.frame(), chart=spher)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The exterior derivative of the 2-form $\epsilon_g$:
    """)
    return


@app.cell
def _(diff, eps):
    print(diff(eps))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Of course, since $\mathbb{S}^2$ has dimension 2, all 3-forms vanish identically:
    """)
    return


@app.cell
def _(diff, eps):
    diff(eps).display()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Non-holonomic frames
    Up to know, all the vector frames introduced on $\mathbb{S}^2$ have been coordinate frames. Let us introduce a non-coordinate frame on the open subset $A$. To ease the manipulations, we change first the default chart and default frame on $A$ to the spherical coordinate ones:
    """)
    return


@app.cell
def _(A):
    A.default_chart()
    return


@app.cell
def _(A):
    A.default_frame()
    return


@app.cell
def _(A, spher):
    A.set_default_chart(spher)
    A.set_default_frame(spher.frame())
    A.default_chart()
    return


@app.cell
def _(A):
    A.default_frame()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We introduce the new vector frame $e =  \left(\frac{\partial}{\partial\theta}, \frac{1}{\sin\theta}\frac{\partial}{\partial\phi}\right)$:
    """)
    return


@app.cell
def _(spher):
    spher.frame()[:]
    return


@app.cell
def _(A, sin, spher, th):
    d_dth, d_dph = spher.frame()[:]
    e = A.vector_frame('e', (d_dth, 1/sin(th)*d_dph))
    print(e)
    e
    return (e,)


@app.cell
def _(e):
    (e[1].display(), e[2].display())
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <p>The new frame is an orthonormal frame for the metric $g$:</p>
    """)
    return


@app.cell
def _(e, g_1):
    g_1(e[1], e[1]).expr()
    return


@app.cell
def _(e, g_1):
    g_1(e[1], e[2]).expr()
    return


@app.cell
def _(e, g_1):
    g_1(e[2], e[2]).expr()
    return


@app.cell
def _(e, g_1):
    g_1[e, :]
    return


@app.cell
def _(e, g_1):
    g_1.display(e)
    return


@app.cell
def _(e, eps):
    eps.display(e)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    It is non-holonomic, since its structure coefficients are not identically zero:
    """)
    return


@app.cell
def _(e):
    e.structure_coeff()[:]
    return


@app.cell
def _(e):
    e[2].lie_derivative(e[1]).display(e)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <p>while we have of course</p>
    """)
    return


@app.cell
def _(spher):
    spher.frame().structure_coeff()[:]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Using SymPy as the symbolic backend

    By default, the symbolic backend used in calculus on manifolds is SageMath's one (Pynac + Maxima), implemented via the symbolic ring `SR`. We can choose to use [SymPy](https://www.sympy.org/) instead:
    """)
    return


@app.cell
def _(S2_1):
    S2_1.set_calculus_method('sympy')
    return


@app.cell
def _(f_2):
    F = 2 * f_2
    F.display()
    return (F,)


@app.cell
def _(F):
    F.expr()
    return


@app.cell
def _(F):
    type(F.expr())
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Back to Sage's default:
    """)
    return


@app.cell
def _(S2_1):
    S2_1.set_calculus_method('SR')
    return


@app.cell
def _(F):
    F.expr()
    return


@app.cell
def _(F):
    type(F.expr())
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Going further

    See the notebooks [Smooth manifolds, charts and scalar fields](https://nbviewer.org/github/sagemanifolds/SageManifolds/blob/master/Worksheets/JNCF2018/jncf18_scalar.ipynb) and [Smooth manifolds, vector fields and tensor fields](https://nbviewer.org/github/sagemanifolds/SageManifolds/blob/master/Worksheets/JNCF2018/jncf18_vector.ipynb) from the lectures [Symbolic tensor calculus on manifolds](https://sagemanifolds.obspm.fr/jncf2018/). Many example notebooks are
    provided at the [SageManifolds page](https://sagemanifolds.obspm.fr/examples.html).

    See also the series of notebooks by Andrzej Chrzeszczyk: [Introduction to manifolds in SageMath](https://sagemanifolds.obspm.fr/intro_to_manifolds.html), as well as the tutorial videos by Christian Bär: [Manifolds in SageMath](https://www.youtube.com/playlist?list=PLnrOCYZpQUuJlnQbQ48zgGk-Ks1t145Yw).
    """)
    return


if __name__ == "__main__":
    app.run()
