# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "cysignals==1.12.6",
#     "marimo",
#     "passagemath-cmr[test]==10.8.2",
#     "passagemath-flint==10.8.2",
#     "passagemath-graphs==10.8.2",
#     "passagemath-nauty==10.8.2",
#     "passagemath-polyhedra==10.8.2",
#     "passagemath-repl==10.8.2",
# ]
# ///

import marimo

__generated_with = "0.21.1"
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

    Use the "Packages" tab on the left to uv-install `passagemath-cmr[test] passagemath-polyhedra[flint] passagemath-nauty` for the functionality tested in this marimo notebook.
    """)
    return


@app.cell
def _():
    import marimo as mo
    import passagemath_polyhedra, passagemath_flint, passagemath_graphs, passagemath_nauty, passagemath_repl
    from passagemath_modules import matrix, unicode_art

    return matrix, mo, unicode_art


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 3.1 Matrices

    The pip-installable package "passagemath-cmr"
    """)
    return


@app.cell
def _(matrix):
    A = matrix([[1, 0], [-1, -1], [0, 1]]); A
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
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The package passagemath-modules also provides linear algebra facilities in a style favored in algebraic combinatorics. Users can define vector spaces and free modules with distinguished bases whose elements are indexed by arbitrary objects. Linear maps (module morphisms) between such vector spaces or modules are represented by matrices whose rows and columns are indexed by the basis indices.
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
                row_keys=range(6)); A2
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

    The package passagemath-graphs provides graph theory facilities. You can obtain the incidence matrix of an undirected graph and check whether it is totally unimodular.
    """)
    return


@app.cell
def _():
    from passagemath_graphs import Graph, graphs, digraphs

    return Graph, digraphs, graphs


@app.cell
def _(Graph):
    g = Graph([(1, 3), (3, 8), (5, 2)]); g
    return (g,)


@app.cell
def _(g):
    g.is_connected()
    return


@app.cell
def _(g):
    g.incidence_matrix(vertices=True,edges=True)._unicode_art_matrix()
    return


@app.cell
def _(g):
    A = g.incidence_matrix(vertices=True,edges=True)
    return (A,)


@app.cell
def _(A):
    _result, certificate = A.is_totally_unimodular(certificate=True)
    certificate
    return (certificate,)


@app.cell
def _(certificate):
    certificate.child_nodes()
    return


@app.cell
def _(certificate):
    certificate.child_keys()
    return


@app.cell
def _(certificate):
    C1, C2 = certificate.child_nodes()
    return C1, C2


@app.cell
def _(C1):
    C1.graph().incidence_matrix(vertices=True,edges=True)._unicode_art_matrix()
    return


@app.cell
def _(C2):
    C2.graph().incidence_matrix(vertices=True,edges=True)._unicode_art_matrix()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We can also check whether the connected undirected graph has odd cycle packing number $\mathrm{ocp}(G)\le 1$. It is done by first checking if the incidence matrix is totally unimodular. If so, it is a bipartite graph with no odd cycle. If not, we can find a basis $B$, which containing at least one odd cycle (otherwise it cannot be a basis). Then by left multiplying the inverse of the basis and checking if the obtained matrix is totally unimodular, we can claim that the graph has odd cycle packing number $\log_2(\mathopen|\det(B)\mathclose|)$ if it is totally unimodular. In the following implementation, we use rref function to compute the new matrix for efficiency.
    """)
    return


@app.cell
def _(graphs):
    gt = graphs.GrotzschGraph()
    return (gt,)


@app.cell
def _(gt):
    _result, certificate_1 = gt.incidence_matrix(vertices=True, edges=True).is_totally_unimodular(certificate=True)
    certificate_1
    return


@app.cell
def _(gt):
    At = gt.incidence_matrix(vertices=True,edges=True).matrix()
    return (At,)


@app.cell
def _(At):
    At.rref().is_totally_unimodular(certificate=True)
    return


@app.cell
def _(graphs):
    A_K6 = graphs.CompleteGraph(6).incidence_matrix()
    _result, certificate_2 = A_K6.is_totally_unimodular(certificate=True)
    certificate_2
    return (A_K6,)


@app.cell
def _(A_K6):
    A_K6.rref().is_totally_unimodular(certificate=True)
    return


