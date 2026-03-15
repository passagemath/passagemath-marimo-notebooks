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
    # SageManifolds example notebook using [passagemath](https://github.com/passagemath): The 3-sphere: charts, quaternions, and Hopf fibration
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
        sum, srange, forget, asin
    )
    from passagemath_plot import (
        show, sphere, colormaps, parametric_plot3d, text3d, Graphics, animate,
        implicit_plot3d
    )
    from passagemath_repl import get_display_manager; dm = get_display_manager()
    return (
        Graphics,
        Manifold,
        Parallelism,
        asin,
        assume,
        atan,
        atan2,
        cos,
        forget,
        implicit_plot3d,
        manifolds,
        mo,
        pi,
        show,
        sin,
        sqrt,
        var,
    )


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    This marimo notebook, adapted from a Jupyter notebook published in https://sagemanifolds.obspm.fr/examples.html, demonstrates some differential geometry capabilities of SageMath on the example of the 3-dimensional sphere, $\mathbb{S}^3$. The corresponding tools have been developed within the  [SageManifolds](https://sagemanifolds.obspm.fr) project. They are now available in Python environments via the modularized distributions of the Sage library developed by the [passagemath](https://github.com/passagemath) project.
    - The SageManifolds functionality is shipped as part of [passagemath-symbolics](https://pypi.org/project/passagemath-symbolics/).
    - The pip-installable package [passagemath-maxima](https://pypi.org/project/passagemath-maxima/) provides the backend for symbolic computation.
    - [passagemath-plot](https://pypi.org/project/passagemath-plot/) provides 2D and 3D plotting facilities.
    - [passagemath-repl](https://pypi.org/project/passagemath-repl/) provides the integration with the marimo notebook.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    To increase the computational speed, we ask for demanding computations to be parallelly performed:
    """)
    return


@app.cell
def _(Parallelism):
    Parallelism().set(nproc=3)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## $\mathbb{S}^3$ as a 3-dimensional differentiable manifold

    We start by declaring $\mathbb{S}^3$ as a differentiable manifold of dimension 3 over $\mathbb{R}$:
    """)
    return


@app.cell
def _(Manifold):
    S3 = Manifold(3, 'S^3', latex_name=r'\mathbb{S}^3', start_index=1)
    return (S3,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The first argument, `3`, is the dimension of the manifold, while the second argument is the symbol used to label the manifold, with the LaTeX output specified by the argument `latex_name`. The argument `start_index` sets the index range to be used on the manifold for labelling components w.r.t. a basis or a frame: `start_index=1` corresponds to $\{1,2,3\}$; the default value is `start_index=0`, yielding to $\{0,1,2\}$.
    """)
    return


@app.cell
def _(S3):
    print(S3)
    return


@app.cell
def _(S3):
    S3
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Coordinate charts on $\mathbb{S}^3$

    The 3-sphere cannot be covered by a single chart. At least two charts are necessary, for instance the charts associated with the stereographic projections from two distinct points, $N$ and $S$ say,
    which we may call the *North pole* and the *South pole* respectively. Let us introduce the open subsets covered by these two charts:
    $$ U := \mathbb{S}^3\setminus\{N\} $$
    $$ V := \mathbb{S}^3\setminus\{S\} $$
    """)
    return


@app.cell
def _(S3):
    U = S3.open_subset('U') ; print(U)
    return (U,)


@app.cell
def _(S3):
    V = S3.open_subset('V') ; print(V)
    return (V,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We declare that $\mathbb{S}^3 = U \cup V$:
    """)
    return


@app.cell
def _(S3, U, V):
    S3.declare_union(U, V)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Then we introduce the stereographic chart on $U$, denoting by $(x,y,z)$ the coordinates resulting from the stereographic projection from the North pole onto the equatorial plane:
    """)
    return


@app.cell
def _(U):
    stereoN = U.chart("x y z")
    x,y,z = stereoN[:]
    stereoN
    return stereoN, x, y, z


@app.cell
def _(stereoN):
    stereoN.coord_range()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Similarly, we introduce on $V$ the coordinates $(x',y',z')$ corresponding to the stereographic projection from the South pole onto the equatorial plane:
    """)
    return


@app.cell
def _(V):
    stereoS = V.chart("xp:x' yp:y' zp:z'")
    xp,yp,zp = stereoS[:]
    stereoS
    return stereoS, xp, yp, zp


@app.cell
def _(stereoS):
    stereoS.coord_range()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We have to specify the **transition map** between the charts `stereoN` = $(U,(x,y,z))$ and `stereoS` = $(V,(x',y',z'))$; it is given by the standard inversion formulas:
    """)
    return


@app.cell
def _(stereoN, stereoS, x, xp, y, yp, z, zp):
    r2 = x**2 + y**2 + z**2
    stereoN_to_S = stereoN.transition_map(stereoS, 
                                          (x/r2, y/r2, z/r2), 
                                          intersection_name='W',
                                          restrictions1=(x**2 + y**2 + z**2 != 0), 
                                          restrictions2=(xp**2 + yp**2 + zp**2 != 0))
    stereoN_to_S.display()
    return r2, stereoN_to_S


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    In the above declaration, `'W'` is the name given to the open subset where the two charts overlap: $W := U\cap V$, the condition $x^2+y^2+z^2\not=0$  defines $W$ as a subset of $U$, and the condition $x'^2+y'^2+z'^2\not=0$ defines $W$ as a subset of $V$.

    The inverse coordinate transformation is computed by means of the method `inverse()`:
    """)
    return


@app.cell
def _(stereoN_to_S):
    stereoS_to_N = stereoN_to_S.inverse()
    stereoS_to_N.display()
    return (stereoS_to_N,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Note that the situation is of course perfectly symmetric regarding the coordinates $(x,y,z)$ and $(x',y',z')$.

    At this stage, the user's atlas has four charts:
    """)
    return


@app.cell
def _(S3):
    S3.atlas()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    For future reference, we store $W=U\cap V$ into a Python variable:
    """)
    return


@app.cell
def _(U, V):
    W = U.intersection(V)
    print(W)
    return (W,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### The North and South poles

    $N$ is the point of $V$ of stereographic coordinates $(x',y',z')=(0,0,0)$:
    """)
    return


@app.cell
def _(V, stereoS):
    N = V((0,0,0), chart=stereoS, name='N')
    print(N)
    return (N,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    while $S$ is the point of U of stereographic coordinates $(x,y,z)=(0,0,0)$:
    """)
    return


@app.cell
def _(U, stereoN):
    S = U((0,0,0), chart=stereoN, name='S')
    print(S)
    return (S,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We have of course
    """)
    return


@app.cell
def _(N, S, U, V):
    all([N not in U, N in V, S in U, S not in V])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Embedding of $\mathbb{S}^3$ into $\mathbb{R}^4$

    Let us first declare $\mathbb{R}^4$ as a 4-dimensional manifold covered by a single chart (the so-called **Cartesian coordinates**):
    """)
    return


@app.cell
def _(Manifold):
    R4 = Manifold(4, 'R^4', r'\mathbb{R}^4')
    X4 = R4.chart("T X Y Z")
    T,X,Y,Z = X4[:]
    X4
    return R4, T, X, X4, Y, Z


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The embedding of $\mathbb{S}^3$ into $\mathbb{R}^4$ is then defined by the standard formulas relating the stereographic coordinates to the ambient Cartesian ones when considering a **stereographic projection** from the point $(-1,0,0,0)$ to the equatorial plane $T=0$:
    """)
    return


@app.cell
def _(R4, S3, X4, r2, stereoN, stereoS, x, xp, y, yp, z, zp):
    rp2 = xp**2 + yp**2 + zp**2
    Phi = S3.diff_map(R4, {(stereoN, X4): 
                           [(1-r2)/(r2+1), 2*x/(r2+1), 
                            2*y/(r2+1), 2*z/(r2+1)],
                           (stereoS, X4):
                           [(rp2-1)/(rp2+1), 2*xp/(rp2+1), 
                            2*yp/(rp2+1), 2*zp/(rp2+1)]},
                      name='Phi', latex_name=r'\Phi')
    Phi.display()
    return (Phi,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    From this choice of stereographic projection, the "North" pole is actually the point of coordinates $(-1,0,0,0)$ in $\mathbb{R}^4$:
    """)
    return


@app.cell
def _(N, Phi, X4):
    X4(Phi(N))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    while the "South" pole is the point of coordinates $(1,0,0,0)$:
    """)
    return


