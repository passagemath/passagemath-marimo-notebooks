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
    # SageManifolds example notebook using [passagemath](https://github.com/passagemath): Visualizing the horizons and ergosurfaces of Kerr spacetime
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
        sum, srange
    )
    from passagemath_plot import (
        show, sphere, colormaps, parametric_plot3d, text3d, Graphics, animate
    )
    from passagemath_repl import get_display_manager; dm = get_display_manager()
    return (
        EuclideanSpace,
        Graphics,
        Parallelism,
        RR,
        acos,
        animate,
        assume,
        colormaps,
        cos,
        integral,
        manifolds,
        mo,
        parametric_plot3d,
        pi,
        show,
        sin,
        solve,
        srange,
        sum,
        text3d,
        var,
        vector,
    )


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    This marimo notebook, adapted from a Jupyter notebook by **Rogerio T. Cavalcanti** published in https://sagemanifolds.obspm.fr/examples.html, illustrates some applications of SageMath functionalities in general relativity, specifically in deriving and displaying the horizons and ergosurfaces of the Kerr spacetime.

    Most of the involved tools are part of the [SageManifolds project](https://sagemanifolds.obspm.fr/). They are now available in Python environments via the modularized distributions of the Sage library developed by the [passagemath](https://github.com/passagemath) project.
    - The SageManifolds functionality is shipped as part of [passagemath-symbolics](https://pypi.org/project/passagemath-symbolics/).
    - The pip-installable package [passagemath-maxima](https://pypi.org/project/passagemath-maxima/) provides the backend for symbolic computation.
    - [passagemath-plot](https://pypi.org/project/passagemath-plot/) provides 2D and 3D plotting facilities.
    - [passagemath-repl](https://pypi.org/project/passagemath-repl/) provides the integration with the marimo notebook.
    """)
    return


@app.cell
def _(Parallelism):
    Parallelism().set(nproc=3)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Kerr spacetime in Boyer–Lindquist coordinates
    """)
    return


@app.cell
def _(manifolds, var):
    a = var('a', domain='positive')
    M = manifolds.Kerr(m=1, a=a, coordinates='BL', 
                       names=['t', 'r', 'th', 'ph'])
    BL = M.default_chart()
    t_BL, r_BL, th_BL, ph_BL = BL[:]
    return BL, M, a, ph_BL, r_BL, t_BL, th_BL


@app.cell
def _(M):
    g = M.metric()
    g.display_comp()
    return (g,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Metric singularities and ergosurfaces
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The $g_{tt},g_{t\phi}$ and $g_{\phi\phi}$ components are singular at the singular ring $a^2\cos^2\theta +r^2=0$, that is $r=0$ and $\theta =\frac{\pi}{2}$. It corresponds to a physical singularity, as checked below.
    """)
    return


@app.cell
def _(pi, r_BL, th_BL):
    singular_ring = {r_BL: 0, th_BL: pi/2}
    return (singular_ring,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Singular surfaces on $\displaystyle ({g_{rr}})^{-1} = 0$ (Horizons)
    """)
    return


@app.cell
def _(g, r_BL, solve):
    horizons = solve(1/g[1,1].expr()==0, r_BL, solution_dict=True)
    horizons
    return (horizons,)


@app.cell
def _(horizons):
    inner_horizon, outer_horizon = horizons
    return inner_horizon, outer_horizon


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The ergosurfaces are the regions of vanishing $K_\mu K^\mu$, where $K = \frac{\partial}{\partial t }$ is a Killing vector field.
    """)
    return


@app.cell
def _(M):
    K = M.vector_field(1,0,0,0, name='K')
    K.display()
    return (K,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Checking if $K$ is a Killing vector field $(\mathcal{L}_{_K}g = 0)$
    """)
    return


@app.cell
def _(K, g):
    g.lie_derivative(K) == 0
    return


@app.cell
def _(K, g):
    g(K,K).display()
    return


@app.cell
def _(K, g, r_BL, solve):
    ergosurfaces = solve(g(K,K).expr(), r_BL, solution_dict=True)
    ergosurfaces
    return (ergosurfaces,)


@app.cell
def _(ergosurfaces):
    inner_ergo, outer_ergo = ergosurfaces
    return inner_ergo, outer_ergo


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    List of surfaces
    """)
    return


@app.cell
def _(inner_ergo, inner_horizon, outer_ergo, outer_horizon, singular_ring):
    surfaces_param = [outer_ergo,outer_horizon,inner_horizon,inner_ergo,singular_ring]
    return (surfaces_param,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Rational polynomial coordinates
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    In rational polynomial coordinates all components of the Kerr metric are rational polynomials, which in principle make it easyer to handle. We are going to use such coordinates for checking the Kretschmann scalar over the horizon and ergosurfaces of the spacetime.
    """)
    return


@app.cell
def _(M):
    RP = M.chart(r't:(-oo,+oo) r:(0,+oo) ch:(-1,1):\chi ph:(-pi,pi):periodic:\phi')
    t, r, ch, ph = RP[:]
    return RP, ch, ph, r, t


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Transition map from Boyer–Lindquist coordinates to rational polynomial coordinates and its inverse.
    """)
    return


@app.cell
def _(BL, RP, cos, ph_BL, r_BL, t_BL, th_BL):
    BL_to_RP = BL.transition_map(RP, [t_BL, r_BL, cos(th_BL), ph_BL])
    BL_to_RP.display()
    return (BL_to_RP,)


@app.cell
def _(BL_to_RP, acos, ch, ph, r, t):
    BL_to_RP.set_inverse(t, r, acos(ch), ph)
    BL_to_RP.inverse().display()
    return


@app.cell
def _(RP, g):
    g.display_comp(RP.frame(), RP)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Setting the default chart and frame
    """)
    return


@app.cell
def _(M, RP):
    M.set_default_chart(RP)
    return


@app.cell
def _(M, RP):
    M.set_default_frame(RP.frame())
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Riemann tensor, Ricci tensor and Kretschmann scalar
    """)
    return


@app.cell
def _(g):
    Riem = g.riemann()
    return (Riem,)


@app.cell
def _(g):
    Ric = g.ricci()
    return (Ric,)


@app.cell
def _(Ric):
    Ric == 0
    return


@app.cell
def _(Riem, g):
    R_up = Riem.up(g)
    return (R_up,)


@app.cell
def _(Riem, g):
    R_down = Riem.down(g)
    return (R_down,)


@app.cell
def _(R_down, R_up):
    Kretschmann_scalar = R_up['^{abcd}']*R_down['_{abcd}']
    return (Kretschmann_scalar,)


@app.cell
def _(Kretschmann_scalar):
    Kretschmann_scalar.display()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Getting and factoring the symbolic expression in the default chart
    """)
    return