@app.cell
def _(graphs):
    common_graphs = []
    map_graphs = []
    for _name in dir(graphs):
        if _name.startswith('_'):
            continue
        attr = getattr(graphs, _name)
        try:
            g_1 = attr()
            if hasattr(g_1, 'order') and hasattr(g_1, 'edges') and (len(g_1.edges()) >= len(g_1.vertices())):
                if not g_1.is_connected():
                    map_graphs.append((_name, g_1))
                elif len(g_1.vertices()) < 600:
                    common_graphs.append((_name, g_1))
        except:
            pass
    print(f'Successfully loaded {len(common_graphs)} parameter-free named graphs.')
    return common_graphs, map_graphs


@app.cell
def _(common_graphs):
    sorted([(len(g[1].vertices()), len(g[1].edges()), g[0]) for g in common_graphs])
    return


@app.cell
def _(common_graphs):
    # about 5 minute running time
    import time
    import signal
    from math import log2

    class GraphTimeoutError(Exception):
        pass

    def timeout_handler(signum, frame):
        raise GraphTimeoutError('Total time limit exceeded')
    signal.signal(signal.SIGALRM, timeout_handler)
    bipartite_graphs = []
    ocp1_graphs = []
    timed_out_graphs = []
    TIMEOUT_SECONDS = 300
    print(f"{'Graph Name':<30} | {'Time (s)':<10} | {'OCP'}")
    print('-' * 65)
    for _name, _gg in sorted(common_graphs, key=lambda x: len(x[1].vertices())):
        _start_time = time.time()
        _status = 'Processing'
        try:
            signal.alarm(TIMEOUT_SECONDS)
            AA = _gg.incidence_matrix()
            if AA.is_totally_unimodular(time_limit=TIMEOUT_SECONDS / 2):
                bipartite_graphs.append((_name, _gg))
                _status = '0'
            elif AA.rref().is_totally_unimodular(time_limit=TIMEOUT_SECONDS / 2):
                ocp1_graphs.append((_name, _gg))
                _status = '1'
            else:
                _status = '>=2'
            signal.alarm(0)
        except GraphTimeoutError:
            timed_out_graphs.append((_name, _gg))
            _status = 'TIMEOUT (>5m)'
            signal.alarm(0)
        except RuntimeError:
            timed_out_graphs.append((_name, _gg))
            _status = 'TU TIMEOUT'
            signal.alarm(0)
        _elapsed = time.time() - _start_time
        print(f'{_name:<30} | {_elapsed:<10.4f} | {_status}')
    print('-' * 65)
    print(f'Bipartite graphs found: {len(bipartite_graphs)}')
    print(f'OCP1 graphs found:      {len(ocp1_graphs)}')
    print(f'Timed out graphs:       {len(timed_out_graphs)}')
    return ocp1_graphs, time


@app.cell
def _(map_graphs):
    map_graphs
    return


@app.cell
def _(map_graphs, ocp1_graphs, time):
    for _name, _gg in sorted(map_graphs, key=lambda x: len(x[1].vertices())):
        _start_time = time.time()
        ocp_total = 0
        for gg_cc in _gg.connected_components_subgraphs():
            AA_1 = gg_cc.incidence_matrix()
            _result, certificate_3 = AA_1.is_totally_unimodular(certificate=True)
            if _result:
                continue
            elif AA_1.rref().is_totally_unimodular():
                ocp_total = ocp_total + 1
            else:
                _status = '>=2'
                break
        if _status != '>=2':
            ocp1_graphs.append((_name, _gg))
            _status = f'{ocp_total}'
        _elapsed = time.time() - _start_time
        print(f'{_name:<30} | {_elapsed:<10.4f} | {_status}')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The passagemath-cmr package also provides the recognition algorithm of network matrices. It can return the directed graph certificate of a network matrix, which can be used to reconstruct the original matrix.
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
                row_keys=range(6)); A2
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
    G = A2_certificate.graph()
    return (G,)


@app.cell
def _(G):
    M = G.incidence_matrix(vertices=True,edges=True)
    return (M,)


@app.cell
def _(M):
    M._unicode_art_matrix()
    return


@app.cell
def _(A2_certificate, G, M):
    row_keys, forest_order = zip(*A2_certificate.forest_edges().items())
    column_keys, coforest_order = zip(*A2_certificate.coforest_edges().items())
    row_order = G.vertices()[:-1]
    AA_2 = M.matrix(row_order=row_order, column_order=forest_order).inverse() * M.matrix(row_order=row_order, column_order=coforest_order)
    print(AA_2)
    return AA_2, column_keys, row_keys