@app.cell
def _(Phi, S, X4):
    X4(Phi(S))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We may use the embedding $\Phi$ to plot the stereographic coordinate grid in terms of the $\mathbb{R}^4$'s Cartesian coordinates:
    """)
    return


@app.cell
def _(Phi, X, X4, Y, Z, show, stereoN, x, y, z):
    graph_stereoN = stereoN.plot(chart=X4, mapping=Phi, 
                                 ambient_coords=(X,Y,Z),
                                 number_values=9,
                                 color={x: 'red', y: 'green', z: 'gold'},
                                 label_axes=False)
    show(graph_stereoN, axes_labels=['X', 'Y', 'Z'])
    return


@app.cell
def _(N, Phi, S, T, X, X4, Y, show, stereoN, x, y, z):
    graph_stereoN_1 = stereoN.plot(chart=X4, mapping=Phi, ambient_coords=(X, Y, T), 
                                   number_values=13, plot_points=150, 
                                   color={x: 'red', y: 'green', z: 'gold'}, 
                                   label_axes=False)
    pointN = N.plot(chart=X4, mapping=Phi, ambient_coords=(X, Y, T), 
                    color='maroon', label_offset=0.05)
    pointS = S.plot(chart=X4, mapping=Phi, ambient_coords=(X, Y, T), 
                    color='maroon', label_offset=0.05)
    show(graph_stereoN_1 + pointN + pointS, axes_labels=['X', 'Y', 'T'])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Hyperspherical coordinates

    The hyperspherical coordinates $(\chi, \theta, \phi)$ generalize the standard spherical coordinates $(\theta, \phi)$ on $\mathbb{S}^2$. They are defined on the open domain $A\subset W \subset \mathbb{S}^3$ that is the complement of the "origin meridian"; since the latter is defined by $y=0$ and $x\geq 0$, we declare:
    """)
    return


@app.cell
def _(W, stereoN, stereoS, x, xp, y, yp):
    A = W.open_subset('A', coord_def={stereoN.restrict(W): (y!=0, x<0), 
                                      stereoS.restrict(W): (yp!=0, xp<0)})
    print(A)
    return (A,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We then declare the chart $(A,(\chi,\theta,\phi))$ by specifying the intervals spanned by the various coordinates:
    """)
    return


@app.cell
def _(A):
    spher = A.chart(r'ch:(0,pi):\chi th:(0,pi):\theta ph:(0,2*pi):\phi')
    ch,th,ph = spher[:]
    spher
    return ch, ph, spher, th


@app.cell
def _(spher):
    spher.coord_range()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The specification of the hyperspherical coordinates is completed by providing the transition map to the stereographic chart $(A,(x,y,z))$:
    """)
    return


@app.cell
def _(A, ch, cos, ph, sin, spher, stereoN, th):
    den = 1 + cos(ch)
    spher_to_stereoN = spher.transition_map(stereoN.restrict(A), 
                                            (sin(ch)*sin(th)*cos(ph)/den,
                                             sin(ch)*sin(th)*sin(ph)/den,
                                             sin(ch)*cos(th)/den))
    spher_to_stereoN.display()
    return (spher_to_stereoN,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We also provide the inverse transition map by means of the method `set_inverse`, which (by default) performs a check that the provided formulas are indeed correct:
    """)
    return


@app.cell
def _(atan, atan2, pi, spher_to_stereoN, sqrt, x, y, z):
    spher_to_stereoN.set_inverse(2*atan(sqrt(x**2 + y**2 + z**2)),
                                 atan2(sqrt(x**2 + y**2), z),
                                 atan2(-y, -x) + pi)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The check is passed, modulo some lack of trigonometric simplifications in the first three lines.
    """)
    return


@app.cell
def _(spher_to_stereoN):
    spher_to_stereoN.inverse().display()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The transition map $(A,(\chi,\theta,\phi))\rightarrow (A,(x',y',z'))$ is obtained by combining the transition maps $(A,(\chi,\theta,\phi))\rightarrow (A,(x,y,z))$ and $(A,(x,y,z))\rightarrow (A,(x',y',z'))$:
    """)
    return


@app.cell
def _(A, spher_to_stereoN, stereoN_to_S):
    spher_to_stereoS = stereoN_to_S.restrict(A) * spher_to_stereoN
    spher_to_stereoS.display()
    return (spher_to_stereoS,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Similarly, the transition map $(A,(x',y',z'))\rightarrow (A,(\chi,\theta,\phi))$ is obtained by combining the transition maps $(A,(x',y',z'))\rightarrow (A,(x,y,z))$ and $(A,(x,y,z))\rightarrow (A,(\chi,\theta,\phi))$:
    """)
    return


@app.cell
def _(A, spher_to_stereoN, stereoS_to_N):
    stereoS_to_spher = spher_to_stereoN.inverse() * stereoS_to_N.restrict(A)
    stereoS_to_spher.display()
    return (stereoS_to_spher,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    At this stage, the user atlas of $\mathbb{S}^3$ is
    """)
    return


@app.cell
def _(S3):
    S3.atlas()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Let us get the coordinate expression of the restriction of the embedding $\Phi$ to $A$:
    """)
    return


@app.cell
def _(A, Phi, X4, stereoN):
    Phi.display(stereoN.restrict(A), X4)
    return


@app.cell
def _(Phi, X4, spher):
    Phi.display(spher, X4)
    return


@app.cell
def _(Phi):
    Phi.display()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Plots of the hyperspherical coordinate grid

    First let us plot the chart $(A,(\chi,\theta,\phi))$ in terms of the stereographic chart $(U,(x,y,z))$ (notice that the "point at infinity" corresponds to $\chi\rightarrow \pi$, hence the $0.9$ truncation in the $\chi$ range):
    """)
    return


@app.cell
def _(ch, ph, pi, show, spher, stereoN, th):
    graph = spher.plot(stereoN, 
                       number_values=7,
                       ranges={ch: (0, 0.9*pi)},
                       color={ch: 'green', th: 'blue', ph: 'red'},
                       label_axes=False)
    show(graph, axes_labels=['x', 'y', 'z'])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    In terms of the stereographic coordinates $(V, (x',y',z'))$ (notice that the "point at infinity" corresponds then to $\chi\rightarrow 0$):
    """)
    return


@app.cell
def _(ch, ph, pi, show, spher, stereoS, th):
    graph_1 = spher.plot(stereoS, number_values=7, ranges={ch: (0.1, pi)}, 
                         color={ch: 'green', th: 'blue', ph: 'red'}, label_axes=False)
    show(graph_1, axes_labels=["x'", "y'", "z'"])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Of course we may use the embeddding $\Phi$ to get views of the hyperspherical coordinates in terms of the Cartesian coordinates $(T,X,Y,Z)$ of $\mathbb{R}^4$:
    """)
    return


@app.cell
def _(Phi, T, X, X4, Y, ch, ph, show, spher, th):
    graph_2 = spher.plot(X4, mapping=Phi, ambient_coords=(X, Y, T), number_values=7, 
                         color={ch: 'green', th: 'blue', ph: 'red'}, label_axes=False)
    show(graph_2, axes_labels=['X', 'Y', 'T'])
    return


@app.cell
def _(Phi, X, X4, Y, Z, ch, ph, show, spher, th):
    graph_3 = spher.plot(X4, mapping=Phi, ambient_coords=(X, Y, Z), number_values=7, 
                         color={ch: 'green', th: 'blue', ph: 'red'}, label_axes=False)
    show(graph_3, axes_labels=['X', 'Y', 'Z'])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Projection of $\mathbb{R}^4$ to $\mathbb{S}^3$
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We will need some projection operator from (a subset of) $\mathbb{R}^4$ to $\mathbb{S}^3$.
    Let $\mathbb{R}^4_N$ be $\mathbb{R}^4$ minus the hyperplane $T=-1$:
    """)
    return


@app.cell
def _(R4, T, X4):
    R4N = R4.open_subset('R4N', latex_name=r'\mathbb{R}^4_N', 
                         coord_def={X4: T!=-1})
    X4N = X4.restrict(R4N)
    return R4N, X4N


@app.cell
def _(R4N, T, U, X, X4N, Y, Z, stereoN):
    ProjN = R4N.diff_map(U, {(X4N, stereoN): 
                             [X/(1+T), Y/(1+T), Z/(1+T)]},
                         name='P_N', latex_name=r'\Pi_N')
    ProjN.display()
    return (ProjN,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Let us check that once applied to an embedded point of $U\subset \mathbb{S}^3$, this projection reduces to the identity:
    """)
    return


@app.cell
def _(Phi, ProjN, S3, a, b, c, stereoN, var):
    var('a b c', domain='real')
    p = S3((a,b,c), chart=stereoN)
    ProjN(Phi(p)) == p
    return


@app.cell
def _(R4, X4, a, b, cos, sin, sqrt):
    q = R4((sqrt(3)/2, sin(a)*cos(b)/2, sin(a)*sin(b)/2, cos(a)/2))
    X4(q)
    return (q,)


@app.cell
def _(Phi, ProjN, R4N, q):
    all([q in R4N, Phi(ProjN(q)) == q])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Quaternions
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We consider the (division) algebra of quaternions $\mathbb{H}$ as $\mathbb{R}^4$ endowed with the following (non-commutative) product:
    """)
    return


