# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "cysignals==1.12.6",
#     "marimo",
#     "matplotlib==3.10.9",
#     "passagemath-cmr[test]==10.8.4",
#     "passagemath-flint==10.8.4",
#     "passagemath-graphs==10.8.4",
#     "passagemath-nauty==10.8.4",
#     "passagemath-plot==10.8.4",
#     "passagemath-polyhedra[flint]==10.8.4",
#     "passagemath-repl==10.8.4",
# ]
# ///

import marimo

__generated_with = "0.23.15"
app = marimo.App(
    width="medium",
    css_file="/usr/local/_marimo/custom.css",
    auto_download=["html"],
)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # Example for [passagemath-cmr](https://pypi.org/project/passagemath-cmr/)

    This notebook illustrates Seymour's decomposition of totally unimodular matrices and regular matroids provided by [passagemath-cmr](https://pypi.org/project/passagemath-cmr/) – one of the modularized pip-installable packages of the Sage library provided by the [passagemath project](https://github.com/passagemath).

    Use the "Packages" tab on the left to uv-install `passagemath-cmr[test] passagemath-polyhedra[flint] passagemath-nauty passagemath-plot` for the functionality tested in this marimo notebook.
    """)
    return


@app.cell
def _():
    import marimo as mo
    import passagemath_polyhedra, passagemath_flint, passagemath_graphs, passagemath_nauty, passagemath_repl
    from passagemath_cmr import matrix, unicode_art
    from passagemath_graphs import matroids, Matroid, Graph, DiGraph, QQ, ZZ, graphs, digraphs

    return (
        DiGraph,
        Graph,
        Matroid,
        QQ,
        ZZ,
        digraphs,
        graphs,
        matrix,
        matroids,
        mo,
        unicode_art,
    )


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 3.1 Matrices

    The pip-installable package `passagemath-cmr` extends standard matrix types with specialized methods for Seymour's decomposition and recognition of totally unimodular (TU) matrices.
    """)
    return


@app.cell
def _(matrix):
    A = matrix([[1, 0], [-1, -1], [0, 1]], column_keys=['a', 'b'], row_keys=range(3)); A
    return (A,)


@app.cell
def _(A):
    A._unicode_art_matrix()
    return


@app.cell
def _(A):
    result, certificate = A.is_totally_unimodular(certificate=True); result, certificate
    return (certificate,)


@app.cell
def _(certificate):
    certificate.graph()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    All of these methods are made available by delegating to a specialized matrix element class `Matrix_cmr_chr_sparse`, in which matrices are backed by the CMR library.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 3.2 Module morphisms

    The package `passagemath-modules` provides linear algebra facilities in a style favored in algebraic combinatorics. Users can define vector spaces and free modules with distinguished bases whose elements are indexed by arbitrary objects. Linear maps (module morphisms) between such vector spaces or modules are represented by matrices whose rows and columns are indexed by the basis indices.
    """)
    return


@app.cell
def _(matrix):
    A2 = matrix([[-1,  0,  0,  0,  1, -1,  0],
                 [ 1,  0,  0,  1, -1,  1,  0],
                 [ 0, -1,  0, -1,  1, -1,  0],
                 [ 0,  1,  0,  0,  0,  0,  1],
                 [ 0,  0,  1, -1,  1,  0,  1],
                 [ 0,  0, -1,  1, -1,  0,  0]],
                column_keys=['a', 'b', 'c', 'd', 'e', 'f', 'g'],
                row_keys=range(6))
    return (A2,)


@app.cell
def _(A2):
    A2._unicode_art_matrix()
    return


@app.cell
def _(A2):
    A2_result, A2_certificate = A2.is_totally_unimodular(certificate=True); A2_result, A2_certificate
    return (A2_certificate,)


@app.cell
def _(A2_certificate):
    A2_certificate.graph().incidence_matrix(vertices=True,edges=True)._unicode_art_matrix()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 3.3 Graphs

    Graph structures have a direct link to total unimodularity. The vertex-edge incidence matrix of any directed graph is totally unimodular.
    """)
    return


@app.cell
def _(DiGraph):
    G_directed = DiGraph([(0, 1), (1, 2), (2, 0)])
    m_directed = G_directed.incidence_matrix(oriented=True)
    res_directed, cert_directed = m_directed.is_totally_unimodular(certificate=True)
    return cert_directed, res_directed