@app.cell
def _(A2, AA_2, ZZ, column_keys, matrix, row_keys):
    matrix(AA_2, base_ring=ZZ, row_keys=row_keys, column_keys=column_keys) == A2
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Here are some more examples of the two excluded minors $K_5$, $K_{3,3}$ for conetwork matrices.
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
    K33_undirect = graphs.CompleteBipartiteGraph(3,3)
    K33 = K33_undirect.orient(lambda e:e if e[0] < e[1] else (e[1], e[0], e[2]))
    M_K33 = K33.incidence_matrix(vertices=True,edges=True)
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
    _result, certificate_4 = M_K33.is_totally_unimodular(certificate=True)
    certificate_4
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 3.4 Matroids
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The packages passagemath-graphs and passagemath-modules provide facilities for matroid theory. A comprehensive catalog of known matroids is a good starting point for investigations.
    """)
    return


@app.cell
def _():
    from passagemath_cmr import matroids, Matroid

    return Matroid, matroids


@app.cell
def _(matroids):
    dir(matroids.catalog)
    return


@app.cell
def _(matroids):
    R10 = matroids.catalog.R10(); R10
    return (R10,)


@app.cell
def _(R10):
    sorted(R10.groundset())
    return


@app.cell
def _(A, R10):
    R10_rr = R10.representation(reduced=True, order=True); A
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
def _(M):
    M1M = M.direct_sum(M); M1M
    return (M1M,)


@app.cell
def _(M1M, Matroid):
    Matroid(M1M, regular=True)  ### bug, fixed in 10.6.34
    return


@app.cell
def _(M):
    MD = M.dual(); MD
    return (MD,)


@app.cell
def _(MD):
    MD_rr = MD.representation(reduced=True, order=True); MD_rr
    return (MD_rr,)


@app.cell
def _(MD_rr):
    MD_rr._unicode_art_matrix()
    return


@app.cell
def _(M, MD):
    MD.is_isomorphic(M)
    return


@app.cell
def _(MD_rr):
    MD_tu, MD_certificate = MD_rr.is_totally_unimodular(certificate=True); MD_certificate
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
    return


app._unparsable_cell(
    r"""
    sage: _._unicode_art_matrix()
             (1, 'g') (0, 'c') (0, 'd') (1, 'i') (0, 'g') (1, 'j') (1, 'b') (0, 'a') (0, 'e') (1, 'h') 
    (0, 'f')⎛       0        1        1        0        0        0        0        1        0        0⎞
    (0, 'i')⎜       0        0        0        0        1        0        0        1        1        0⎟
    (1, 'e')⎜       1        0        0        1        0        1        1        0        0        1⎟
    (0, 'j')⎜       0        1        1        0       -1        0        0        0        0        0⎟
    (0, 'b')⎜       0        0       -1        0        1        0        0        0        1        0⎟
    (1, 'a')⎜       0        0        0        0        0        1        1        0        0        1⎟
    (1, 'f')⎜       1        0        0        0        0        0        1        0        0        1⎟
    (0, 'h')⎜       0        1        0        0        0        0        0        1        1        0⎟
    (1, 'c')⎜       1        0        0        1        0        0        0        0        0        1⎟
    (1, 'd')⎝       0        0        0        1        0        1        0        0        0        1⎠
    sage:                                                                                                                                                                  

    sage: M = matroids.catalog.R10()
    sage: M1M = M.direct_sum(M)
    sage: M1M_reg = Matroid(M1M, regular=True)
    sage: M1M_reg.representation(reduced=True, order=True)
    Generic morphism:
      From: Free module generated by {(0, 'd'), (0, 'g'), (1, 'i'), (0, 'a'), (1, 'j'), (1, 'h'), (0, 'f'), (1, 'e'), (0, 'i'), (1, 'b')} over Integer Ring
      To:   Free module generated by {(0, 'h'), (0, 'j'), (1, 'f'), (0, 'e'), (1, 'c'), (1, 'g'), (1, 'd'), (0, 'b'), (0, 'c'), (1, 'a')} over Integer Ring
    sage: M1M_reg.representation(reduced=True, order=True).is_totally_unimodular()
    True
    sage: M1M_reg.representation(reduced=True, order=True).is_totally_unimodular(certificate=True)
    (True, OneSumNode (10×10) with 2 children)
    sage: M1M_tu, M1M_cert = M1M_reg.representation(reduced=True, order=True).is_totally_unimodular(certificate=True)
    sage: M1M_cert.morphism()
    Generic morphism:
      From: Free module generated by {(0, 'd'), (0, 'g'), (1, 'i'), (0, 'a'), (1, 'j'), (1, 'h'), (0, 'f'), (1, 'e'), (0, 'i'), (1, 'b')} over Integer Ring
      To:   Free module generated by {(0, 'h'), (0, 'j'), (1, 'f'), (0, 'e'), (1, 'c'), (1, 'g'), (1, 'd'), (0, 'b'), (0, 'c'), (1, 'a')} over Integer Ring
    sage: M1M_cert.as_ordered_tree()
    OneSumNode (10×10) with 2 children[R10Node (5×5) a reduced matrix representation of R10 matroid[], R10Node (5×5) a reduced matrix representation of R10 matroid[]]
    sage: unicode_art(M1M_cert.as_ordered_tree())
    ╭─────────────OneSumNode (10×10) with 2 children─────────────╮
    │                                                            │
    R10Node (5×5) a reduced matrix representation of R10 matroid R10Node (5×5) a reduced matrix representation of R10 matroid
    sage: M1M_reg.representation(reduced=True, order=True)._unicode_art_matrix()
             (0, 'd') (0, 'g') (1, 'i') (0, 'a') (1, 'j') (1, 'h') (0, 'f') (1, 'e') (0, 'i') (1, 'b') 
    (0, 'h')⎛       1        1        0        1        0        0        1        0        1        0⎞
    (0, 'j')⎜       0        1        0        1        0        0        1        0        0        0⎟
    (1, 'f')⎜       0        0        1        0        1        0        0        1        0        0⎟
    (0, 'e')⎜       0        1        0        1        0        0        0        0        1        0⎟
    (1, 'c')⎜       0        0        0        0        1        0        0        1        0        1⎟
    (1, 'g')⎜       0        0        1        0        1        1        0        1        0        1⎟
    (1, 'd')⎜       0        0        1        0        1        1        0        0        0        0⎟
    (0, 'b')⎜       1        0        0        1        0        0        0        0        1        0⎟
    (0, 'c')⎜       1        0        0        1        0        0        1        0        0        0⎟
    (1, 'a')⎝       0        0        0        0        1        1        0        0        0        1⎠
    sage: unicode_art(M1M_cert.block_matrix_form())
    ⎛1 1 1 1 1│0 0 0 0 0⎞
    ⎜0 1 1 0 1│0 0 0 0 0⎟
    ⎜1 0 1 0 1│0 0 0 0 0⎟
    ⎜0 1 1 1 0│0 0 0 0 0⎟
    ⎜1 0 1 1 0│0 0 0 0 0⎟
    ⎜─────────┼─────────⎟
    ⎜0 0 0 0 0│1 1 1 0 0⎟
    ⎜0 0 0 0 0│0 1 1 0 1⎟
    ⎜0 0 0 0 0│1 1 1 1 1⎟
    ⎜0 0 0 0 0│0 1 0 1 1⎟
    ⎝0 0 0 0 0│1 1 0 1 0⎠
    """,
    name="_"
)


app._unparsable_cell(
    r"""
    sage: matroids.catalog.AG23minus()
    AG23minus: Matroid of rank 3 on 8 elements with circuit-closures
    {2: {{'a', 'b', 'c'}, {'a', 'd', 'f'}, {'a', 'e', 'g'}, {'b', 'd', 'h'}, {'b', 'e', 'f'}, {'c', 'd', 'g'}, {'c', 'e', 'h'}, {'f', 'g', 'h'}}, 3: {{'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'}}}
    sage: matroids.catalog.AG23minus().is_regular()
    False
    sage: AG23minus = matroids.catalog.AG23minus()
    sage: Matroid(AG23minus, regular=True)
    Regular matroid of rank 3 on 8 elements with 32 bases
    sage: _.is_regular()
    True
    sage: Matroid?
    sage: Matroid(AG23minus, regular=True, check=True)
    Regular matroid of rank 3 on 8 elements with 32 bases
    sage: AG23minus.is_regular()
    False
    sage: AG23minus.is_regular?
    Signature:      AG23minus.is_regular(self, algorithm=None)
    Docstring:     
    Return if \"self\" is regular.

    A regular matroid is one that can be represented by a totally
    unimodular matrix, the latter being a matrix over \mathbb{R} for which
    every square submatrix has determinant in \{0, 1, -1\}. A matroid is
    regular if and only if it is representable over every field.
    Alternatively, a matroid is regular if and only if it has no minor
    isomorphic to U_{2, 4}, F_7, or F_7^*.

    INPUT:

    * \"algorithm\" -- (default: \"None\"); specify which algorithm to check
      regularity:

      * \"None\" -- an algorithm based on excluded minors.

      * \"\"cmr\"\" -- an algorithm based on Seymour's decomposition, the
        optional package \"cmr\" is required.

    See also:

      \"M.is_regular()\" \"M.is_regular()\"
      \"M._is_binary_linear_matroid_regular()\" \"M.is_totally_unimodular()\"

    EXAMPLES:

       sage: M = matroids.catalog.Wheel4()
       sage: M.is_regular()
       True
       sage: M = matroids.catalog.R9()
       sage: M.is_regular(algorithm=\"cmr\")
       False
       sage: from sage.matroids.advanced import LinearMatroid
       sage: M1 = LinearMatroid(Matrix(ZZ,[[1,0,1,1],[0,1,1,-1]]))
       sage: M1.is_regular(algorithm=\"cmr\")
       False

    REFERENCES:

    [Oxl2011], p. 373, chapter 13.
    Init docstring: Initialize self.  See help(type(self)) for accurate signature.
    File:           ~/s/sage/sage-rebasing/local/var/lib/sage/venv-python3.10/lib/python3.10/site-packages/sage/matroids/matroid.pyx
    Type:           builtin_function_or_method
    sage: AG23minus.is_regular()
    False
    sage: AG23minus.is_regular(algorithm='cmr')
    False
    sage: AG23minus.is_binary()
    False
    sage: AG23minus.is_ternary()
    True
    sage: type(AG23minus)
    <class 'sage.matroids.circuit_closures_matroid.CircuitClosuresMatroid'>
    sage: AG23minus.is_ternary?
    Signature:      AG23minus.is_ternary(self, randomized_tests=1)
    Docstring:     
    Decide if \"self\" is a ternary matroid.

    INPUT:

    * \"randomized_tests\" -- (default: 1) an integer; the number of times a
      certain necessary condition for being ternary is tested, using
      randomization

    OUTPUT: boolean

    ALGORITHM:

    First, compare the ternary matroids local to two random bases. If
    these matroids are not  isomorphic, return \"False\". This test is
    performed \"randomized_tests\" times. Next, test if a ternary matroid
    local to some basis is isomorphic to \"self\".

    See also: \"M.ternary_matroid()\"

    EXAMPLES:

       sage: N = matroids.catalog.Fano()
       sage: N.is_ternary()
       False
       sage: N = matroids.catalog.NonFano()
       sage: N.is_ternary()
       True
    Init docstring: Initialize self.  See help(type(self)) for accurate signature.
    File:           ~/s/sage/sage-rebasing/local/var/lib/sage/venv-python3.10/lib/python3.10/site-packages/sage/matroids/matroid.pyx
    Type:           builtin_function_or_method
    sage: AG23minus.ternary_matroid()
    Ternary matroid of rank 3 on 8 elements, type 2-
    sage: AG23minus.ternary_matroid().representation(reduced=True, order=True)
    Generic morphism:
      From: Free module generated by {'c', 'd', 'e', 'f', 'g'} over Finite Field of size 3
      To:   Free module generated by {'a', 'b', 'h'} over Finite Field of size 3
    sage: AG23minus.ternary_matroid().representation(reduced=True, order=True).is_totally_unimodular()
    False
    sage: AG23minus.ternary_matroid().representation(reduced=True, order=True).is_totally_unimodular(certificate=True)
    (False, (None, ((0,), (2,))))
    sage: AG23minus.ternary_matroid().representation(reduced=True, order=True)._unicode_art_matrix()
      c d e f g 
    a⎛1 0 2 2 2⎞
    b⎜2 1 1 2 2⎟
    h⎝0 1 2 2 1⎠
    sage: 
    sage: AG23minus_rr = AG23minus.ternary_matroid().representation(reduced=True, order=True)
    """,
    name="_"
)


@app.cell
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


@app.cell
def _():
    from passagemath_cmr import QQ

    return (QQ,)


@app.cell
def _(mo):
    mo.md(r"""
    ### 3.5.1 Network flow
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    As an illustrating example, we set up a min-cost flow problem.
    """)
    return


@app.cell
def _():
    from passagemath_cmr import graphs

    return (graphs,)


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
    imbalance = DPA.image().random_element().lift(); imbalance
    return (imbalance,)


@app.cell
def _(DPA, MixedIntegerLinearProgram, QQ, imbalance):
    Mincostflow = MixedIntegerLinearProgram(solver='GLPK', base_ring=QQ)
    flow = Mincostflow.new_variable(real=True, nonnegative=True, name="x"); flow
    Mincostflow.add_constraint(DPA.matrix() * flow, min=imbalance.to_vector(), max=imbalance.to_vector())
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


@app.cell
def _(mo):
    mo.md(r"""
    ### 3.5.2 Stable sets

    QSTAB vs STAB; know integral polyhedron for perfect graphs, investigate TU-ness of constraint matrix. When non-TU, use certificate to find violating subgraphs... calls them "unimodular graphs"
    """)
    return


@app.cell
def _():
    return


@app.cell
def _(graphs):
    W6 = graphs.WheelGraph(7); W6
    return (W6,)


@app.cell
def _(W6):
    max_cliques = [frozenset(Q) for Q in W6.cliques_maximal()]; max_cliques
    return (max_cliques,)


@app.cell
def _(W6, matrix, max_cliques):
    W6_clique_vertex_incidence_matrix = matrix(entries=lambda clique, vertex: 1 if vertex in clique else 0,
                                                     row_keys=max_cliques, column_keys=W6.vertices())
    W6_clique_vertex_incidence_matrix
    return (W6_clique_vertex_incidence_matrix,)


@app.cell
def _(W6_clique_vertex_incidence_matrix):
    W6_clique_vertex_incidence_matrix._unicode_art_matrix()
    return


@app.cell
def _(MixedIntegerLinearProgram, QQ, W6_clique_vertex_incidence_matrix):
    W6_stab_mip = MixedIntegerLinearProgram(solver='GLPK', base_ring=QQ)
    W6_stab_x = W6_stab_mip.new_variable(integer=True, nonnegative=True)
    W6_stab_mip.add_constraint(W6_clique_vertex_incidence_matrix.matrix() * W6_stab_x <= 1)
    W6_stab_mip.show()
    return (W6_stab_mip,)


@app.cell
def _(QQ, W6_stab_mip):
    W6_qstab = W6_stab_mip.polyhedron(base_ring=QQ)
    W6_qstab
    return (W6_qstab,)


@app.cell
def _(W6_qstab):
    W6_qstab.vertices_matrix()
    return


@app.cell
def _(mo):
    mo.md(r"""
    It's integral!
    """)
    return


@app.cell
def _(W6_clique_vertex_incidence_matrix):
    W6_clique_vertex_incidence_matrix.is_totally_unimodular()
    return


@app.cell
def _(matrix):
    def clique_vertex_incidence_matrix(graph):
        max_cliques = [frozenset(Q) for Q in graph.cliques_maximal()]
        return matrix(entries=lambda clique, vertex: 1 if vertex in clique else 0,
                      row_keys=max_cliques, column_keys=graph.vertices())

    return (clique_vertex_incidence_matrix,)


@app.cell
def _(clique_vertex_incidence_matrix, graphs):
    [clique_vertex_incidence_matrix(graphs.WheelGraph(n)).is_totally_unimodular() for n in range(20)]
    return


@app.cell
def _(clique_vertex_incidence_matrix, graphs):
    all(clique_vertex_incidence_matrix(G).is_totally_unimodular() for G in graphs(4))
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
    for G in perfect_but_not_unimodular_on_6: print(clique_vertex_incidence_matrix(G)._unicode_art_matrix())
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


@app.cell
def _(mo):
    mo.md(r"""
    ## 3.6 Detailed example for Seymour's decomposition
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


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