@app.cell
def _(N, Phi, ProjN, R4, R4N, S3, X4):
    def qprod(p,q):
        if p in R4 and q in R4:
            T1, X1, Y1, Z1 = X4(p)
            T2, X2, Y2, Z2 = X4(q)
            return R4(((T1*T2-X1*X2-Y1*Y2-Z1*Z2).simplify_full(),
                       (T1*X2+X1*T2+Y1*Z2-Z1*Y2).simplify_full(),
                       (T1*Y2-X1*Z2+Y1*T2+Z1*X2).simplify_full(),
                       (T1*Z2+X1*Y2-Y1*X2+Z1*T2).simplify_full()))
        if p in S3 and q in S3:
            a = qprod(Phi(p),Phi(q))
            if X4(a) == (-1,0,0,0):
                return N
            return ProjN(R4N(a))
        raise ValueError("Cannot evaluate qprod of {} and {}".format(p,q))

    return (qprod,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Note that we have extended the definition of the quaternionic product to $\mathbb{S}^3$ via the embedding $\Phi$.

    ### Distinguished quaternions on $\mathbb{S}^3$

    Let us introduce two special points on $\mathbb{S}^3$: $\mathbf{1}$ and $-\mathbf{1}$.
    """)
    return


@app.cell
def _(Phi, S3, X4, stereoN):
    One = S3((0,0,0), chart=stereoN, name='1', latex_name=r'\mathbf{1}')
    X4(Phi(One))
    return (One,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    As we can see from the Cartesian coordinates of $\Phi(\mathbf{1})$, the point $\mathbf{1}$ is actually nothing but the "South" pole used to define the stereographic chart $(V,(x',y',z'))$:
    """)
    return


@app.cell
def _(One, S):
    One == S
    return


@app.cell
def _(Phi, S3, X4, stereoS):
    minusOne = S3((0,0,0), chart=stereoS, name='-1', latex_name=r'-\mathbf{1}')
    X4(Phi(minusOne))
    return (minusOne,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The point $\mathbf{-1}$ is thus nothing but the "North" pole used to define the stereographic chart $(U,(x,y,z))$:
    """)
    return


@app.cell
def _(N, minusOne):
    minusOne == N
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Next we introduce points $\mathbf{i}$, $\mathbf{j}$ and $\mathbf{k}$ on $\mathbb{S}^3$:
    """)
    return


@app.cell
def _(Phi, S3, X4, stereoN):
    I = S3((1,0,0), chart=stereoN, name='i', latex_name=r'\mathbf{i}')
    X4(Phi(I))
    return (I,)


@app.cell
def _(I, stereoS):
    stereoS(I)
    return


@app.cell
def _(Phi, S3, X4, stereoN):
    J = S3((0,1,0), chart=stereoN, name='j', latex_name=r'\mathbf{j}')
    X4(Phi(J))
    return (J,)


@app.cell
def _(J, stereoS):
    stereoS(J)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Since $\mathbf{j}$ lies in $A$, contrary to $\mathbf{i}$, we may ask for its hyperspherical coordinates:
    """)
    return


@app.cell
def _(J, spher):
    spher(J)
    return


@app.cell
def _(Phi, S3, X4, stereoN):
    K = S3((0,0,1), chart=stereoN, name='k', latex_name=r'\mathbf{k}')
    X4(Phi(K))
    return (K,)


@app.cell
def _(K, stereoS):
    stereoS(K)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Hamilton's fundamental relations
    $$ \mathbf{i} \mathbf{j} \mathbf{k} = \mathbf{-1} $$
    $$ \mathbf{i} \mathbf{j} = \mathbf{k},\quad \mathbf{j} \mathbf{k} = \mathbf{i}, \quad \mathbf{k} \mathbf{i} = \mathbf{j}$$
    are satisfied:
    """)
    return


@app.cell
def _(I, J, K, minusOne, qprod):
    qprod(I, qprod(J,K)) == minusOne
    return


@app.cell
def _(I, J, K, qprod):
    all([qprod(I,J) == K, qprod(J,K) == I,
         qprod(K,I) == J])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    These relations imply $\mathbf{i}^2 = \mathbf{-1}$, $\mathbf{j}^2 = \mathbf{-1}$ and $\mathbf{k}^2 = \mathbf{-1}$:
    """)
    return


@app.cell
def _(I, J, K, One, minusOne, qprod):
    all([qprod(One,One) == One, qprod(I,I) == minusOne,
         qprod(J,J) == minusOne, qprod(K,K) == minusOne])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Let us introduce $\mathbf{-i}$, $\mathbf{-j}$ and $\mathbf{-k}$, as points of $\mathbb{S}^3$:
    """)
    return


@app.cell
def _(I, Phi, X4, minusOne, qprod):
    minusI = qprod(minusOne, I)
    X4(Phi(minusI))
    return (minusI,)


@app.cell
def _(J, Phi, X4, minusOne, qprod):
    minusJ = qprod(minusOne, J)
    X4(Phi(minusJ))
    return (minusJ,)


@app.cell
def _(K, Phi, X4, minusOne, qprod):
    minusK = qprod(minusOne, K)
    X4(Phi(minusK))
    return (minusK,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Quaternionic conjugation
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    In the comments below (but not in the SageMath code), we shall identify $\mathbf{1}\in \mathbb{S}^3$ with $\Phi(\mathbf{1})\in \mathbb{R}^4$, $\mathbf{i}\in \mathbb{S}^3$ with $\Phi(\mathbf{i})\in \mathbb{R}^4$, etc. In particular, we consider $(\mathbf{1}, \mathbf{i}, \mathbf{j},\mathbf{k})$ as a basis of the quaternion algebra $\mathbb{H}$.

    The *conjugate* of a quaternion $q = T + X\mathbf{i} + Y\mathbf{j} + Z\mathbf{k}$ is $\bar{q} = T - X\mathbf{i} - Y\mathbf{j} - Z\mathbf{k}$; hence we define:
    """)
    return


@app.cell
def _(N, Phi, ProjN, R4, S3, X4):
    def qconj(p):
        if p in R4:
            T, X, Y, Z = X4(p)
            return R4((T, -X, -Y, -Z))
        if p in S3:
            a = qconj(Phi(p))
            if X4(a) == (-1,0,0,0):
                return N
            return ProjN(a)
        raise ValueError("Cannot evaluate qconf of {}".format(p))

    return (qconj,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    In particular, we have $\bar{\mathbf{1}} = \mathbf{1}$, $\bar{\mathbf{i}} = -\mathbf{i}$,  $\bar{\mathbf{j}} = -\mathbf{j}$ and  $\bar{\mathbf{k}} = -\mathbf{k}$:
    """)
    return


@app.cell
def _(I, J, K, One, minusI, minusJ, minusK, qconj):
    all([qconj(One) == One, 
         qconj(I) == minusI,
         qconj(J) == minusJ, 
         qconj(K) == minusK])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The conjugate of an element of $\mathbb{S}^3$
    """)
    return


@app.cell
def _(S3, a, assume, b, c, qconj, stereoN):
    assume(a != 0)  # to ensure that qconj(p) is not N
    p_1 = S3((a, b, c), chart=stereoN)
    stereoN(qconj(p_1))
    return


@app.cell
def _(S3, a, b, c, qconj, stereoS):
    p_2 = S3((a, b, c), chart=stereoS)
    stereoS(qconj(p_2))
    return


@app.cell
def _(a, forget):
    forget(a!=0)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Norm of a quaternion

    The quaternionic norm $\| q\| = \sqrt{q\bar{q}}$ coincide with the Euclidean norm in $\mathbb{R}^4$, so that $\mathbb{S}^3$ can be viewed as the set of unit quaternions; hence we define:
    """)
    return


@app.cell
def _(R4, S3, X4, sqrt):
    def qnorm(p):
        if p in R4:
            T, X, Y, Z = X4(p)
            return (sqrt(T**2 + X**2 + Y**2 + Z**2)).simplify_full()
        if p in S3:
            return 1
        raise ValueError("Cannot evaluate qnorm of {}".format(p))

    return (qnorm,)


@app.cell
def _(R4, a, b, c, d, qnorm, var):
    var('d', domain='real')
    q_1 = R4((a, b, c, d))
    qnorm(q_1)
    return (q_1,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Let us check that $\| q\|^2 = q\bar{q}$:
    """)
    return


@app.cell
def _(R4, q_1, qconj, qnorm, qprod):
    R4((qnorm(q_1)**2, 0, 0, 0)) == qprod(q_1, qconj(q_1))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    As elements of $\mathbb{S}^3$, $\mathbf{1}$,  $\mathbf{i}$,  $\mathbf{j}$ and  $\mathbf{k}$ have all unit norm:
    """)
    return