@app.cell
def _(cert_directed, res_directed):
    res_directed, cert_directed
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    For undirected graphs, the incidence matrix is totally unimodular if and only if the graph is bipartite.
    """)
    return


@app.cell
def _(Graph):
    c4 = Graph([(0, 1), (1, 2), (2, 3), (3, 0)])
    c5 = Graph([(0, 1), (1, 2), (2, 3), (3, 4), (4, 0)])
    res_c4 = c4.incidence_matrix().is_totally_unimodular()
    res_c5, cert_c5 = c5.incidence_matrix().is_totally_unimodular(certificate=True)
    return cert_c5, res_c4, res_c5


@app.cell
def _(cert_c5, res_c4, res_c5):
    print("C4 is TU:", res_c4)
    print("C5 is TU:", res_c5)
    print("C5 certificate violating root node:", cert_c5[0])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 3.3.1 Odd Cycle Packing Number

    We can check whether a connected undirected graph has odd cycle packing number $\mathrm{ocp}(G) \le 1$. It is done by first checking if the incidence matrix is totally unimodular. If so, it is a bipartite graph with no odd cycle ($\mathrm{ocp}(G) = 0$). If not, we can find a basis $B$, which contains at least one odd cycle (otherwise it cannot be a basis). Then by left multiplying the inverse of the basis and checking if the obtained matrix is totally unimodular, we can claim that the graph has odd cycle packing number $\log_2(|\det(B)|)$ (which is 1) if the obtained matrix is totally unimodular.

    In the following implementation, we use the `rref` function to compute the new matrix after left multiplying the inverse of the basis for efficiency.
    """)
    return


@app.cell
def _(graphs):
    gt = graphs.GrotzschGraph()
    At = gt.incidence_matrix(vertices=True, edges=True).matrix()
    res_gt_tu, cert_gt_tu = At.is_totally_unimodular(certificate=True)
    res_gt_rref_tu, cert_gt_rref_tu = At.rref().is_totally_unimodular(certificate=True)
    return cert_gt_rref_tu, cert_gt_tu, res_gt_rref_tu, res_gt_tu


@app.cell
def _(cert_gt_rref_tu, cert_gt_tu, res_gt_rref_tu, res_gt_tu):
    print("Grötzsch Graph incidence matrix is TU:", res_gt_tu)
    print("Grötzsch Graph certificate:", cert_gt_tu)
    print("Grötzsch Graph rref matrix is TU:", res_gt_rref_tu)
    print("Grötzsch Graph rref certificate:", cert_gt_rref_tu)
    return


@app.cell
def _(graphs):
    A_K6 = graphs.CompleteGraph(6).incidence_matrix()
    res_K6_tu, cert_K6_tu = A_K6.is_totally_unimodular(certificate=True)
    res_K6_rref_tu, cert_K6_rref_tu = A_K6.rref().is_totally_unimodular(certificate=True)
    return cert_K6_rref_tu, cert_K6_tu, res_K6_rref_tu, res_K6_tu


@app.cell
def _(cert_K6_rref_tu, cert_K6_tu, res_K6_rref_tu, res_K6_tu):
    print("K6 incidence matrix is TU:", res_K6_tu)
    print("K6 certificate:", cert_K6_tu)
    print("K6 rref matrix is TU:", res_K6_rref_tu)
    print("K6 rref certificate:", cert_K6_rref_tu)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 3.3.2 Recognition algorithm of network matrices

    The `passagemath-cmr` package also provides the recognition algorithm of network matrices. It can return the directed graph certificate of a network matrix, which can be used to reconstruct the original matrix.
    """)
    return


@app.cell
def _(matrix):
    A2_g = matrix([[-1,  0,  0,  0,  1, -1,  0],
                 [ 1,  0,  0,  1, -1,  1,  0],
                 [ 0, -1,  0, -1,  1, -1,  0],
                 [ 0,  1,  0,  0,  0,  0,  1],
                 [ 0,  0,  1, -1,  1,  0,  1],
                 [ 0,  0, -1,  1, -1,  0,  0]],
                column_keys=['a', 'b', 'c', 'd', 'e', 'f', 'g'],
                row_keys=range(6))
    return (A2_g,)


@app.cell
def _(A2_g):
    A2_g_result, A2_g_certificate = A2_g.is_totally_unimodular(certificate=True); A2_g_result, A2_g_certificate
    return (A2_g_certificate,)


@app.cell
def _(A2_g_certificate):
    G_g = A2_g_certificate.graph()
    return (G_g,)


@app.cell
def _(G_g):
    M_g = G_g.incidence_matrix(vertices=True, edges=True)
    return (M_g,)


@app.cell
def _(M_g):
    M_g._unicode_art_matrix()
    return


@app.cell
def _(A2_g_certificate, G_g, M_g):
    row_keys_g, forest_order_g = zip(*A2_g_certificate.forest_edges().items())
    column_keys_g, coforest_order_g = zip(*A2_g_certificate.coforest_edges().items())
    row_order_g = G_g.vertices()[:-1]
    AA_g = M_g.matrix(row_order=row_order_g, column_order=forest_order_g).inverse() * M_g.matrix(row_order=row_order_g, column_order=coforest_order_g)
    print(AA_g)
    return AA_g, column_keys_g, row_keys_g


@app.cell
def _(A2_g, AA_g, ZZ, column_keys_g, matrix, row_keys_g):
    matrix(AA_g, base_ring=ZZ, row_keys=row_keys_g, column_keys=column_keys_g) == A2_g
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Here are some more examples of the two excluded minors $K_5$, $K_{3,3}$ for conetwork/network matrices.
    """)
    return


