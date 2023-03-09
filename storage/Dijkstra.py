import matplotlib.pyplot as plt
import random

def show(map, grid, state):
    size = -19
    fig = plt.figure(figsize=(5, 5))
    
    plt.plot([-0.5, -0.5], [0.5, size+0.5], color='k')
    plt.plot([-0.5, -size-0.5], [size+0.5, size+0.5], color='k')
    plt.plot([-size-0.5, -0.5], [0.5, 0.5], color='k')
    plt.plot([-size-0.5, -size-0.5], [size+0.5, 0.5], color='k')
    
    
    import matplotlib.cm as cm
    import matplotlib.colors as colors
    
    cmap = cm.binary
    cmap_data = cmap(np.arange(cmap.N))
    cmap_data[0, 3] = 0 # 0 のときのα値を0(透明)にする
    customized_gray = colors.ListedColormap(cmap_data)

    dem = [[0.0 for i in range(-size)] for i in range(-size)] #known or unknown
    x, y = np.mgrid[-0.5:-size+0.5:1, -0.5:-size:1]
    # x, y = np.mgrid[-0.5:-size-0.5:1, 0.5:-size+0.5:1]

    demGrid = plt.pcolor(x, -y, dem, vmax=1, cmap=plt.cm.BrBG, alpha=0.2)
    
    soil = [[0.0 for i in range(-size)] for i in range(-size)] #2Dgridmap(xw, yw)
    
    "Add test-LBM"
    Node = ["A", "B", "C", "D", "O", "E", "F", "G",     "g", "s"]
    test = [[0.0 for i in range(-size)] for i in range(-size)] #2Dgridmap(xw, yw) # Node
    test = [[1.0 for i in range(-size)] for i in range(-size)] #2Dgridmap(xw, yw) # Node # here

    
    for ix in range(-size):
        for iy in range(-size):   
            if grid[ix][iy] == 2: # 9:
                soil[ix][iy] = 1 #sandy terrain
            else:
                soil[ix][iy] = 0 #hard ground
                "Add test-LBM"

    print("====== end ======")

    "Add"
    test = np.flip(test, 1)
    test = np.rot90(test, k=1)
    # lm = plt.pcolor(x, -y, test, vmax=1, cmap=plt.cm.Greens, alpha = 1.0) # マス目が消える
    lm = plt.pcolor(x, -y, test, vmax=1, cmap=plt.cm.BrBG, alpha = 1.0)
    # lm = plt.pcolor(x, -y, test, vmax=1, cmap=plt.cm.RdGy, alpha = 1.0) # here
    
    soil = np.flip(soil, 1)
    soil = np.rot90(soil, k=1)
    # terrain = plt.pcolor(x, -y, soil, vmax=1, cmap=plt.cm.Greys, alpha = 0.2)
    terrain = plt.pcolor(x, -y, soil, vmax=1, cmap=plt.cm.Greys, alpha = 0.5)
    # terrain = plt.pcolor(x, -y, soil, vmax=1, cmap=plt.cm.BuPu, alpha = 0.5) # here

    map  = np.flip(map, 1)
    map = np.rot90(map, k=1)
    known = plt.pcolor(x, -y, map, vmax=1, cmap=customized_gray)


    "----------"
    # Node = ["A", "B", "C", "D", "O", "E", "F", "G",     "g", "s"]
    # # if self.env.grid[state.row][state.column] in Node:
    # # self.to_arrows(A, V)
    # "----------"
    
    # # plt.plot(state.column, -state.row, ".y", markersize=10)
    # if self.env.NODELIST[state.row][state.column] in Node:
    #     # plt.plot(state.column, -state.row, ".r", markersize=10)
    #     plt.plot(state.column, -state.row, ".r", markersize=10)
    # elif self.env.NODELIST[state.row][state.column] == "x":
    #     plt.plot(state.column, -state.row, "xb", markersize=5) # 10) # , alpha = 0.5)
    # else:
    plt.plot(state[1], -state[0], ".y", markersize=10)

    
    tx = 8
    ty = -18
    plt.plot(tx, ty, "*g", markersize=4+2)

    # goal_x = (8)
    # goal_y = (0.3)
    # "----- 2d -----"
    goal_x = 18
    goal_y = 0.3
    plt.plot(goal_x, goal_y, "*r", markersize=4+2)


    # png_path = os.path.join(result_dir, "{0}.png".format(ww))
    # plt.savefig(png_path)
    
    # plt.show()