@app.cell
def _(I, J, K, One, qnorm):
    (qnorm(One), qnorm(I), qnorm(J), qnorm(K)) == (1, 1, 1, 1)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Hopf map
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We shall define the Hopf map by considering first the map

    $\begin{array}{cccc}
       C: &  \mathbb{R}^4 & \to & \mathbb{R}^4\\
       &  p & \mapsto & p \mathbf{k} \bar{p}
       \end{array}$

    The coordinate expression of $C$ is obtained as follows:
    """)
    return


@app.cell
def _(K, Phi, R4, T, X, X4, Y, Z, qconj, qprod):
    p_3 = R4((T, X, Y, Z))  # a generic point of R^4
    coord_Cp = X4(qprod(p_3, qprod(Phi(K), qconj(p_3))))
    coord_Cp
    return (coord_Cp,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Therefore we define $C$ as
    """)
    return


@app.cell
def _(R4, coord_Cp):
    C = R4.diff_map(R4, coord_Cp, name='C')
    C.display()
    return (C,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The restriction of $C$ to $\Phi(\mathbb{S}^3)\subset \mathbb{R}^4$ can be viewed as the map
    $C\circ \Phi: \mathbb{S}^3 \to \mathbb{R}^4$ :
    """)
    return


@app.cell
def _(C, Phi):
    CS = C * Phi
    CS.display()
    return (CS,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    On the above coordinate expressions, we note that the codomain of $C\circ \Phi$ lies in the hyperplane $T=0$, i.e. in the set $\operatorname{Im}\mathbb{H}$ of pure imaginary quaternions.
    Moreover, if we consider a generic point $p\in U\subset\mathbb{S}^3$:
    """)
    return


@app.cell
def _(S3, a, b, c, stereoN):
    p_4 = S3((a, b, c), chart=stereoN)
    return (p_4,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    we have $\| C\circ\Phi(p) \| = 1$:
    """)
    return


@app.cell
def _(CS, p_4, qnorm):
    qnorm(CS(p_4))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    For the only point of $\mathbb{S}^3$ not lying in $U$, i.e. $N = -\mathbf{1}$, we have as well
    """)
    return


@app.cell
def _(CS, N, qnorm):
    qnorm(CS(N))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Hence the codomain of $C \circ\Phi$ lies in $\Phi(\mathbb{S}^3)$. From the previous result, we conclude that it actually lies in $\Phi(\mathbb{S}^3)\cap \operatorname{Im}\mathbb{H}$, which is a 2-sphere: the 2-sphere of unit imaginary quaternions.

    In particular, we have:
    """)
    return


@app.cell
def _(CS, K, One, Phi, minusOne):
    all([CS(K) == Phi(K), CS(One) == Phi(K), CS(minusOne) == Phi(K)])
    return


@app.cell
def _(CS, I, J, Phi, minusI, minusJ, minusK):
    all([CS(I) == Phi(minusK), CS(J) == Phi(minusK),
         CS(minusI) == Phi(minusK), CS(minusJ) == Phi(minusK)])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    On $\Phi(\mathbb{S}^3)\cap \operatorname{Im}\mathbb{H}$, the inverse embedding $\Phi^{-1}$ coincides with
    the projector $\Pi_N$ introduced above since $(\Phi(\mathbb{S}^3)\cap \operatorname{Im}\mathbb{H})\subset \mathbb{R}^4_N$. Hence the map $H = \Phi^{-1}\circ C \circ \Phi: \mathbb{S}^3 \to \mathbb{S}^3$ can be obtained as $\Pi_N\circ C \circ \Phi$:
    """)
    return


@app.cell
def _(CS, ProjN, R4N, S3):
    H = ProjN * CS.restrict(S3, subcodomain=R4N)
    return (H,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Note that we have used the method `restrict` with the argument `subcodomain=R4N`
    to declare that the codomain of $C\circ\Phi$ actually lies in $\mathbb{R}^4_N$, so that the composition with $\Pi_N$ is well defined.
    We have
    """)
    return


@app.cell
def _(H):
    H.display()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Actually since neither $N$ (which has $T=-1$) nor $S$ (which has $T=1$) lie in the codomain of $C\circ\Phi$, we may safely declare that the codomain of $H$ is $W = U\cap V$:
    """)
    return


@app.cell
def _(H, S3, W):
    H_1 = H.restrict(S3, subcodomain=W)
    H_1.display()
    return (H_1,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We have $H(\mathbf{k})=H(\mathbf{1})=H(-\mathbf{k})=H(-\mathbf{1})=\mathbf{k}$:
    """)
    return


@app.cell
def _(H_1, K, One, minusK, minusOne):
    all([H_1(K) == K, H_1(One) == K, H_1(minusK) == K, H_1(minusOne) == K])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    and $H(\mathbf{i})=H(\mathbf{j})=-\mathbf{k}$:
    """)
    return


@app.cell
def _(H_1, I, J, minusK):
    all([H_1(I) == minusK, H_1(J) == minusK])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Let us consider the expression of $H$ in stereographic coordinates:
    """)
    return


@app.cell
def _(H_1, stereoN):
    Hx, Hy, Hz = H_1.expr(stereoN, stereoN)
    (Hx.factor(), Hy.factor(), Hz.factor())
    return Hx, Hy, Hz


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We have
    """)
    return


@app.cell
def _(Hx, Hy, Hz):
    (Hx**2 + Hy**2 + Hz**2).simplify_full()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    which shows that the codomain of $H$ lies in the 2-sphere of equation $x^2+y^2+z^2=1$ in stereographic coordinates. This is not surprising since (i) the equation of the 2-sphere of
    unit imaginary quaternions, $\Phi(\mathbb{S}^3)\cap \operatorname{Im}\mathbb{H}$, is $T=0$ and $X^2+Y^2+Z^2=1$ and (ii) for
    $T=0$, we have $x=X$, $y=Y$ and $z=Z$.
    Let us construct this 2-sphere as a manifold by itself, which we call the **base 2-sphere**. This will be the codomain of the Hopf map.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## The base 2-sphere (unit imaginary quaternions)
    """)
    return


@app.cell
def _(Manifold):
    S2 = Manifold(2, 'S^2', latex_name=r'\mathbb{S}^2')
    print(S2)
    return (S2,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    As for $\mathbb{S}^3$, we introduce on $\mathbb{S}^2$ two complementary stereographic coordinate systems:
    """)
    return


@app.cell
def _(S2):
    U2 = S2.open_subset('U_2')
    V2 = S2.open_subset('V_2')
    S2.declare_union(U2, V2)
    return U2, V2


@app.cell
def _(U2):
    stereoN2 = U2.chart("x2:x_2 y2:y_2")
    x2, y2 = stereoN2[:]
    stereoN2
    return stereoN2, x2, y2


@app.cell
def _(V2):
    stereoS2 = V2.chart(r"xp2:{x'}_2 yp2:{y'}_2")
    xp2, yp2 = stereoS2[:]
    stereoS2
    return stereoS2, xp2, yp2


@app.cell
def _(stereoN2, stereoS2, x2, xp2, y2):
    stereoN_to_S2 = stereoN2.transition_map(stereoS2, 
                                            (x2/(x2**2+y2**2), y2/(x2**2+y2**2)), 
                                            intersection_name='W_2',
                                            restrictions1=(x2**2 + y2**2 != 0), 
                                            restrictions2=(xp2**2 + xp2**2 != 0))
    stereoN_to_S2.display()
    return (stereoN_to_S2,)


@app.cell
def _(stereoN_to_S2):
    stereoS_to_N2 = stereoN_to_S2.inverse()
    stereoS_to_N2.display()
    return


@app.cell
def _(U2, V2):
    W2 = U2.intersection(V2)
    return (W2,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We embed the base 2-sphere $\mathbb{S}^2$ in $\mathbb{S}^3$ by considering that the North pole defining the above stereographic coordinates is $\mathbf{k}$, i.e. the point
    $(x,y,z)=(0,0,1)$ in $\mathbb{S}^3$:
    """)
    return


@app.cell
def _(S2, S3, stereoN, stereoN2, stereoS2, x2, xp2, y2, yp2):
    Phi2 = S2.diff_map(S3, {(stereoN2, stereoN): 
                            [2*x2/(1+x2**2+y2**2), 
                             2*y2/(1+x2**2+y2**2),
                             (x2**2+y2**2-1)/(1+x2**2+y2**2)],
                            (stereoS2, stereoN): 
                            [2*xp2/(1+xp2**2+yp2**2), 
                             2*yp2/(1+xp2**2+yp2**2),
                             (1-xp2**2-yp2**2)/(1+xp2**2+yp2**2)]},
                       name='Phi2', latex_name=r'\Phi_2')
    Phi2.display()
    return (Phi2,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The unit imaginary quaternions $\mathbf{i}$, $\mathbf{j}$, $\mathbf{k}$ and $-\mathbf{k}$ as elements of the base 2-sphere:
    """)
    return