@app.cell
def _(digraphs):
    K5 = digraphs.Complete(5)
    M_K5 = K5.incidence_matrix()
    return (M_K5,)


@app.cell
def _(M_K5):
    M_K5.is_conetwork_matrix()
    return


@app.cell
def _(M_K5):
    M_K5.is_network_matrix()
    return


@app.cell
def _(graphs):
    K33_undirect = graphs.CompleteBipartiteGraph(3, 3)
    K33 = K33_undirect.orient(lambda e: e if e[0] < e[1] else (e[1], e[0], e[2]))
    M_K33 = K33.incidence_matrix(vertices=True, edges=True)
    return (M_K33,)


@app.cell
def _(M_K33):
    M_K33.is_conetwork_matrix()
    return


@app.cell
def _(M_K33):
    M_K33.is_network_matrix()
    return


@app.cell
def _(M_K33):
    res_K33, cert_K33 = M_K33.is_totally_unimodular(certificate=True)
    return (cert_K33,)


@app.cell
def _(cert_K33):
    cert_K33
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 3.4 Matroids

    The packages `passagemath-graphs` and `passagemath-modules` provide facilities for matroid theory. A comprehensive catalog of known matroids is a good starting point for investigations. We can inspect the regular matroid $R_{10}$ and perform Seymour's decomposition.
    """)
    return


@app.cell
def _(matroids):
    R10 = matroids.catalog.R10()
    return (R10,)


@app.cell
def _(R10):
    sorted(R10.groundset())
    return


@app.cell
def _(A, R10):
    R10_rr = R10.representation(reduced=True, order=True)
    # Reference A from cell 4
    R10_rr, A
    return (R10_rr,)


@app.cell
def _(R10_rr):
    R10_rr._unicode_art_matrix()
    return


@app.cell
def _(R10_rr):
    R10_tu, R10_certificate = R10_rr.is_totally_unimodular(certificate=True); R10_certificate
    return (R10_certificate,)


@app.cell
def _(R10_certificate):
    R10_certificate.morphism()
    return


@app.cell
def _(R10_certificate):
    R10_certificate.morphism()._unicode_art_matrix()
    return


@app.cell
def _(R10):
    R10D = R10.dual(); R10D
    return (R10D,)


@app.cell
def _(R10D):
    R10D_rr = R10D.representation(reduced=True, order=True); R10D_rr
    return (R10D_rr,)


@app.cell
def _(R10D_rr):
    R10D_rr._unicode_art_matrix()
    return


@app.cell
def _(R10, R10D):
    R10D.is_isomorphic(R10)
    return


@app.cell
def _(R10D_rr):
    R10D_tu, R10D_certificate = R10D_rr.is_totally_unimodular(certificate=True); R10D_certificate
    return


@app.cell
def _(Matroid, R10):
    R10_1_R10 = R10.direct_sum(R10)
    R10_1_R10_reg = Matroid(R10_1_R10, regular=True)
    R10_1_R10_reg.representation()
    return (R10_1_R10_reg,)


@app.cell
def _(R10_1_R10_reg):
    R10_1_R10_rr = R10_1_R10_reg.representation(reduced=True, order=True); R10_1_R10_rr
    return (R10_1_R10_rr,)


@app.cell
def _(R10_1_R10_rr):
    R10_1_R10_tu, R10_1_R10_certificate = R10_1_R10_rr.is_totally_unimodular(certificate=True); R10_1_R10_certificate
    return (R10_1_R10_certificate,)


@app.cell
def _(R10_1_R10_certificate, unicode_art):
    unicode_art(R10_1_R10_certificate.as_ordered_tree())
    return


@app.cell
def _(R10_1_R10_rr):
    R10_1_R10_rr._unicode_art_matrix()
    return


@app.cell
def _(R10_1_R10_certificate, unicode_art):
    unicode_art(R10_1_R10_certificate.block_matrix_form())
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 3.4.1 Non-Regular Matroids (AG23minus)

    Not all matroids are regular. The `AG23minus` matroid is representable over GF(3) (ternary) but is not binary, meaning it cannot be represented by a totally unimodular matrix.
    """)
    return