def obserb(init, size, map):

    NODELIST = [
        ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
        ["x", "", "x", "", "x", "", "x", "", "x", "", "x", "", "x", "", "x", "", "x", "", "x"],
        ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
        ["x", "", "x", "", "x", "", "x", "", "x", "", "x", "", "x", "", "x", "", "x", "", "x"],
        ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
        ["x", "", "x", "", "x", "", "x", "", "x", "", "x", "", "x", "", "x", "", "x", "", "x"],
        ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
    ]
        
    init_x, init_y = init[0], init[1]

    # Node = ["A", "B", "C", "D", "O", "E", "F", "G",     "g",     "x"]
    Node = ["A", "B", "C", "D", "O", "E", "F", "G",     "g",     "x",          "s"] # "s"を追加

    if NODELIST[init_x][init_y] in Node: #交差点のみ前後一マス観測
        for i in range(-1,2):
            if init_x+i < 0 or init_x+i >=size:
            # if init_x+i >= 0 or init_x+i <size:
                continue
            for j in range(-1,2):
            
                if init_y+j < 0 or init_y+j >=size:
                # if init_y+j >= 0 or init_y+j <size:
                    continue
                
                map[init_x+i][init_y+j] = 0
    map[init_x][init_y] = 0 # 現在のマスのみ観測
            
    return map

import numpy as np
import time
 
# 1: フリーのセル
# 2: 障害物
# 3: 探索済
# 4: 探索リスト
# 5: スタート
# 6: ゴール
# 0: 解の経路




result = []
little = []
over = []
goal_count = 0

# goal_check = 0
retry_num = []
goal_y_n = []




