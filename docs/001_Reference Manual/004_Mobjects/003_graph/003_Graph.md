---
{
  "title": "Graph",
  "source_url": "https://docs.manim.community/en/stable/reference/manim.mobject.graph.Graph.html",
  "tree_path": [
    "Reference Manual",
    "Mobjects",
    "graph",
    "Graph"
  ],
  "scraped_at": "2026-07-10T15:59:24"
}
---

# Graph

Qualified name: `manim.mobject.graph.Graph`

class Graph(*vertices*, *edges*, *labels=False*, *label\_fill\_color=ManimColor('#000000')*, *layout='spring'*, *layout\_scale=2*, *layout\_config=None*, *vertex\_type=<class 'manim.mobject.geometry.arc.Dot'>*, *vertex\_config=None*, *vertex\_mobjects=None*, *edge\_type=<class 'manim.mobject.geometry.line.Line'>*, *partitions=None*, *root\_vertex=None*, *edge\_config=None*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/graph.html)
:   Bases: [`GenericGraph`](https://docs.manim.community/en/stable/reference/manim.mobject.graph.GenericGraph.html)

    An undirected graph (vertices connected with edges).

    The graph comes with an updater which makes the edges stick to
    the vertices when moved around. See [`DiGraph`](https://docs.manim.community/en/stable/reference/manim.mobject.graph.DiGraph.html) for
    a version with directed edges.

    See also

    [`GenericGraph`](https://docs.manim.community/en/stable/reference/manim.mobject.graph.GenericGraph.html)

    Parameters:
    :   - **vertices** (*Sequence**[**Hashable**]*) – A list of vertices. Must be hashable elements.
        - **edges** (*Sequence**[**tuple**[**Hashable**,* *Hashable**]**]*) – A list of edges, specified as tuples `(u, v)` where both `u`
          and `v` are vertices. The vertex order is irrelevant.
        - **labels** (*bool* *|* *dict*) – Controls whether or not vertices are labeled. If `False` (the default),
          the vertices are not labeled; if `True` they are labeled using their
          names (as specified in `vertices`) via [`MathTex`](https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.MathTex.html). Alternatively,
          custom labels can be specified by passing a dictionary whose keys are
          the vertices, and whose values are the corresponding vertex labels
          (rendered via, e.g., [`Text`](https://docs.manim.community/en/stable/reference/manim.mobject.text.text_mobject.Text.html) or [`Tex`](https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.Tex.html)).
        - **label\_fill\_color** (*str*) – Sets the fill color of the default labels generated when `labels`
          is set to `True`. Has no effect for other values of `labels`.
        - **layout** (*LayoutName* *|* *dict**[**Hashable**,* [*Point3DLike*](https://docs.manim.community/en/stable/reference/manim.typing.html)*]* *|* [*LayoutFunction*](https://docs.manim.community/en/stable/reference/manim.mobject.graph.LayoutFunction.html)) – Either one of `"spring"` (the default), `"circular"`, `"kamada_kawai"`,
          `"planar"`, `"random"`, `"shell"`, `"spectral"`, `"spiral"`, `"tree"`, and `"partite"`
          for automatic vertex positioning using `networkx`
          (see [their documentation](https://networkx.org/documentation/stable/reference/drawing.html)
          for more details), or a dictionary specifying a coordinate (value)
          for each vertex (key) for manual positioning.
        - **layout\_config** (*dict* *|* *None*) – Only for automatically generated layouts. A dictionary whose entries
          are passed as keyword arguments to the automatic layout algorithm
          specified via `layout` of `networkx`.
          The `tree` layout also accepts a special parameter `vertex_spacing`
          passed as a keyword argument inside the `layout_config` dictionary.
          Passing a tuple `(space_x, space_y)` as this argument overrides
          the value of `layout_scale` and ensures that vertices are arranged
          in a way such that the centers of siblings in the same layer are
          at least `space_x` units apart horizontally, and neighboring layers
          are spaced `space_y` units vertically.
        - **layout\_scale** (*float* *|* *tuple**[**float**,* *float**,* *float**]*) – The scale of automatically generated layouts: the vertices will
          be arranged such that the coordinates are located within the
          interval `[-scale, scale]`. Some layouts accept a tuple `(scale_x, scale_y)`
          causing the first coordinate to be in the interval `[-scale_x, scale_x]`,
          and the second in `[-scale_y, scale_y]`. Default: 2.
        - **vertex\_type** (*type**[*[*Mobject*](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html)*]*) – The mobject class used for displaying vertices in the scene.
        - **vertex\_config** (*dict* *|* *None*) – Either a dictionary containing keyword arguments to be passed to
          the class specified via `vertex_type`, or a dictionary whose keys
          are the vertices, and whose values are dictionaries containing keyword
          arguments for the mobject related to the corresponding vertex.
        - **vertex\_mobjects** (*dict* *|* *None*) – A dictionary whose keys are the vertices, and whose values are
          mobjects to be used as vertices. Passing vertices here overrides
          all other configuration options for a vertex.
        - **edge\_type** (*type**[*[*Mobject*](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html)*]*) – The mobject class used for displaying edges in the scene.
        - **edge\_config** (*dict* *|* *None*) – Either a dictionary containing keyword arguments to be passed
          to the class specified via `edge_type`, or a dictionary whose
          keys are the edges, and whose values are dictionaries containing
          keyword arguments for the mobject related to the corresponding edge.
        - **partitions** (*Sequence**[**Sequence**[**Hashable**]**]* *|* *None*)
        - **root\_vertex** (*Hashable* *|* *None*)

    Examples

    First, we create a small graph and demonstrate that the edges move
    together with the vertices.

    Example: MovingVertices

    [
    ](./MovingVertices-1.mp4)

    ```
    class MovingVertices(Scene):
        def construct(self):
            vertices = [1, 2, 3, 4]
            edges = [(1, 2), (2, 3), (3, 4), (1, 3), (1, 4)]
            g = Graph(vertices, edges)
            self.play(Create(g))
            self.wait()
            self.play(g[1].animate.move_to([1, 1, 0]),
                      g[2].animate.move_to([-1, 1, 0]),
                      g[3].animate.move_to([1, -1, 0]),
                      g[4].animate.move_to([-1, -1, 0]))
            self.wait()
    ```

    There are several automatic positioning algorithms to choose from:

    Example: GraphAutoPosition

    ![../_images/GraphAutoPosition-1.png](https://docs.manim.community/en/stable/_images/GraphAutoPosition-1.png)

    ```
    class GraphAutoPosition(Scene):
        def construct(self):
            vertices = [1, 2, 3, 4, 5, 6, 7, 8]
            edges = [(1, 7), (1, 8), (2, 3), (2, 4), (2, 5),
                     (2, 8), (3, 4), (6, 1), (6, 2),
                     (6, 3), (7, 2), (7, 4)]
            autolayouts = ["spring", "circular", "kamada_kawai",
                           "planar", "random", "shell",
                           "spectral", "spiral"]
            graphs = [Graph(vertices, edges, layout=lt).scale(0.5)
                      for lt in autolayouts]
            r1 = VGroup(*graphs[:3]).arrange()
            r2 = VGroup(*graphs[3:6]).arrange()
            r3 = VGroup(*graphs[6:]).arrange()
            self.add(VGroup(r1, r2, r3).arrange(direction=DOWN))
    ```

    Vertices can also be positioned manually:

    Example: GraphManualPosition

    ![../_images/GraphManualPosition-1.png](https://docs.manim.community/en/stable/_images/GraphManualPosition-1.png)

    ```
    class GraphManualPosition(Scene):
        def construct(self):
            vertices = [1, 2, 3, 4]
            edges = [(1, 2), (2, 3), (3, 4), (4, 1)]
            lt = {1: [0, 0, 0], 2: [1, 1, 0], 3: [1, -1, 0], 4: [-1, 0, 0]}
            G = Graph(vertices, edges, layout=lt)
            self.add(G)
    ```

    The vertices in graphs can be labeled, and configurations for vertices
    and edges can be modified both by default and for specific vertices and
    edges.

    Note

    In `edge_config`, edges can be passed in both directions: if
    `(u, v)` is an edge in the graph, both `(u, v)` as well
    as `(v, u)` can be used as keys in the dictionary.

    Example: LabeledModifiedGraph

    ![../_images/LabeledModifiedGraph-1.png](https://docs.manim.community/en/stable/_images/LabeledModifiedGraph-1.png)

    ```
    class LabeledModifiedGraph(Scene):
        def construct(self):
            vertices = [1, 2, 3, 4, 5, 6, 7, 8]
            edges = [(1, 7), (1, 8), (2, 3), (2, 4), (2, 5),
                     (2, 8), (3, 4), (6, 1), (6, 2),
                     (6, 3), (7, 2), (7, 4)]
            g = Graph(vertices, edges, layout="circular", layout_scale=3,
                      labels=True, vertex_config={7: {"fill_color": RED}},
                      edge_config={(1, 7): {"stroke_color": RED},
                                   (2, 7): {"stroke_color": RED},
                                   (4, 7): {"stroke_color": RED}})
            self.add(g)
    ```

    You can also lay out a partite graph on columns by specifying
    a list of the vertices on each side and choosing the partite layout.

    Note

    All vertices in your graph which are not listed in any of the partitions
    are collected in their own partition and rendered in the rightmost column.

    Example: PartiteGraph

    ![../_images/PartiteGraph-1.png](https://docs.manim.community/en/stable/_images/PartiteGraph-1.png)

    ```
    import networkx as nx

    class PartiteGraph(Scene):
        def construct(self):
            G = nx.Graph()
            G.add_nodes_from([0, 1, 2, 3])
            G.add_edges_from([(0, 2), (0,3), (1, 2)])
            graph = Graph(list(G.nodes), list(G.edges), layout="partite", partitions=[[0, 1]])
            self.play(Create(graph))
    ```

    The representation of a linear artificial neural network is facilitated
    by the use of the partite layout and defining partitions for each layer.

    Example: LinearNN

    ![../_images/LinearNN-1.png](https://docs.manim.community/en/stable/_images/LinearNN-1.png)

    ```
    class LinearNN(Scene):
        def construct(self):
            edges = []
            partitions = []
            c = 0
            layers = [2, 3, 3, 2]  # the number of neurons in each layer

            for i in layers:
                partitions.append(list(range(c + 1, c + i + 1)))
                c += i
            for i, v in enumerate(layers[1:]):
                    last = sum(layers[:i+1])
                    for j in range(v):
                        for k in range(last - layers[i], last):
                            edges.append((k + 1, j + last + 1))

            vertices = np.arange(1, sum(layers) + 1)

            graph = Graph(
                vertices,
                edges,
                layout='partite',
                partitions=partitions,
                layout_scale=3,
                vertex_config={'radius': 0.20},
            )
            self.add(graph)
    ```

    The custom tree layout can be used to show the graph
    by distance from the root vertex. You must pass the root vertex
    of the tree.

    Example: Tree

    [
    ](./Tree-1.mp4)

    ```
    import networkx as nx

    class Tree(Scene):
        def construct(self):
            G = nx.Graph()

            G.add_node("ROOT")

            for i in range(5):
                G.add_node("Child_%i" % i)
                G.add_node("Grandchild_%i" % i)
                G.add_node("Greatgrandchild_%i" % i)

                G.add_edge("ROOT", "Child_%i" % i)
                G.add_edge("Child_%i" % i, "Grandchild_%i" % i)
                G.add_edge("Grandchild_%i" % i, "Greatgrandchild_%i" % i)

            self.play(Create(
                Graph(list(G.nodes), list(G.edges), layout="tree", root_vertex="ROOT")))
    ```

    The following code sample illustrates the use of the `vertex_spacing`
    layout parameter specific to the `"tree"` layout. As mentioned
    above, setting `vertex_spacing` overrides the specified value
    for `layout_scale`, and as such it is harder to control the size
    of the mobject. However, we can adjust the captured frame and
    zoom out by using a [`MovingCameraScene`](https://docs.manim.community/en/stable/reference/manim.scene.moving_camera_scene.MovingCameraScene.html):

    Methods

    |  |  |
    | --- | --- |
    | `update_edges` |  |

    Attributes

    |  |  |
    | --- | --- |
    | `always` | Call a method on a mobject every frame. |
    | `animate` | Used to animate the application of any method of `self`. |
    | `animation_overrides` |  |
    | `color` |  |
    | `depth` | The depth of the mobject. |
    | `fill_color` | If there are multiple colors (for gradient) this returns the first one |
    | `height` | The height of the mobject. |
    | `n_points_per_curve` |  |
    | `sheen_factor` |  |
    | `stroke_color` |  |
    | `width` | The width of the mobject. |

    static \_empty\_networkx\_graph()[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/graph.html)
    :   Return an empty networkx graph for the given graph type.

        Return type:
        :   *Graph*

    \_original\_\_init\_\_(*vertices*, *edges*, *labels=False*, *label\_fill\_color=ManimColor('#000000')*, *layout='spring'*, *layout\_scale=2*, *layout\_config=None*, *vertex\_type=<class 'manim.mobject.geometry.arc.Dot'>*, *vertex\_config=None*, *vertex\_mobjects=None*, *edge\_type=<class 'manim.mobject.geometry.line.Line'>*, *partitions=None*, *root\_vertex=None*, *edge\_config=None*)
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   - **vertices** (*Sequence**[**Hashable**]*)
            - **edges** (*Sequence**[**tuple**[**Hashable**,* *Hashable**]**]*)
            - **labels** (*bool* *|* *dict*)
            - **label\_fill\_color** (*str*)
            - **layout** (*Literal**[**'circular'**,* *'kamada\_kawai'**,* *'partite'**,* *'planar'**,* *'random'**,* *'shell'**,* *'spectral'**,* *'spiral'**,* *'spring'**,* *'tree'**]* *|* *dict**[**~collections.abc.Hashable**,* *TypeAliasForwardRef**(**'~manim.typing.Point3DLike'**)**]* *|* *~manim.mobject.graph.LayoutFunction*)
            - **layout\_scale** (*float* *|* *tuple**[**float**,* *float**,* *float**]*)
            - **layout\_config** (*dict* *|* *None*)
            - **vertex\_type** (*type**[*[*Mobject*](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html)*]*)
            - **vertex\_config** (*dict* *|* *None*)
            - **vertex\_mobjects** (*dict* *|* *None*)
            - **edge\_type** (*type**[*[*Mobject*](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html)*]*)
            - **partitions** (*Sequence**[**Sequence**[**Hashable**]**]* *|* *None*)
            - **root\_vertex** (*Hashable* *|* *None*)
            - **edge\_config** (*dict* *|* *None*)

        Return type:
        :   None

    \_populate\_edge\_dict(*edges*, *edge\_type*)[[source]](https://docs.manim.community/en/stable/_modules/manim/mobject/graph.html)
    :   Helper method for populating the edges of the graph.

        Parameters:
        :   - **edges** (*list**[**tuple**[**Hashable**,* *Hashable**]**]*)
            - **edge\_type** (*type**[*[*Mobject*](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html)*]*)