@app.cell
def _(matroids):
    AG23minus = matroids.catalog.AG23minus()
    return (AG23minus,)


@app.cell
def _(AG23minus):
    AG23minus.is_regular()
    return


@app.cell
def _(AG23minus):
    AG23minus.is_binary(), AG23minus.is_ternary()
    return


@app.cell
def _(AG23minus):
    AG23minus_ternary = AG23minus.ternary_matroid()
    return (AG23minus_ternary,)


@app.cell
def _(AG23minus_ternary):
    AG23minus_rr = AG23minus_ternary.representation(reduced=True, order=True)
    return (AG23minus_rr,)


@app.cell
def _(AG23minus_rr):
    AG23minus_rr._unicode_art_matrix()
    return


@app.cell
def _(AG23minus_rr):
    AG23minus_tu, AG23minus_certificate = AG23minus_rr.is_totally_unimodular(certificate=True); AG23minus_certificate
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 3.5 Polyhedra and linear programming

    The Sage library provides a simple modeling facility for mixed-integer linear programs with access to various numerical solvers as backends, as well as facilities for convex polyhedra. In the passagemath system, this functionality is available in the pip-installable package **passagemath-polyhedra**.
    """)
    return


@app.cell
def _():
    from sage.numerical.mip import MixedIntegerLinearProgram

    return (MixedIntegerLinearProgram,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 3.5.1 Network flow

    As an illustrating example, we set up a min-cost flow problem.
    """)
    return


@app.cell
def _(graphs):
    GP = graphs.PetersenGraph(); GP
    return (GP,)


@app.cell
def _(GP):
    DP = next(GP.acyclic_orientations()); DP
    return (DP,)


@app.cell
def _(DP):
    DPA = DP.incidence_matrix(vertices=True, edges=True); DPA
    return (DPA,)


@app.cell
def _(DPA):
    DPA._unicode_art_matrix()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    To set up a feasible min-cost flow problem, we pick a flow imbalance from the range of the matrix (image of this linear map).
    """)
    return


@app.cell
def _(DPA):
    DPA.image()
    return


@app.cell
def _(DPA):
    import random
    dom = DPA.domain()
    random_flow = dom.sum(random.randint(0, 5) * dom.monomial(e) for e in dom.basis().keys())
    imbalance = DPA(random_flow); imbalance
    return (imbalance,)


@app.cell
def _(DPA, MixedIntegerLinearProgram, QQ, imbalance):
    from sage.modules.free_module_element import vector
    imbalance_vector = vector(QQ, [imbalance[v] for v in sorted(imbalance.parent().basis().keys())])
    Mincostflow = MixedIntegerLinearProgram(solver='GLPK', base_ring=QQ)
    flow = Mincostflow.new_variable(real=True, nonnegative=True, name="x"); flow
    Mincostflow.add_constraint(DPA.matrix() * flow, min=imbalance_vector, max=imbalance_vector)
    return (Mincostflow,)


@app.cell
def _(Mincostflow):
    Mincostflow.show()
    return


@app.cell
def _(Mincostflow, QQ):
    DPP = Mincostflow.polyhedron(base_ring=QQ); DPP
    return (DPP,)


@app.cell
def _(DPP):
    DPP.vertices_list()
    return


@app.cell
def _(DPP):
    DPP.rays_list()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 3.5.2 Stable sets

    For perfect graphs, the fractional stable set polyhedron (QSTAB) is equal to the stable set polyhedron (STAB), which is integral. Although QSTAB is integral for perfect graphs, the constraint matrix (clique-vertex incidence matrix) is not necessarily totally unimodular. When the matrix is non-TU, we can use the decomposition certificate to investigate the failure.
    """)
    return