for epoch in range(100):
 
    # 10x10のフィールドを作成
    map = np.ones(100).reshape(10,10)
    # 障害物を生成
    map[0,7] = map[1,7] = map[2,7] = map[3,7] = map[4,7] = map[5,7] = 2
    map[5,4] = map[6,4] = map[7,4] = 2




    map = [
        # [1, 2, 1, 2, 1, 2, 1, 2, 6, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1],
        # [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1],
        # [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1],
        # [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1],
        # [1, 1, 1, 1, 1, 1, 1, 2, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        # [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1],
        # [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1],
        # [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1],
        # [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1],
        # [1, 1, 1, 1, 1, 1, 1, 2, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        # [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1],
        # [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1],
        # [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1],
        # [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1],
        # [1, 1, 1, 1, 1, 1, 1, 2, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        # [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1],
        # [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1],
        # [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1],
        # [1, 2, 1, 2, 1, 2, 1, 2, 5, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1],

        [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1],
        [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1],
        [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1],
        [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1],
        [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1],
        [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1],
        [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1],
        [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1],
        [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1],
        [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1],
        [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1],
        [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1],
        [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1],
    ]

    map = np.array(map)




    "----- Add -----"
    size = 19
    map_test = [[0.0 for i in range(size)] for i in range(size)] #known or unknown
    for ix in range(size):
        for iy in range(size):
            map_test[ix][iy] = 1
            # # soil[ix][iy] = 1 #sandy terrain
            # if dem[ix][iy] <= 0.2:
            #     soil[ix][iy] = 1 #sandy terrain
            # else:
            #     soil[ix][iy] = 0 #hard ground


            # map[ix][iy] = 0 # 全マス観測している場合


    import math
    # goal = (4, 14) # Virtual Goal # here
    # start = (self.state.row, self.state.column) # here
    # dist = math.sqrt((self.goal[0]-self.start[0])**2+(self.goal[1]-self.start[1])**2)
    # D_NUM = dist
    VIZD = []
    STATE_HISTORY = []
    goal_check = 0
    "----- Add -----"





    # スタート、ゴール座標
    # start_coords = np.array([5, 1])
    start_coords = np.array([18, 8])
    # dest_coords = np.array([7,8])
    # dest_coords = np.array([0, 18])
    dest_coords = np.array([4, 14])

    map[start_coords[0],start_coords[1]] = 5
    map[dest_coords[0],dest_coords[1]] = 6
    # 行数、列数
    nrows = map.shape[0]
    ncols = map.shape[1]

    # nrows = len(map) # 19
    # ncols = len(map[0]) # 19



    # 線形インデックス
    start_node = ncols * (start_coords[0]) + start_coords[1]
    dest_node = ncols * (dest_coords[0]) + dest_coords[1]
    # 各セルのスタート座標からの距離　とりあえず100に設定
    distanceFromStart = np.ones(nrows * ncols).reshape(nrows,ncols)*100
    # スタート地点は距離0
    distanceFromStart[start_coords[0],start_coords[1]] = 0
    # 探索用　親セル
    parent = np.zeros(nrows*ncols).reshape(nrows,ncols)
    
    while True:

        
        map[start_coords[0],start_coords[1]] = 5
        map[dest_coords[0],dest_coords[1]] = 6
        # スタート座標から最短距離のセルを探す（最初はスタート座標）
        # 線形インデックスが得られる
        min_dist = np.min(distanceFromStart)
        current = np.argmin(distanceFromStart)
        # ゴールに達したら抜ける
        if current == dest_node or min_dist == 100:
            break
        # 通常の座標に変換
        i = int(current // ncols)
        j = int(current - (current // ncols) * ncols)
        # 探索済とする
        map[i, j] = 3

        "----- Add -----"
        init = [i, j]
        map_test = obserb(init, size, map_test)

        "----- Add -----"
        start = (init[0], init[1]) # here
        dist = math.sqrt((dest_coords[0]-start[0])**2+(dest_coords[1]-start[1])**2)
        D_NUM = dist
        VIZD.append(D_NUM)
        STATE_HISTORY.append(init)
        "----- Add -----"
        "----- Add -----"
        rand = random.randint(0, 10)
        # print("観測の不確実性 prob : {}".format(rand))
        if rand >= 0: # > 1:
            # 次回の探索から外す
            distanceFromStart[i][j] = 100
        
        
            # rand = random.randint(0, 10)
            # # print("観測の不確実性 prob : {}".format(rand))
            # if rand > 1:
            # カレントセルの上下左右を調べる
            for ii in range(1,5):
                if ii == 1:
                    if i > 0:
                        neighbor_node_r = i - 1
                        neighbor_node_c = j
                elif ii == 2:
                    if i < nrows - 1:
                        neighbor_node_r = i + 1
                        neighbor_node_c = j
                elif ii == 3:
                    if j > 0:
                        neighbor_node_r = i
                        neighbor_node_c = j - 1
                elif ii == 4:
                    if j < ncols - 1:
                        neighbor_node_r = i
                        neighbor_node_c = j + 1
                # 探索済/障害物/ゴールかどうか
                if map[neighbor_node_r,neighbor_node_c] != 3 and\
                    map[neighbor_node_r,neighbor_node_c] != 2 and\
                    map[neighbor_node_r,neighbor_node_c] != 5:
                    # 距離をプラス１
                    dist = min_dist + 1
                    # 最短なら更新
                    if dist < distanceFromStart[neighbor_node_r,neighbor_node_c]:
                        distanceFromStart[neighbor_node_r,neighbor_node_c] = dist
                        parent[neighbor_node_r,neighbor_node_c] = current
                        map[neighbor_node_r,neighbor_node_c] = 4
                # print('distance')
                # print(distanceFromStart)
                # print('status')
                # print(map)
                # # time.sleep(0.3)
                # print('')

                if map[neighbor_node_r,neighbor_node_c] != 5:
                    goal_check = 1
                    goal_count += 1



        # show(map_test, map, init)
    # 最短経路を表示する
    # ゴールの線形インデックス座標
    print('found shortest path!')
    # route = np.array([dest_coords[0] * ncols + dest_coords[1] - 1])
    route = np.array([dest_coords[0] * ncols + dest_coords[1]])




    VIZD.append(0) # Goal
    STATE_HISTORY.append(init)


    # # 普通の座標に変換
    # route_r = int(route[0] // ncols)
    # route_c = int(route[0] - (route[0] // ncols) * ncols)
    # # スタート地点まで
    # while parent[route_r,route_c] != 0:
    #     # 親座標まで１コマ戻る
    #     route = np.append(parent[route_r,route_c],route)
    #     # 0で表示
    #     map[route_r,route_c] = 0
    #     # 座標を更新
    #     route_r = int(route[0] // ncols)
    #     route_c = int(route[0] - (route[0] // ncols) * ncols)
    #     print(map)
    #     print('')
    #     time.sleep(0.5)
    "======== データの出力 ========"
    import pandas as pd
    # df = pd.Series(data=STATE_HISTORY)
    # df = df[df != df.shift(1)]
    # print('-----削除後データ----')
    # print("Steps:{}".format((len(df))))
    # result.append((len(df)))
    
    print('-----削除後データ----')
    print("Steps:{}".format((len(STATE_HISTORY))))
    result.append((len(STATE_HISTORY)))
    # if len(df) <= 45+10: # 100:
    #     little.append(len(df))

    # if len(df) >= 100: # 0:
    #     over.append(len(df))

    goal_y_n.append(goal_check)
    # retry_num.append(x) # +1)

print("steps =", result)
print("goal_y_n =", goal_y_n)
# print("retry_num =", retry_num)
print("最小:{}".format(min(result)))
print("最大:{}".format(max(result)))
print("45+10 以内 : {}".format(len(little)))
print("100以上 : {}".format(len(over)))

print("----------")
print("試行回数 {}".format(epoch+1))
print("goal到達回数 : {}".format(goal_count))
print("到達率 : {}".format(goal_count/(epoch+1)))
print("----------")


print("goal distance = ", VIZD)
# print("len goal distance = ", len(VIZD))
# import pandas as pd
viz = pd.DataFrame({ # "Number of Landmarks found":VIZL,
                    "Distance to goal":VIZD,
                    })
try:
    print(viz)
    # map_viz_init.viz(viz)
    viz.plot.line(subplots=True, layout=(2, 1), grid=True, figsize=(5, 5)) # , style=['-', '--', '-.', ':'])
    # viz.plot.line(layout=(2, 1), grid=True, figsize=(5, 5))
    import matplotlib.pyplot as plt
    plt.show()
except:
    print("viz エラー")