@app.cell
def _(S2, stereoN2, stereoS2):
    I2 = S2((1,0), chart=stereoN2)
    J2 = S2((0,1), chart=stereoN2)
    K2 = S2((0,0), chart=stereoS2)
    minusK2 = S2((0,0), chart=stereoN2)
    return I2, J2, K2, minusK2


@app.cell
def _(I, I2, J, J2, K, K2, Phi2, minusK, minusK2):
    all([Phi2(I2) == I, Phi2(J2) == J,
         Phi2(K2) == K, Phi2(minusK2) == minusK])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Spherical coordinates on $\mathbb{S}^2$

    We introduce spherical coordinates $(\theta_2,\phi_2)$ on the base 2-sphere in the standard way (cf. the [2-sphere notebook](http://nbviewer.jupyter.org/github/sagemanifolds/SageManifolds/blob/master/Notebooks/SM_sphere_S2.ipynb)):
    """)
    return


@app.cell
def _(
    W2,
    atan,
    atan2,
    cos,
    pi,
    sin,
    sqrt,
    stereoN2,
    stereoN_to_S2,
    stereoS2,
    x2,
    xp2,
    y2,
    yp2,
):
    A2 = W2.open_subset('A_2', 
                        coord_def={stereoN2.restrict(W2): (y2!=0, x2<0), 
                                   stereoS2.restrict(W2): (yp2!=0, xp2<0)})
    spher2 = A2.chart(r'th2:(0,pi):\theta_2 ph2:(0,2*pi):\phi_2')
    th2, ph2 = spher2[:]
    spher2_to_stereoN2 = spher2.transition_map(stereoN2.restrict(A2), 
                                            (sin(th2)*cos(ph2)/(1-cos(th2)),
                                             sin(th2)*sin(ph2)/(1-cos(th2))))
    spher2_to_stereoN2.set_inverse(2*atan(1/sqrt(x2**2+y2**2)), 
                                   atan2(-y2,-x2)+pi)
    spher2_to_stereoS2 = stereoN_to_S2.restrict(A2) * spher2_to_stereoN2
    stereoS2_to_spher2 = spher2_to_stereoN2.inverse() * \
                         stereoN_to_S2.inverse().restrict(A2)
    return A2, spher2


@app.cell
def _(A2):
    A2.atlas()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Projectors $\mathbb{S}^3 \to \mathbb{S}^2$

    Let $W_{z\not=1}$ denote the subset of $W\subset\mathbb{S}^3$ defined by $z\not=1$:
    """)
    return


@app.cell
def _(W, stereoN, z):
    Wz1 = W.open_subset('Wz1', latex_name=r'W_{z\not=1}', 
                        coord_def={stereoN.restrict(W): z!=1})
    return (Wz1,)


@app.cell
def _(I, J, K, One, Wz1, minusK, minusOne):
    all([I in Wz1, J in Wz1, minusK in Wz1,
         K not in Wz1, One not in Wz1, minusOne not in Wz1])
    return


@app.cell
def _(U2, Wz1, stereoN, stereoN2, x, y, z):
    Proj2N = Wz1.diff_map(U2, {(stereoN.restrict(Wz1), stereoN2): 
                               [x/(1-z), y/(1-z)]},
                          name='P_2^N', latex_name=r'\Pi_2^N')
    Proj2N.display()
    return (Proj2N,)


@app.cell
def _(Phi2, Proj2N, U2, a, b, stereoN2):
    p_5 = U2((a, b), chart=stereoN2)
    Proj2N(Phi2(p_5)) == p_5
    return


@app.cell
def _(Phi2, Proj2N, U, a, assume, b, cos, sin, stereoN):
    assume(cos(a) != 1, cos(a) != 0)
    p_6 = U((sin(a) * cos(b), sin(a) * sin(b), cos(a)), chart=stereoN)
    Phi2(Proj2N(p_6)) == p_6
    return


@app.cell
def _(a, cos, forget):
    forget(cos(a)!=1, cos(a)!=0)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Let $W_{z\not=-1}$ denote the subset of $W\subset\mathbb{S}^3$ defined by $z\not=-1$:
    """)
    return


@app.cell
def _(W, stereoN, z):
    Wzm1 = W.open_subset('Wzm1', latex_name=r'W_{z\not=-1}', 
                         coord_def={stereoN.restrict(W): z!=-1})
    return (Wzm1,)


@app.cell
def _(I, J, K, One, Wzm1, minusK, minusOne):
    all([I in Wzm1, J in Wzm1, K in Wzm1,
         minusK not in Wzm1, One not in Wzm1, 
         minusOne not in Wzm1])
    return


@app.cell
def _(V2, Wzm1, stereoN, stereoS2, x, y, z):
    Proj2S = Wzm1.diff_map(V2, {(stereoN.restrict(Wzm1), stereoS2): 
                                [x/(1+z), y/(1+z)]},
                           name='P_2^S', latex_name=r'\Pi_2^S')
    Proj2S.display()
    return (Proj2S,)


@app.cell
def _(Phi2, Proj2S, V2, a, b, stereoS2):
    p_7 = V2((a, b), chart=stereoS2)
    Proj2S(Phi2(p_7)) == p_7
    return


@app.cell
def _(Phi2, Proj2S, U, a, assume, b, cos, sin, stereoN):
    assume(cos(a) != -1, cos(a) != 0)
    p_8 = U((sin(a) * cos(b), sin(a) * sin(b), cos(a)), chart=stereoN)
    Phi2(Proj2S(p_8)) == p_8
    return


@app.cell
def _(a, cos, forget):
    forget(cos(a)!=-1, cos(a)!=0)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Hopf map

    We are now in position to define the Hopf map as a map $\mathbb{S}^3 \to \mathbb{S}^2$.
    To give its coordinate expressions, we have to consider that $\mathbb{S}^3$ is covered by
    two charts, `stereoN` = $(U,(x,y,z))$ and `stereoS` = $(V,(x',y',z'))$, and $\mathbb{S}^2$ is covered by two charts:
    - `stereoN2` = $(U_2,(x_2,y_2))$, the domain of which contains
      all points of $\mathbb{S}^2$ but $\mathbf{k}$
    - `stereoS2` = $(V_2,(x'_2,y'_2))$, the domain of which contains
      all points of $\mathbb{S}^2$ but $-\mathbf{k}$.

    First we search for all the points $p\in U$ such that $H(p)\in U_2$, i.e. such that
    $H(p)\not=\mathbf{k}$, or equivalently, $z(H(p))\not= 1$, or again $H(p)\in W_{z\not=1}$.
    On the chart $(U,(x,y,z))$, the expression of $z(H(p))$ is
    """)
    return


@app.cell
def _(H_1, stereoN):
    Hx_1, Hy_1, Hz_1 = H_1.expr(stereoN, stereoN)
    Hz_1
    return (Hz_1,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The condition $z(H(p))\not=1$ is
    """)
    return


@app.cell
def _(Hz_1):
    Hz_1.numerator() - Hz_1.denominator() != 0
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    which is equivalent to $x^2+y^2 \not= 0$. We define thus the subdomain
    $D_1 = U \setminus (H^{-1}(\mathbf{k})\cap U)$ as
    """)
    return


@app.cell
def _(U, stereoN, x, y):
    D1 = U.open_subset('D_1', coord_def=({stereoN: x**2 + y**2 != 0}))
    stereoN_D1 = stereoN.restrict(D1)
    return D1, stereoN_D1


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    By construction, the restriction of $H$ to $D_1$ has $W_{z\not=1}$ as codomain and we declare the Hopf map on $D_1$ by considering the image points as points of $\mathbb{S}^2$ via $\Pi_2^N$:
    """)
    return


@app.cell
def _(D1, H_1, Proj2N, Wz1):
    hD1 = Proj2N * H_1.restrict(D1, subcodomain=Wz1)
    hD1.display()
    return (hD1,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We have $\mathbf{i}\in D_1$ and $\mathbf{j}\in D_1$; we can check that
    $h(\mathbf{i}) = h(\mathbf{j}) = -\mathbf{k}$:
    """)
    return


@app.cell
def _(I, J, hD1, minusK2):
    all([hD1(I) == minusK2, hD1(J) == minusK2])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Let us now consider the points $p\in U$ such that $H(p)\in V_2$, i.e. such that
    $H(p)\not=-\mathbf{k}$, or equivalently, $z(H(p))\not= -1$, or again $H(p)\in W_{z\not=-1}$.
    The condition $z(H(p))\not= -1$ is equivalent to $s\not=0$ with
    """)
    return


@app.cell
def _(Hz_1):
    s = ((Hz_1.numerator() + Hz_1.denominator()) / 2).simplify_full()
    s
    return (s,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Since
    """)
    return


