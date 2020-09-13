import h5py
import contextlib
import pygraphviz as pgv


def hdf5_handler(filename, mode="r"):
    h5py.File(filename, "a").close()
    propfaid = h5py.h5p.create(h5py.h5p.FILE_ACCESS)
    settings = list(propfaid.get_cache())
    settings[1] = 0
    settings[2] = 0
    propfaid.set_cache(*settings)
    with contextlib.closing(h5py.h5f.open(filename, fapl=propfaid)) as fid:
        f = h5py.File(fid, mode)
        return f


def draw_graphviz():
    # 创建有向图对象
    G = pgv.AGraph(directed=True, rankdir="TB")

    # 设置节点标签
    Root = "水表层级漏水情况"
    L1_1 = "416X"
    L1_2 = "405X"
    L1_3 = "404X"
    L1_4 = "403X"
    L1_5 = "402X"
    L1_6 = "401X"
    L1_7 = "419T"
    L1_8 = "418T"
    L1_9 = "417T"
    L1_10 = "413T"
    L1_11 = "412X"
    L1_12 = "411T"
    L1_13 = "406T"
    L2_1 = "41601X"
    L2_2 = "40511X"
    L2_3 = "40509T"
    L2_4 = "40508T"
    L2_5 = "40507T"
    L2_6 = "40506T"
    L2_7 = "40504T"
    L2_8 = "40503T"
    L2_9 = "40502T"
    L2_10 = "40501T"
    L2_11 = "40405T"
    L2_12 = "40404T"
    L2_13 = "40403T"
    L2_14 = "40402T"
    L2_15 = "40401T"
    L2_16 = "40338T"
    L2_17 = "40337X"
    L2_18 = "40336T"
    L2_19 = "40335X"
    L2_20 = "40334T"
    L2_21 = "40333T"
    L2_22 = "40331T"
    L2_23 = "40325T"
    L2_24 = "40321T"
    L2_25 = "40318T"
    L2_26 = "40316T"
    L2_27 = "40315T"
    L2_28 = "40313T"
    L2_29 = "40219T"
    L2_30 = "40218T"
    L2_31 = "40217T"
    L2_32 = "40215T"
    L2_33 = "40214T"
    L2_34 = "40213T"
    L2_35 = "40136T"
    L2_36 = "40135X"
    L2_37 = "40134X"
    L2_38 = "40133X"
    L2_39 = "40126T"
    L2_40 = "40124T"
    L2_41 = "40123T"
    L2_42 = "40122T"
    L2_43 = "40121T"
    L2_44 = "40120T"
    L2_45 = "40119T"
    L2_46 = "40118T"
    L2_47 = "40117T"
    L2_48 = "40116T"
    L2_49 = "40115T"
    L2_50 = "40106T"
    L2_51 = "40105T"
    L3_1 = "4160101T"
    L3_2 = "4051101T"
    L3_3 = "4040501T"
    L3_4 = "4033726T"
    L3_5 = "4033725T"
    L3_6 = "4033723T"
    L3_7 = "4033720T"
    L3_8 = "4033506T"
    L3_9 = "4033503T"
    L3_10 = "4033502T"
    L3_11 = "4033501T"
    L3_12 = "4013502T"
    L3_13 = "4013501T"
    L3_14 = "4013407X"
    L3_15 = "4013406T"
    L3_16 = "4013404T"
    L3_17 = "4013403T"
    L3_18 = "4013402T"
    L3_19 = "4013401T"
    L3_20 = "4013308T"
    L3_21 = "4013307T"
    L3_22 = "4013305T"
    L3_23 = "4013304T"
    L3_24 = "4013303T"
    L3_25 = "4010401T"
    L4_1 = "403350301T"
    L4_2 = "403350202T"
    L4_3 = "403350201T"
    L4_4 = "403350101T"

    # 添加节点
    G.add_node(Root, style="filled", shape="box3d", color="#d6c8ff")

    for L1 in [eval(_) for _ in dir() if _.startswith("L1")]:
        G.add_node(L1, style="filled", shape="ellipse", color="#95e1d3")

    for L2 in [eval(_) for _ in dir() if _.startswith("L2")]:
        G.add_node(L2, style="filled", shape="ellipse", color="#eaffd0")

    for L3 in [eval(_) for _ in dir() if _.startswith("L3")]:
        G.add_node(L3, style="filled", shape="ellipse", color="#fce38a")

    for L4 in [eval(_) for _ in dir() if _.startswith("L4")]:
        G.add_node(L4, style="filled", shape="ellipse", color="#f38181")

    # 添加边
    G.add_edges_from([[Root, L1_1], [Root, L1_2], [Root, L1_3], [Root, L1_4],
                      [Root, L1_5], [Root, L1_6], [Root, L1_7], [Root, L1_8],
                      [Root, L1_9], [Root, L1_10], [Root, L1_11], [Root, L1_12], [Root, L1_13]],
                     color="#ffc93c", style="dashed", penwidth=1.5)

    G.add_edges_from([[L1_1, L2_1], [L1_2, L2_2], [L1_2, L2_3], [L1_2, L2_4],
                      [L1_2, L2_5], [L1_2, L2_6], [L1_2, L2_7], [L1_2, L2_8],
                      [L1_2, L2_9], [L1_2, L2_10], [L1_3, L2_11], [L1_3, L2_12],
                      [L1_3, L2_13], [L1_3, L2_14], [L1_3, L2_15], [L1_4, L2_16],
                      [L1_4, L2_17], [L1_4, L2_18], [L1_4, L2_19], [L1_4, L2_20],
                      [L1_4, L2_21], [L1_4, L2_22], [L1_4, L2_23], [L1_4, L2_24],
                      [L1_4, L2_25], [L1_4, L2_26], [L1_4, L2_27], [L1_4, L2_28],
                      [L1_5, L2_29], [L1_5, L2_30], [L1_5, L2_31], [L1_5, L2_32],
                      [L1_5, L2_33], [L1_5, L2_34], [L1_6, L2_35], [L1_6, L2_36],
                      [L1_6, L2_37], [L1_6, L2_38], [L1_6, L2_39], [L1_6, L2_40],
                      [L1_6, L2_41], [L1_6, L2_42], [L1_6, L2_43], [L1_6, L2_44],
                      [L1_6, L2_45], [L1_6, L2_46], [L1_6, L2_47], [L1_6, L2_48],
                      [L1_6, L2_49], [L1_6, L2_50], [L1_6, L2_51]],
                     color="#ff9a3c", style="dashed", penwidth=1.5)

    G.add_edges_from([[L2_1, L3_1], [L2_2, L3_2], [L2_11, L3_3], [L2_17, L3_4],
                      [L2_17, L3_5], [L2_17, L3_6], [L2_17, L3_7], [L2_19, L3_8],
                      [L2_19, L3_9], [L2_19, L3_10], [L2_19, L3_11], [L2_36, L3_12],
                      [L2_36, L3_13], [L2_37, L3_14], [L2_37, L3_15], [L2_37, L3_16],
                      [L2_37, L3_17], [L2_37, L3_18], [L2_37, L3_19], [L2_38, L3_20],
                      [L2_38, L3_21], [L2_38, L3_22], [L2_38, L3_23], [L2_38, L3_24],
                      [L2_51, L3_25]],
                     color="#ff6f3c", style="dashed", penwidth=1.5)

    G.add_edges_from([[L3_9, L4_1], [L3_10, L4_2], [L3_10, L4_3], [L3_11, L4_4]],
                     color="#155263", style="dashed", penwidth=1.5)

    # 导出图形
    G.layout()
    G.draw("水表层级漏水情况.png", prog="dot")