@app.cell
def _(Kretschmann_scalar):
    K_scalar = Kretschmann_scalar.expr().factor()
    K_scalar
    return (K_scalar,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Kretschmann scalar along the singular ring, horizons and ergosurfaces
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Singular Ring $(r=0,\chi=0)$
    """)
    return


@app.cell
def _(K_scalar):
    K_scalar.subs(r=0)
    return


@app.cell
def _(K_scalar):
    K_scalar.subs(ch=0)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Outer ergosurface, outer horizon and inner horizon at $\chi = 0$
    """)
    return


@app.cell
def _(K_scalar, ch, cos, show, th_BL):
    for k in ['outer_ergo', 'outer_horizon', 'inner_horizon']:
        show(k)
        show(K_scalar.subs(eval(k)).subs({cos(th_BL): ch}).subs(ch=0))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Inner ergosurface for $\chi \neq 0$ (the inner ergosurface coincides with the singular ring at $\chi = 0$)
    """)
    return


@app.cell
def _(K_scalar, ch, cos, inner_ergo, th_BL):
    K_inner_ergo = K_scalar.subs(inner_ergo).subs({cos(th_BL): ch}).canonicalize_radical()
    K_inner_ergo
    return (K_inner_ergo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Series expansion up to $O(\chi^5)$
    """)
    return


@app.cell
def _(K_inner_ergo, ch):
    K_inner_ergo.series(ch, 5)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Setting the default chart and frame back to Boyer–Lindquist
    """)
    return


@app.cell
def _(BL, M):
    M.set_default_chart(BL)
    M.set_default_frame(BL.frame())
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Kerr coordinates
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The Kerr original coordinates will be used as an intermediate step for introducing the Kerr-Schild coordinates.
    """)
    return


@app.cell
def _(M):
    Kr = M.chart(r'u:(-oo,+oo) r:(0,+oo) th:(0,pi):\theta vph:(-pi,pi):periodic:\varphi')
    u_Kr, r_Kr, th_Kr, vph_Kr = Kr[:]
    return Kr, r_Kr, th_Kr, u_Kr, vph_Kr