@app.cell
def _(s, x, y, z):
    (s - (x**2+y**2+z**2-1)**2).simplify_full()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    the condition $s\not =0$ is equivalent to
    """)
    return


@app.cell
def _(x, y, z):
    (x**2+y**2+z**2-1)**2 + 4*z**2 != 0
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    i.e. to ($x^2+y^2\not= 1$ or $z\not= 0$). Hence we introduce the subset
    $D_2 = U \setminus (H^{-1}(-\mathbf{k})\cap U)$ by
    """)
    return


@app.cell
def _(U, stereoN, x, y, z):
    D2 = U.open_subset('D_2', coord_def=({stereoN: (x**2 + y**2 != 1, z != 0)}))
    stereoN_D2 = stereoN.restrict(D2)
    return D2, stereoN_D2


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    By construction, the restriction of $H$ to $D_2$ has $W_{z\not=-1}$ as codomain and we declare the Hopf map on $D_2$ by considering the image points as points of $\mathbb{S}^2$ via $\Pi_2^S$:
    """)
    return


@app.cell
def _(D2, H_1, Proj2S, Wzm1):
    hD2 = Proj2S * H_1.restrict(D2, subcodomain=Wzm1)
    hD2.display()
    return (hD2,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We have $\mathbf{k}\in D_2$, $-\mathbf{k}\in D_2$ and $\mathbf{1}\in D_2$; we can check that
    $h(\mathbf{k}) = h(-\mathbf{k}) = h(\mathbf{1}) = \mathbf{k}$:
    """)
    return


@app.cell
def _(K, K2, One, hD2, minusK):
    all([hD2(K) == K2, hD2(minusK) == K2, hD2(One) == K2])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Since $H^{-1}(\mathbf{k})\cap H^{-1}(-\mathbf{k})=\emptyset$, we have $U=D_1\cup D_2$:
    """)
    return


@app.cell
def _(D1, D2, U):
    U.declare_union(D1, D2)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Similarly let us consider the points $p\in V$ such that $H(p)\in U_2$, i.e. such that
    $H(p)\not=\mathbf{k}$, or equivalently, $z(H(p))\not= 1$, or again $H(p)\in W_{z\not=1}$.
    On the chart $(V,(x',y',z'))$, the expression of $z(H(p))$ is
    """)
    return


@app.cell
def _(H_1, stereoN, stereoS):
    Hx_2, Hy_2, Hz_2 = H_1.expr(stereoS, stereoN)
    Hz_2
    return (Hz_2,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The condition $z(H(p))\not=1$ is
    """)
    return


@app.cell
def _(Hz_2):
    Hz_2.numerator() - Hz_2.denominator() != 0
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    which is equivalent to ${x'}^2+{y'}^2 \not= 0$. We define thus the subset
    $D_3 = V \setminus (H^{-1}(\mathbf{k})\cap V)$ as
    """)
    return


@app.cell
def _(V, stereoS, xp, yp):
    D3 = V.open_subset('D_3', coord_def=({stereoS: xp**2 + yp**2 != 0}))
    stereoS_D3 = stereoS.restrict(D3)
    return D3, stereoS_D3


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    By construction, the restriction of $H$ to $D_2$ has $W_{z\not=1}$ as codomain and we declare the Hopf map on $D_3$ by considering the image points as points of $\mathbb{S}^2$ via $\Pi_2^N$:
    """)
    return


@app.cell
def _(D3, H_1, Proj2N, Wz1):
    hD3 = Proj2N * H_1.restrict(D3, subcodomain=Wz1)
    hD3.display()
    return (hD3,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We have $\mathbf{i}\in D_3$ and $\mathbf{j}\in D_3$; we can check that
    $h(\mathbf{i}) = h(\mathbf{j}) = -\mathbf{k}$:
    """)
    return


@app.cell
def _(I, J, hD3, minusK2):
    all([hD3(I) == minusK2, hD3(J) == minusK2])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Finally, let us consider the points $p\in V$ such that $H(p)\in V_2$, i.e. such that
    $H(p)\not=-\mathbf{k}$, or equivalently, $z(H(p))\not= -1$, or again $H(p)\in W_{z\not=-1}$.
    The condition $z(H(p))\not= -1$ is equivalent to $s\not=0$ with
    """)
    return


@app.cell
def _(Hz_2):
    s_1 = ((Hz_2.numerator() + Hz_2.denominator()) / 2).simplify_full()
    s_1
    return (s_1,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Since
    """)
    return


@app.cell
def _(s_1, xp, yp, zp):
    (s_1 - (xp**2+yp**2+zp**2 - 1)**2).simplify_full()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    the condition $s\not=0$ is equivalent to
    """)
    return


@app.cell
def _(xp, yp, zp):
    (xp**2+yp**2+zp**2-1)**2 + 4*zp**2 == 0
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    i.e. to (${x'}^2+{y'}^2\not= 1$ or $z'\not= 0$). Hence we introduce the subset
    $D_4 = V \setminus (H^{-1}(-\mathbf{k})\cap V)$ by
    """)
    return


@app.cell
def _(V, stereoS, xp, yp, zp):
    D4 = V.open_subset('D_4', coord_def=({stereoS: (xp**2+yp**2!=1, zp!=0)}))
    stereoS_D4 = stereoS.restrict(D4)
    return D4, stereoS_D4


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    By construction, the restriction of $H$ to $D_4$ has $W_{z\not=-1}$ as codomain and we declare the Hopf map on $D_4$ by considering the image points as points of $\mathbb{S}^2$ via $\Pi_2^S$:
    """)
    return


@app.cell
def _(D4, H_1, Proj2S, Wzm1):
    hD4 = Proj2S * H_1.restrict(D4, subcodomain=Wzm1)
    hD4.display()
    return (hD4,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We have $-\mathbf{1}\in D_4$ and we can check that
    $h(-\mathbf{1}) = \mathbf{k}$:
    """)
    return


@app.cell
def _(K2, hD4, minusOne):
    hD4(minusOne) == K2
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Since $H^{-1}(\mathbf{k})\cap H^{-1}(-\mathbf{k})=\emptyset$, we have $V=D_3\cup D_4$:
    """)
    return


@app.cell
def _(D3, D4, V):
    V.declare_union(D3, D4)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### Declaration of the Hopf map

    We construct the Hopf map $h:\mathbb{S}^3\to \mathbb{S}^2$ from the coordinate expressions of its restriction to $D_1$, $D_2$, $D_3$ and $D_4$, as obtained above:
    """)
    return


@app.cell
def _(
    S2,
    S3,
    hD1,
    hD2,
    hD3,
    hD4,
    stereoN2,
    stereoN_D1,
    stereoN_D2,
    stereoS2,
    stereoS_D3,
    stereoS_D4,
):
    h = S3.diff_map(S2, name='h')
    h.add_expression(stereoN_D1, stereoN2, hD1.expr(stereoN_D1, stereoN2))
    h.add_expression(stereoN_D2, stereoS2, hD2.expr(stereoN_D2, stereoS2))
    h.add_expression(stereoS_D3, stereoN2, hD3.expr(stereoS_D3, stereoN2))
    h.add_expression(stereoS_D4, stereoS2, hD4.expr(stereoS_D4, stereoS2))
    return (h,)


@app.cell
def _(h, stereoN2, stereoN_D1):
    h.display(stereoN_D1, stereoN2)
    return


@app.cell
def _(h, stereoN_D2, stereoS2):
    h.display(stereoN_D2, stereoS2)
    return


@app.cell
def _(h, stereoN2, stereoS_D3):
    h.display(stereoS_D3, stereoN2)
    return


@app.cell
def _(h, stereoS2, stereoS_D4):
    h.display(stereoS_D4, stereoS2)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Let us check that $h(\mathbf{1})=h(-\mathbf{1})=h(\mathbf{k})=h(-\mathbf{k})=\mathbf{k}$
    and $h(\mathbf{i})=h(-\mathbf{i})=h(\mathbf{j})=h(-\mathbf{j})=-\mathbf{k}$:
    """)
    return


@app.cell
def _(I, J, K, K2, One, h, minusI, minusJ, minusK, minusK2, minusOne):
    all([h(One)==K2, h(minusOne)==K2, 
         h(K)==K2, h(minusK)==K2,
         h(I)==minusK2, h(minusI)==minusK2,
         h(J)==minusK2, h(minusJ)==minusK2])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Expression of the Hopf map in spherical coordinates
    """)
    return


@app.cell
def _(A, D1, spher):
    D1A = A.intersection(D1)
    spherD1A = spher.restrict(D1A)
    spherD1A
    return D1A, spherD1A