@app.cell
def _(MixedIntegerLinearProgram, QQ, graphs, matrix):
    def clique_vertex_incidence_matrix(G):
        cliques = [frozenset(Q) for Q in G.cliques_maximal()]
        vertices = list(G.vertices(sort=True))
        data = [[1 if v in clique else 0 for v in vertices] for clique in cliques]
        return matrix(data, column_keys=vertices, row_keys=range(len(cliques)))

    W6 = graphs.WheelGraph(6)
    W6_clique_vertex_incidence_matrix = clique_vertex_incidence_matrix(W6)

    W6_stab_mip = MixedIntegerLinearProgram(solver='GLPK', base_ring=QQ)
    x = W6_stab_mip.new_variable(real=True, nonnegative=True, name="x")
    for v in W6.vertices():
        W6_stab_mip.set_max(x[v], 1)
    for clique in W6.cliques_maximal():
        W6_stab_mip.add_constraint(sum(x[v] for v in clique) <= 1)
    return (
        W6,
        W6_clique_vertex_incidence_matrix,
        W6_stab_mip,
        clique_vertex_incidence_matrix,
    )


@app.cell
def _(W6):
    max_cliques = [frozenset(Q) for Q in W6.cliques_maximal()]; max_cliques
    return


@app.cell
def _(W6_clique_vertex_incidence_matrix):
    W6_clique_vertex_incidence_matrix._unicode_art_matrix()
    return


@app.cell
def _(QQ, W6_stab_mip):
    W6_qstab = W6_stab_mip.polyhedron(base_ring=QQ)
    W6_qstab
    return (W6_qstab,)


@app.cell
def _(W6_qstab):
    W6_qstab.vertices_matrix()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The stable set polyhedron of $W_6$ contains fractional vertices (non-integral), because $W_6$ contains a $C_5$ cycle and is thus not perfect.
    """)
    return


@app.cell
def _(W6_clique_vertex_incidence_matrix):
    W6_clique_vertex_incidence_matrix.is_totally_unimodular()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### Interactive Wheel Graph Explorer

    You can use the slider below to dynamically adjust the size of the Wheel Graph $W_n$ and inspect the total unimodularity of its clique-vertex incidence matrix.
    """)
    return


@app.cell
def _(mo):
    n_slider = mo.ui.slider(start=3, stop=20, step=1, value=6, label="Wheel Graph size (n)")
    n_slider
    return (n_slider,)


@app.cell
def _(clique_vertex_incidence_matrix, graphs, n_slider):
    W_interactive = graphs.WheelGraph(n_slider.value)
    W_interactive_tu, W_interactive_cert = clique_vertex_incidence_matrix(W_interactive).is_totally_unimodular(certificate=True)
    return W_interactive_cert, W_interactive_tu


@app.cell
def _(W_interactive_cert, W_interactive_tu, n_slider):
    print(f"W_{n_slider.value} is totally unimodular: {W_interactive_tu}")
    if not W_interactive_tu:
        print("Violation certificate root node:", W_interactive_cert[0])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Let's check the total unimodularity of clique-vertex incidence matrices for a family of Wheel graphs $W_n$.
    """)
    return


@app.cell
def _(clique_vertex_incidence_matrix, graphs):
    [clique_vertex_incidence_matrix(graphs.WheelGraph(n)).is_totally_unimodular() for n in range(20)]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We can search for small non-unimodular graphs on 5 and 6 vertices.
    """)
    return


@app.cell
def _(clique_vertex_incidence_matrix, graphs):
    not_unimodular_on_5 = [G for G in graphs(5) 
                           if not clique_vertex_incidence_matrix(G).is_totally_unimodular()]
    not_unimodular_on_5
    return (not_unimodular_on_5,)


@app.cell
def _(not_unimodular_on_5):
    not_unimodular_on_5[0].is_cycle()
    return


@app.cell
def _(clique_vertex_incidence_matrix, graphs):
    not_unimodular_on_6 = [G for G in graphs(6) 
                           if G.is_connected() 
                           and not clique_vertex_incidence_matrix(G).is_totally_unimodular()]
    not_unimodular_on_6
    return (not_unimodular_on_6,)


@app.cell
def _(not_unimodular_on_6):
    not_unimodular_on_6[0].is_perfect()
    return


@app.cell
def _(clique_vertex_incidence_matrix, graphs):
    perfect_but_not_unimodular_on_6 = [G for G in graphs(6) 
                                       if G.is_connected() and G.is_perfect() 
                                       and not clique_vertex_incidence_matrix(G).is_totally_unimodular()]
    perfect_but_not_unimodular_on_6
    return (perfect_but_not_unimodular_on_6,)