@app.cell
def _(a, assume, integral, r):
    f = (r/(a**2+r**2-2*r)).function(r)
    assume(a<1)
    F = integral(f(r), r).function(r)
    return (F,)


@app.cell
def _(BL, F, Kr, a, r_Kr, th_Kr, u_Kr, vph_Kr):
    Kr_to_BL = Kr.transition_map(BL, [
        u_Kr - 2*F(r_Kr), 
        r_Kr, 
        th_Kr, 
        vph_Kr - a*F(r_Kr)
    ])
    Kr_to_BL.display()
    return (Kr_to_BL,)


@app.cell
def _(Kr_to_BL):
    Kr_to_BL.inverse().display()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Showing the change of frame from BL to Kerr
    """)
    return


@app.cell
def _(BL, Kr, M):
    M.change_of_frame(BL.frame(), Kr.frame())[:]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Surfaces in Kerr-Schild coordinates
    """)
    return


@app.cell
def _(M):
    KS = M.chart(names=['u', 'x', 'y', 'z'])
    u_KS, x_KS, y_KS, z_KS = KS[:]
    return (KS,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Change of coordinates from Kerr to Kerr-Schild
    """)
    return


@app.cell
def _(KS, Kr, a, cos, r_Kr, sin, th_Kr, u_Kr, vph_Kr):
    Kr_to_KS = Kr.transition_map(KS, [
        u_Kr, 
        (r_Kr*cos(vph_Kr) - a*sin(vph_Kr))*sin(th_Kr),
        (r_Kr*sin(vph_Kr) + a*cos(vph_Kr))*sin(th_Kr),
        r_Kr*cos(th_Kr)
    ])
    Kr_to_KS.display()
    return (Kr_to_KS,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Parametrization of the surfaces in Kerr-Schild coordinates
    """)
    return


@app.cell
def _(Kr_to_KS, r_Kr, surfaces_param, th_Kr, u_Kr, vector, vph_Kr):
    surfaces_KS = [vector([s.subs(param) 
                           for s in Kr_to_KS(u_Kr, r_Kr, th_Kr, vph_Kr)[1:]]) 
                   for param in surfaces_param]
    return (surfaces_KS,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Plotting
    """)
    return


@app.cell
def _(colormaps, pi):
    # plotting data
    surfs_data = {
        'outer_ergo': {
            'name': 'Outer ergosurface',
            'color': 'gray',
            'z_label': 1,
            'param_index': 0,
            'phi1': 7*pi/5,
            'plot_points_factor': 1,
        },
        'outer_horizon': {
            'name': 'Outer horizon', 
            'color': colormaps.Set1(1)[:3], 
            'z_label': .5,
            'param_index': 1, 
            'phi1': 7*pi/5, 
            'plot_points_factor': 1,
        },
        'inner_horizon': {
            'name': 'Inner horizon', 
            'color': colormaps.Set1(4)[:3], 
            'z_label': 0,
            'param_index': 2, 
            'phi1': 6*pi/5, 
            'plot_points_factor': .7,
        },
        'inner_ergo': {
            'name': 'Inner ergosurface',
            'color': colormaps.Set1(3)[:3],
            'z_label': -0.5,
            'param_index': 3,
            'phi1': 2*pi,
            'plot_points_factor': .7,
        },
    }
    return (surfs_data,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Python function for plotting the surfaces
    """)
    return