@app.cell
def _(D1A, stereoN_D1, x, y):
    stereoND1A = stereoN_D1.restrict(D1A, restrictions=(y!=0, x<0))
    #stereoND1A.add_restrictions((y!=0, x<0))
    return (stereoND1A,)


@app.cell
def _(D1A):
    D1A.atlas()
    return


@app.cell
def _(D1A, spher_to_stereoN, spher_to_stereoS, stereoS_to_spher):
    spher_to_stereoND1A = spher_to_stereoN.restrict(D1A)
    stereoN_to_spherD1A = spher_to_stereoN.inverse().restrict(D1A)
    spher_to_stereoSD1A = spher_to_stereoS.restrict(D1A)
    stereoS_to_spherD1A = stereoS_to_spher.restrict(D1A)
    return


@app.cell
def _(h, spherD1A, stereoN2, stereoND1A):
    h.expr(stereoND1A, stereoN2)  # necessary
    h.display(spherD1A, stereoN2)
    return


@app.cell
def _(A2, D1A, h, spher2, spherD1A):
    hA = h.restrict(D1A, subcodomain=A2)
    hA.display(spherD1A, spher2)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Hopf coordinates

    The Hopf coordinates are coordinates $(\eta,\alpha,\beta)$ on $\mathbb{S}^3$ which are related to the Cartesian coordinates on $\mathbb{R}^4$ (via the embedding $\Phi$) by
    $$
    \begin{equation} \tag{1}
        \left\{ \begin{array}{lcl}
            T & = &\cos\eta \sin\alpha \\
            X & = &\sin\eta \cos(\alpha+\beta) \\
            Y & = &\sin\eta \sin(\alpha+\beta) \\
            Z & = &\cos\eta \cos\alpha
          \end{array} \right .
    \end{equation}
    $$
    and whose range is $\eta\in(0,\pi/2)$, $\alpha\in (0, 2\pi)$, $\beta\in (0, 2\pi)$. They are
    defined in $D_1$ minus the points for which $X^2+Y^2+T^2=1$ (limit $\alpha\rightarrow 0$
    or $2\pi$) or $TX-YZ=0$ (limit $\beta\rightarrow 0$ or $2\pi$). In terms of the stereograĥic coordinates, this corresponds to $x^2+y^2+z^2=1$ or to $x(1-x^2-y^2-z^2)-2yz=0$. Hence we declare the domain $B$ of Hopf coordinates as
    """)
    return


@app.cell
def _(D1, stereoN_D1, x, y, z):
    B = D1.open_subset('B', coord_def={stereoN_D1: 
                                       [x**2 + y**2 + z**2 != 1, 
                                        x*(1-x**2-y**2-z**2) - 2*y*z !=0 ]})
    print(B)
    return (B,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The limiting surface $x(1-x^2-y^2-z^2)-2yz=0$, where $\beta\rightarrow 0$ or $2\pi$:
    """)
    return


@app.cell
def _(implicit_plot3d, show, x, y, z):
    beta_zero = implicit_plot3d(x*(1-x**2-y**2-z**2) - 2*y*z == 0, 
                                (x,-3,3), (y,-3,3), (z,-3,3))
    show(beta_zero)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We define the Hopf coordinates and provide the transition map to the stereographic coordinates $(x,y,z)$:
    """)
    return


@app.cell
def _(B):
    Hcoord = B.chart(r"eta:(0,pi/2):\eta alpha:(0,2*pi):\alpha beta:(0,2*pi):\beta")
    eta, alp, bet = Hcoord[:]
    Hcoord
    return Hcoord, alp, bet, eta


@app.cell
def _(B, Hcoord, alp, bet, cos, eta, sin, stereoN):
    Hcoord_to_stereoN = Hcoord.transition_map(
                            stereoN.restrict(B),
                            (sin(eta)*cos(alp+bet)/(1+cos(eta)*sin(alp)),
                             sin(eta)*sin(alp+bet)/(1+cos(eta)*sin(alp)),
                             cos(eta)*cos(alp)/(1+cos(eta)*sin(alp))))
    Hcoord_to_stereoN.display()
    return (Hcoord_to_stereoN,)


@app.cell
def _(Hcoord_to_stereoN, asin, atan2, pi, sqrt, x, y, z):
    Hcoord_to_stereoN.set_inverse(asin(2*sqrt(x**2+y**2)/(1+x**2+y**2+z**2)),
                                  atan2(x**2+y**2+z**2-1, -2*z) + pi,
                                  atan2(-y,-x) - atan2(x**2+y**2+z**2-1, -2*z))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Note that the test of the inverse coordinate transformation is passed, modulo some lack of trigonometric simplifications.
    """)
    return


@app.cell
def _(Hcoord_to_stereoN):
    Hcoord_to_stereoN.inverse().display()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Embedding $\Phi$ in terms of Hopf coordinates
    """)
    return


@app.cell
def _(B, Phi):
    PhiB = Phi.restrict(B)
    PhiB.display()
    return (PhiB,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The expression of $\Phi$ in terms of the Hopf coordinates can be simplified by means of the method `trig_reduce`:
    """)
    return


@app.cell
def _(Hcoord, PhiB, X4):
    PhiB.expression(Hcoord, X4)[1].factor().trig_reduce()
    return


@app.cell
def _(Hcoord, PhiB, X4):
    PhiB.expression(Hcoord, X4)[2].factor().trig_reduce()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Hence the recover the expression (1) above.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Expression of the Hopf map in terms of Hopf coordinates

    The expression of $h$ in terms of stereographic coordinates on $B$ is
    """)
    return


@app.cell
def _(B, h, stereoN, stereoN2):
    h.display(stereoN.restrict(B), stereoN2)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Let us ask for the expression in terms of Hoopf coordinates:
    """)
    return


@app.cell
def _(Hcoord, h, stereoN2):
    h.display(Hcoord, stereoN2)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We notice that the image point in $\mathbb{S}^2$ is independent of the value of $\alpha$.

    The expression of $h$ is even simpler in terms of spherical coordinates on $\mathbb{S}^2$:
    """)
    return


@app.cell
def _(A2, B, Hcoord, h, spher2):
    hB = h.restrict(B, subcodomain=A2)
    hB.display(Hcoord, spher2)
    return (hB,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We are facing some lack of simplification:

    - $\operatorname{atan}(\sin\eta/\cos\eta)$ should simplify to $\eta$
    - the `atan2` function should simplify to $\operatorname{atan2}(\sin\beta,-\cos\beta) = \pi-\beta$, so that $\phi_2=\beta$

    Hence the right-hand side of the above formula simplifies to $(\theta_2,\phi_2)=(2\eta,\beta)$. We enforce it by the method `add_expression`:
    """)
    return


@app.cell
def _(Hcoord, bet, eta, hB, spher2):
    hB.add_expression(Hcoord, spher2, (2*eta, bet))
    hB.display(Hcoord, spher2)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The expression of the Hopf map in terms of the Hopf coordinates is thus very simple, which justifies the name given to these coordinates.
    We also recover a very simple expression when asking to express $C\circ \Phi$ (from which $h$ has been constructed) in terms of the Hopf coordinates:
    """)
    return


@app.cell
def _(B, CS, Hcoord, X4):
    CS.restrict(B).display(Hcoord, X4)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The right-hand side should simplify to
    $$(T,X,Y,Z) = (0, \sin(2\eta)\cos\beta, \sin(2\eta)\sin\beta, \cos(2\eta))$$
    We can (partially) obtain this by means of `trig_reduce()`:
    """)
    return


@app.cell
def _(B, CS, Hcoord, X4, show):
    for cp in CS.restrict(B).expr(Hcoord, X4):
        show(cp.trig_reduce().simplify_full())
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## The Hopf map as a fibration of $\mathbb{S}^3$

    The above results show that the image by $h$ of a point of Hopf coordinates $(\eta,\alpha,\beta)$ is independent of $\alpha$. Since $h$ is surjective, this means that for any point
    $p\in\mathbb{S}^2$, the preimage set $h^{-1}(p)$ corresponds to a fixed value of $(\eta,\beta)$, with $\alpha$ taking all values in the range $(0,2\pi)$. From Eq. (1), the projection of  $h^{-1}(p)$ in the $(T,X)$-plane is a circle of radius $\cos\eta$ centered on $(0,0)$, while its projection in the $(X,Y)$-plane is a circle of radius $\sin\eta$ centered on $(0,0)$. We conclude that $h^{-1}(p)$ is a great circle of $\mathbb{S}^3$, sometimes called a *Hopf circle*.

    It follows that $\mathbb{S}^3$ has the structure of a **fiber bundle** over $\mathbb{S}^2$ with
    $\mathbb{S}^1$ fibers. The Hopf map $h:\mathbb{S}^3\to\mathbb{S}^2$ is then nothing but the projection map of this bundle.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We can get a first view of the fibers by plotting the Hopf coordinates in terms of the stereographic ones, for a fixed value of $\eta$ ($\eta=\pi/4$): the lines along which $\alpha$ varies while $\beta$ is kept fixed, hence the fibers $h^{-1}(p)$, are plotted in green. They are
    indeed circles (remember that stereographic projection preserves circles):
    """)
    return


@app.cell
def _(Hcoord, alp, bet, eta, pi, show, stereoN):
    graph_4 = Hcoord.plot(stereoN, fixed_coords={eta: pi / 4}, 
                          color={alp: 'green', bet: 'orange'}, 
                          number_values=9, label_axes=False)
    show(graph_4, axes_labels=['x', 'y', 'z'])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Note that all the green circles are linked.
    The same plot, but in terms of the coordinates $(X,Y,T)$ of $\mathbb{R}^4$ via the embedding $\Phi$:
    """)
    return