@app.cell
def _(clique_vertex_incidence_matrix, perfect_but_not_unimodular_on_6):
    for g in perfect_but_not_unimodular_on_6: print(clique_vertex_incidence_matrix(g)._unicode_art_matrix())
    return


@app.cell
def _(clique_vertex_incidence_matrix, perfect_but_not_unimodular_on_6):
    [clique_vertex_incidence_matrix(G).is_totally_unimodular(certificate=True)[1][0].as_ordered_tree() 
     for G in perfect_but_not_unimodular_on_6]
    return


@app.cell
def _(graphs):
    len(list(graphs(9)))  # OEIS A000088
    return


@app.cell
def _(clique_vertex_incidence_matrix, graphs):
    perfect_but_not_unimodular_on_7 = [G for G in graphs(7) 
                                       if G.is_connected() and G.is_perfect() 
                                       and not clique_vertex_incidence_matrix(G).is_totally_unimodular()]
    perfect_but_not_unimodular_on_7
    return (perfect_but_not_unimodular_on_7,)


@app.cell
def _():
    from sage.matrix.seymour_decomposition import SeriesParallelReductionNode

    return (SeriesParallelReductionNode,)


@app.cell
def _(
    SeriesParallelReductionNode,
    clique_vertex_incidence_matrix,
    perfect_but_not_unimodular_on_7,
):
    def interesting_stuff():
        for G in perfect_but_not_unimodular_on_7:
            result, certificate = clique_vertex_incidence_matrix(G).is_totally_unimodular(certificate=True, stop_when_nonTU=False)
            if not isinstance(certificate[0], SeriesParallelReductionNode):
                yield G, certificate[0].as_ordered_tree() 
    for G345678, tree in interesting_stuff():
        print(clique_vertex_incidence_matrix(G345678)._unicode_art_matrix())
        print(tree)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 3.6 Detailed example for Seymour's decomposition

    We can analyze a larger matrix `MM` of size 16x16 to get one possible Seymour decomposition tree.
    """)
    return


@app.cell
def _(matrix):
    MM = matrix([[ 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [ 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [ 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, -1, 0, 0, -1, -1],
                 [ 0, -1, 0, -1, 1, 0, 0, 0, 0, 0, 1, -1, 0, 0, -1, -1],
                 [ 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [ 0, -1, 0, -1, 0, 0, 0, 1, -1, -1, 1, -1, 0, 0, -1, -1],
                 [ 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                 [ 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, -1, 1, 0, 0, 1, 1],
                 [ 0, 0, 0, 0, 0, -1, 0, -1, 1, 1, 0, 0, 0, 0, 0, 0],
                 [ 0, -1, 0, -1, 0, 0, 0, 0, 0, -1, 1, -1, 0, 0, -1, -1],
                 [ 0, 0, 0, 0, 0, -1, 0, -1, 0, 1, 0, 0, 0, 0, 0, 0],
                 [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 1, -1, 0, 0, 0],
                 [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 1, -1, 0, 0],
                 [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 1, -1, -1],
                 [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, -1, 1, 1],
                 [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]])
    return (MM,)


@app.cell
def _(MM):
    MM_result, MM_certificate = MM.is_totally_unimodular(certificate=True); MM_result, MM_certificate
    return (MM_certificate,)


@app.cell
def _(MM_certificate, unicode_art):
    unicode_art(MM_certificate.as_ordered_tree())
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The certificate `MM_certificate` is a `SeriesParallelReductionNode`. A Series-Parallel Reduction Node indicates that the input matrix arises from a smaller matrix `M'` (called the **core**) by successively adding zero/unit rows/columns, or duplicates/scalings of existing rows/columns.

    We can retrieve this core matrix using the `.core()` method, which is defined specifically for `SeriesParallelReductionNode`.
    """)
    return


@app.cell
def _(MM_certificate):
    MM1 = MM_certificate.core()
    return (MM1,)


@app.cell
def _(MM1):
    MM1.dimensions()
    return


@app.cell
def _(MM_certificate):
    core_row_keys, core_column_keys = MM_certificate.child_keys(); core_row_keys, core_column_keys
    return


@app.cell
def _(MM_certificate):
    MM_certificate.child_nodes()[0].child_nodes()
    return


if __name__ == "__main__":
    app.run()