@app.cell
def _(
    Graphics,
    RR,
    parametric_plot3d,
    pi,
    sum,
    surfs_data,
    text3d,
    th_Kr,
    vph_Kr,
):
    def kerr_surfaces(surf, a=.99, print_labels=True, plot_points=30, 
                      mesh=True, **kwargs):
        if a > 1 or a < 0:
            raise ValueError("choose 'a' between 0 and 1")
        # Labels
        if print_labels:
            Ker_BH = text3d('Kerr black hole', (-2,-5,2.5), 
                            fontsize='200%', fontfamily='serif', 
                            fontweight='bold')
            sep_line = text3d(r'___', (-2,-5,1.7), 
                              fontsize='160%', fontfamily='serif', 
                              fontweight='bold')
            a_label = text3d('a = ' + str(RR(a).n(digits=5)), (-2,-5,2), 
                             fontsize='170%')
            s_ring_label = text3d('Singular ring', (-2,-5,-1), 
                                  color='red', fontsize='170%', 
                                  fontfamily='serif')
            labels = sum([text3d(S['name'], (-2, -5, S['z_label']),
                                 color=S['color'],
                                 fontsize='170%', 
                                 fontfamily='serif') 
                          for S in surfs_data.values()])
            labels += Ker_BH + a_label + s_ring_label + sep_line
        else: 
            labels = Graphics()
        # Surfaces
        s_ring = parametric_plot3d(surf[4].subs(a=a), (vph_Kr, 0, 2*pi), 
                                   color='red', thickness=4)
        plots = sum(
            parametric_plot3d(surf[S['param_index']].subs(a=a),
                              (th_Kr, 0, pi),
                              (vph_Kr, 0, S['phi1']), 
                              color=S['color'], 
                              mesh=mesh,
                              plot_points=S['plot_points_factor']*plot_points, 
                              frame=False, 
                              **kwargs) 
            for S in surfs_data.values())
        plots += s_ring
        return plots + labels

    return (kerr_surfaces,)


@app.cell
def _(kerr_surfaces, surfaces_KS):
    kerr_surfaces(surfaces_KS, 0.999, 
                  viewpoint=[[-0.6557,-0.5284,-0.5394], 112.41])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Immersion in Euclidean space
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We can also see the surfaces immersed in the Euclidean space $\mathbb{E}^3$.
    """)
    return


@app.cell
def _(EuclideanSpace):
    E = EuclideanSpace(3)
    spherical = E.spherical_coordinates()
    r_E, th_E, ph_E = spherical[:]
    return E, spherical


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Differential map from Kerr coordinates to the Euclidean space
    """)
    return


@app.cell
def _(E, Kr, M, r_Kr, spherical, th_Kr, vph_Kr):
    Kr_to_E = M.diff_map(E, {(Kr, spherical): [r_Kr,th_Kr,vph_Kr]}, 
                         name='Kr_to_E', 
                         latex_name=r'\Phi_{_{\text{Kerr} \to \mathbb{E}^3}}')
    return (Kr_to_E,)


@app.cell
def _(Kr_to_E):
    Kr_to_E.display()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Coordinates in Euclidean space
    """)
    return


@app.cell
def _(Kr, Kr_to_E, M, r_Kr, th_Kr, u_Kr, vph_Kr):
    coordinates = Kr_to_E(M.point((u_Kr,r_Kr,th_Kr,vph_Kr), 
                                  chart=Kr)).coordinates()
    return (coordinates,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Surfaces in Euclidean space
    """)
    return


@app.cell
def _(coordinates, surfaces_param, vector):
    surfaces_E = [vector([s.subs(param) for s in coordinates]) 
                  for param in surfaces_param]
    return (surfaces_E,)


@app.cell
def _(kerr_surfaces, surfaces_E, theme):
    kerr_surfaces(surfaces_E, .96, 
                  viewpoint=[[-0.8499,-0.3478,-0.396], 91.88],
                  theme=theme)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Animating the surfaces
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We now create an animation by varying the parameter $a$.
    """)
    return


@app.cell
def _(kerr_surfaces, mo, srange, surfaces_KS, theme):
    mo._runtime.context.get_context().marimo_config["runtime"]["output_max_bytes"] = 20000000
    frames1 = [kerr_surfaces(surfaces_KS,k, theme=theme, 
                             viewpoint=[[-0.6557,-0.5284,-0.5394], 112.41]) 
               for k in srange(0,.5,.1)]
    frames2 = [kerr_surfaces(surfaces_KS,k, theme=theme, 
                             viewpoint=[[-0.6557,-0.5284,-0.5394], 112.41]) 
               for k in srange(.5,.95,.075)]
    frames3 = [kerr_surfaces(surfaces_KS,k, theme=theme, 
                             viewpoint=[[-0.6557,-0.5284,-0.5394], 112.41]) 
               for k in srange(.95,.9999,.005)]
    frames4 = [kerr_surfaces(surfaces_KS,k, theme=theme, 
                             viewpoint=[[-0.6557,-0.5284,-0.5394], 112.41]) 
               for k in srange(.9999,1,.000045)]
    frames = frames1 + frames2 + frames3 + frames4
    return (frames,)


@app.cell
def _(animate, frames):
    animate(frames).interactive()
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