@app.cell
def _(Hcoord, PhiB, T, X, X4, Y, alp, bet, eta, pi, show):
    graph_5 = Hcoord.plot(X4, mapping=PhiB, ambient_coords=(X, Y, T), 
                          fixed_coords={eta: pi / 4}, 
                          color={alp: 'green', bet: 'orange'}, 
                          number_values=9, label_axes=False)
    show(graph_5, axes_labels=['X', 'Y', 'T'])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We may fix $\beta$ instead of $\eta$, in plotting the Hopf coordinates in terms of the stereographic ones. The fibers are still the green circles, the red lines being lines along which $\eta$ varies at fixed $\alpha$. Again, note that all the green circles are linked.
    """)
    return


@app.cell
def _(Hcoord, alp, bet, eta, pi, show, stereoN):
    graph_6 = Hcoord.plot(stereoN, fixed_coords={bet: pi / 2}, ranges={eta: (0.25, 1.5)}, 
                          color={eta: 'red', alp: 'green'}, 
                          number_values=9, plot_points=150, label_axes=False)
    show(graph_6, axes_labels=['x', 'y', 'z'])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    If we vary the three coordinates $(\eta,\alpha,\beta)$, we get the following plots, where $\mathbb{S}^3$ appears as filled by the grid of Hoopf coordinates:
    """)
    return


@app.cell
def _(Hcoord, PhiB, X, X4, Y, Z, alp, bet, eta, show):
    graph_7 = Hcoord.plot(X4, mapping=PhiB, ambient_coords=(X, Y, Z), 
                          color={eta: 'red', alp: 'green', bet: 'orange'}, 
                          number_values=7, label_axes=False)
    show(graph_7, axes_labels=['X', 'Y', 'Z'])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Fibers of the Hopf fibration

    For a point $p\in\mathbb{S}^2$, identified by its spherical coordinates $(\theta_2,\phi_2)=(2\eta,\beta)$, the fiber $h^{-1}(p)$ can be seen as a curve in $\mathbb{S}^3$:
    """)
    return


@app.cell
def _(Hcoord, S3, manifolds, pi):
    R = manifolds.RealLine()
    t = R.canonical_coordinate()
    def fiber(eta, bet):
        return S3.curve({Hcoord: (eta, t, bet)}, (t, 0, 2*pi))

    return (fiber,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    For instance, the fiber above the point $(\theta_2,\phi_2)=(\pi/3,\pi/4)$ is
    """)
    return


@app.cell
def _(fiber, pi):
    F = fiber(pi/6, pi/4)
    F
    return (F,)


@app.cell
def _(F):
    F.display()
    return


@app.cell
def _(F, stereoN):
    graph_F = F.plot(chart=stereoN, color='green', plot_points=100)
    graph_F
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Plot of the fibers

    Let us plot the fibers for three values of $\eta$: $\eta=\pi/6$ (turquoise), $\eta=\pi/4$ (gold)
    and $\eta=5\pi/12$ (red). For each value of $\eta$, we note that the fibers fill a torus.
    """)
    return


@app.cell
def _(B, Graphics, fiber, pi, stereoN):
    graph_8 = Graphics()
    etas = {pi / 6: ['turquoise', (0, 2 * pi), 30], 
            pi / 4: ['gold', (0, 2 * pi), 30], 
            5 * pi / 12: ['red', (0, 2 * pi), 30]}
    for eta_v, param in etas.items():
        color = param[0]
        beta_min, beta_max = param[1]
        nb = param[2]
        db = (beta_max - beta_min) / (nb - 1)
        betas = [beta_min + db * k for k in range(nb)]
        for beta_v in betas:
            F_1 = fiber(eta_v, beta_v)
            F_1.coord_expr(stereoN.restrict(B))
            graph_8 += F_1.plot(chart=stereoN, color=color, 
                                plot_points=150, label_axes=None)
    graph_8
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    A "top" view of the fibers, obtained by projection to the $(x,y)$-plane (note that for clarity, we have reduced the number of fibers from 30 to 12):
    """)
    return


@app.cell
def _(B, Graphics, fiber, pi, show, stereoN, x, y):
    graph_9 = Graphics()
    etas_1 = {pi / 6: ['turquoise', (0, 2 * pi), 12], 
              pi / 4: ['gold', (0, 2 * pi), 12], 
              5 * pi / 12: ['red', (0, 2 * pi), 12]}
    for eta_v_1, param_1 in etas_1.items():
        color_1 = param_1[0]
        beta_min_1, beta_max_1 = param_1[1]
        nb_1 = param_1[2]
        db_1 = (beta_max_1 - beta_min_1) / (nb_1 - 1)
        betas_1 = [beta_min_1 + db_1 * k for k in range(nb_1)]
        for beta_v_1 in betas_1:
            F_2 = fiber(eta_v_1, beta_v_1)
            F_2.coord_expr(stereoN.restrict(B))
            graph_9 += F_2.plot(chart=stereoN, ambient_coords=(x, y), 
                                color=color_1, plot_points=150)
    show(graph_9, aspect_ratio=1)
    return (etas_1,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The same fibers, but viewed in $\mathbb{R}^4$ (via the embedding $\Phi$), in terms of the coordinates $(T,X,Z)$:
    """)
    return


@app.cell
def _(B, Graphics, Phi, T, X, X4, Z, etas_1, fiber, show, stereoN):
    graph_10 = Graphics()
    for eta_v_2, param_2 in etas_1.items():
        color_2 = param_2[0]
        beta_min_2, beta_max_2 = param_2[1]
        nb_2 = param_2[2]
        db_2 = (beta_max_2 - beta_min_2) / (nb_2 - 1)
        betas_2 = [beta_min_2 + db_2 * k for k in range(nb_2)]
        for beta_v_2 in betas_2:
            F_3 = fiber(eta_v_2, beta_v_2)
            F_3.coord_expr(stereoN.restrict(B))
            graph_10 += F_3.plot(chart=X4, ambient_coords=(X, Z, T), mapping=Phi, 
                                 color=color_2, plot_points=200, label_axes=None)
    show(graph_10, axes_labels=['X', 'Z', 'T'])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    or in terms of the coordinates $(X,Y,Z)$:
    """)
    return


@app.cell
def _(B, Graphics, Phi, X, X4, Y, Z, etas_1, fiber, show, stereoN):
    graph_11 = Graphics()
    for eta_v_3, param_3 in etas_1.items():
        color_3 = param_3[0]
        beta_min_3, beta_max_3 = param_3[1]
        nb_3 = param_3[2]
        db_3 = (beta_max_3 - beta_min_3) / (nb_3 - 1)
        betas_3 = [beta_min_3 + db_3 * k for k in range(nb_3)]
        for beta_v_3 in betas_3:
            F_4 = fiber(eta_v_3, beta_v_3)
            F_4.coord_expr(stereoN.restrict(B))
            graph_11 += F_4.plot(chart=X4, ambient_coords=(X, Y, Z), mapping=Phi, 
                                 color=color_3, plot_points=100, label_axes=None)
    show(graph_11, axes_labels=['X', 'Y', 'Z'])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    In this notebook, we have used 18 charts on $\mathbb{S}^3$:
    """)
    return


@app.cell
def _(S3):
    S3.atlas()
    return


@app.cell
def _(S3):
    len(S3.atlas())
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    corresponding actually to 4 different coordinate systems:
    """)
    return


@app.cell
def _(S3):
    S3.top_charts()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    For a follow-up, see the [notebook devoted to vector fields](http://nbviewer.jupyter.org/github/sagemanifolds/SageManifolds/blob/master/Notebooks/SM_sphere_S3_vectors.ipynb) on $\mathbb{S}^3$.

    You may also visit [Niles Johnson's page](http://nilesjohnson.net/hopf.html) for a very nice
    animated 3D visualization of the Hopf fibration, also constructed with SageMath.
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
