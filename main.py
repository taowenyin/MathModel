import pandas as pd
import numpy as np
import math
import utils as utils
import pygraphviz as pgv


if __name__ == '__main__':
    dataset_h5 = utils.hdf5_handler(bytes("./dataset/dataset.hdf5", encoding="utf8"), 'a')
    level_1_water_mater_list = np.array(dataset_h5['water_meter'])

    for level_1_water_mater in level_1_water_mater_list:
        # 获取Level-1水表子信息
        level_1_water_mater_attrs = np.array(dataset_h5['water_meter'][level_1_water_mater])

        level_1_quarter_data_1 = None
        level_1_quarter_data_2 = None
        level_1_quarter_data_3 = None
        level_1_quarter_data_4 = None
        level_1_quarter_data_all = None
        level_1_water_mater_name = None
        # 当水表有信息时才读取数据
        if 'quarter_data' in level_1_water_mater_attrs:
            # 获取Level-1水表信息
            level_1_water_mater_name = dataset_h5['water_meter'][level_1_water_mater].attrs['水表名']
            level_1_quarter_data_1 = np.sum(np.array(dataset_h5['water_meter'][level_1_water_mater]['quarter_data-1'])[:, -1])
            level_1_quarter_data_2 = np.sum(np.array(dataset_h5['water_meter'][level_1_water_mater]['quarter_data-2'])[:, -1])
            level_1_quarter_data_3 = np.sum(np.array(dataset_h5['water_meter'][level_1_water_mater]['quarter_data-3'])[:, -1])
            level_1_quarter_data_4 = np.sum(np.array(dataset_h5['water_meter'][level_1_water_mater]['quarter_data-4'])[:, -1])

            level_1_quarter_data_all = level_1_quarter_data_1 + level_1_quarter_data_2 + \
                                       level_1_quarter_data_3 + level_1_quarter_data_4

        has_water_mater_info = 'quarter_data' in level_1_water_mater_attrs and len(level_1_water_mater_attrs) > 5
        has_sub_water_mater = 'quarter_data' not in level_1_water_mater_attrs and len(level_1_water_mater_attrs) > 0
        # 判断是否有子表数据
        if has_water_mater_info or has_sub_water_mater:
            # 如果包含数据，那剔除
            if has_water_mater_info:
                level_1_water_mater_attrs = level_1_water_mater_attrs[0:-5]

            # 二级水表用水量总和
            level_2_quarter_data_1_sum = 0
            level_2_quarter_data_2_sum = 0
            level_2_quarter_data_3_sum = 0
            level_2_quarter_data_4_sum = 0
            # 读取子表信息
            for level_2_water_mater in level_1_water_mater_attrs:
                level_2_water_mater_name = dataset_h5['water_meter'][level_1_water_mater][
                    level_2_water_mater].attrs['水表名']

                level_2_quarter_data_1 = np.sum(np.array(dataset_h5['water_meter'][level_1_water_mater]
                                                         [level_2_water_mater]['quarter_data-1'])[:, -1])
                level_2_quarter_data_2 = np.sum(np.array(dataset_h5['water_meter'][level_1_water_mater]
                                                         [level_2_water_mater]['quarter_data-2'])[:, -1])
                level_2_quarter_data_3 = np.sum(np.array(dataset_h5['water_meter'][level_1_water_mater]
                                                         [level_2_water_mater]['quarter_data-3'])[:, -1])
                level_2_quarter_data_4 = np.sum(np.array(dataset_h5['water_meter'][level_1_water_mater]
                                                         [level_2_water_mater]['quarter_data-4'])[:, -1])

                # 计算各季度各水表用水合
                level_2_quarter_data_1_sum += level_2_quarter_data_1
                level_2_quarter_data_2_sum += level_2_quarter_data_2
                level_2_quarter_data_3_sum += level_2_quarter_data_3
                level_2_quarter_data_4_sum += level_2_quarter_data_4

                level_2_quarter_data_item_all = level_2_quarter_data_1 + level_2_quarter_data_2 + \
                                                level_2_quarter_data_3 + level_2_quarter_data_4

                # 获取Level-2水表子信息
                level_2_water_mater_attrs = np.array(dataset_h5['water_meter'][level_1_water_mater][level_2_water_mater])
                # 三级水表用水量总和
                level_3_quarter_data_1_sum = 0
                level_3_quarter_data_2_sum = 0
                level_3_quarter_data_3_sum = 0
                level_3_quarter_data_4_sum = 0
                for level_3_water_mater in level_2_water_mater_attrs[0:-5]:
                    level_3_water_mater_name = dataset_h5['water_meter'][level_1_water_mater][
                        level_2_water_mater][level_3_water_mater].attrs['水表名']

                    level_3_quarter_data_1 = np.sum(np.array(dataset_h5['water_meter'][level_1_water_mater]
                                                             [level_2_water_mater][level_3_water_mater]['quarter_data-1'])[:, -1])
                    level_3_quarter_data_2 = np.sum(np.array(dataset_h5['water_meter'][level_1_water_mater]
                                                             [level_2_water_mater][level_3_water_mater]['quarter_data-2'])[:, -1])
                    level_3_quarter_data_3 = np.sum(np.array(dataset_h5['water_meter'][level_1_water_mater]
                                                             [level_2_water_mater][level_3_water_mater]['quarter_data-3'])[:, -1])
                    level_3_quarter_data_4 = np.sum(np.array(dataset_h5['water_meter'][level_1_water_mater]
                                                             [level_2_water_mater][level_3_water_mater]['quarter_data-4'])[:, -1])

                    # 计算各季度各水表用水合
                    level_3_quarter_data_1_sum += level_3_quarter_data_1
                    level_3_quarter_data_2_sum += level_3_quarter_data_2
                    level_3_quarter_data_3_sum += level_3_quarter_data_3
                    level_3_quarter_data_4_sum += level_3_quarter_data_4

                    level_3_quarter_data_item_all = level_3_quarter_data_1 + level_3_quarter_data_2 + \
                                                    level_3_quarter_data_3 + level_3_quarter_data_4

                    # 获取Level-2水表子信息
                    level_3_water_mater_attrs = np.array(dataset_h5['water_meter'][level_1_water_mater][
                                                             level_2_water_mater][level_3_water_mater])
                    # 三级水表用水量总和
                    level_4_quarter_data_1_sum = 0
                    level_4_quarter_data_2_sum = 0
                    level_4_quarter_data_3_sum = 0
                    level_4_quarter_data_4_sum = 0
                    for level_4_water_mater in level_3_water_mater_attrs[0:-5]:
                        level_4_water_mater_name = dataset_h5['water_meter'][level_1_water_mater][
                            level_2_water_mater][level_3_water_mater][level_4_water_mater].attrs['水表名']

                        level_4_quarter_data_1 = np.array(dataset_h5['water_meter'][level_1_water_mater]
                                                          [level_2_water_mater][level_3_water_mater]
                                                          [level_4_water_mater]['quarter_data-1'])[:, -1]
                        level_4_quarter_data_2 = np.array(dataset_h5['water_meter'][level_1_water_mater]
                                                          [level_2_water_mater][level_3_water_mater]
                                                          [level_4_water_mater]['quarter_data-2'])[:, -1]
                        level_4_quarter_data_3 = np.array(dataset_h5['water_meter'][level_1_water_mater]
                                                          [level_2_water_mater][level_3_water_mater]
                                                          [level_4_water_mater]['quarter_data-3'])[:, -1]
                        level_4_quarter_data_4 = np.array(dataset_h5['water_meter'][level_1_water_mater]
                                                          [level_2_water_mater][level_3_water_mater]
                                                          [level_4_water_mater]['quarter_data-4'])[:, -1]

                        # 计算各季度各水表用水合
                        level_4_quarter_data_1_sum += np.sum(level_4_quarter_data_1)
                        level_4_quarter_data_2_sum += np.sum(level_4_quarter_data_2)
                        level_4_quarter_data_3_sum += np.sum(level_4_quarter_data_3)
                        level_4_quarter_data_4_sum += np.sum(level_4_quarter_data_4)

                    if len(level_3_water_mater_attrs) > 5:
                        level_4_quarter_data_all = level_4_quarter_data_1_sum + level_4_quarter_data_2_sum + \
                                                   level_4_quarter_data_3_sum + level_4_quarter_data_4_sum
                        print('({})L3-L4: Q1-Diff={:.4f}, Q2-Diff={:.4f}, Q3-Diff={:.4f}, Q4-Diff={:.4f}, ALL-Diff={:.4f}'.format(
                            level_3_water_mater_name,
                            (level_3_quarter_data_1 - level_4_quarter_data_1_sum) / level_3_quarter_data_1,
                            (level_3_quarter_data_2 - level_4_quarter_data_2_sum) / level_3_quarter_data_2,
                            (level_3_quarter_data_3 - level_4_quarter_data_3_sum) / level_3_quarter_data_3,
                            (level_3_quarter_data_4 - level_4_quarter_data_4_sum) / level_3_quarter_data_4,
                            (level_3_quarter_data_item_all - level_4_quarter_data_all) / level_3_quarter_data_item_all))

                if len(level_2_water_mater_attrs) > 5:
                    level_3_quarter_data_all = level_3_quarter_data_1_sum + level_3_quarter_data_2_sum + \
                                               level_3_quarter_data_3_sum + level_3_quarter_data_4_sum
                    print('({})L2-L3: Q1-Diff={:.4f}, Q2-Diff={:.4f}, Q3-Diff={:.4f}, Q4-Diff={:.4f}, ALL-Diff={:.4f}'.format(
                        level_2_water_mater_name,
                        (level_2_quarter_data_1 - level_3_quarter_data_1_sum) / level_2_quarter_data_1,
                        (level_2_quarter_data_2 - level_3_quarter_data_2_sum) / level_2_quarter_data_2,
                        (level_2_quarter_data_3 - level_3_quarter_data_3_sum) / level_2_quarter_data_3,
                        (level_2_quarter_data_4 - level_3_quarter_data_4_sum) / level_2_quarter_data_4,
                        (level_2_quarter_data_item_all - level_3_quarter_data_all) / level_2_quarter_data_item_all))

            if level_1_water_mater_name is not None:
                level_2_quarter_data_all = level_2_quarter_data_1_sum + level_2_quarter_data_2_sum + \
                                           level_2_quarter_data_3_sum + level_2_quarter_data_4_sum
                print('({})L1-L2: Q1-Diff={:.4f}, Q2-Diff={:.4f}, Q3-Diff={:.4f}, Q4-Diff={:.4f}, ALL-Diff={:.4f}'.format(
                    level_1_water_mater_name,
                    (level_1_quarter_data_1 - level_2_quarter_data_1_sum) / level_1_quarter_data_1,
                    (level_1_quarter_data_2 - level_2_quarter_data_2_sum) / level_1_quarter_data_2,
                    (level_1_quarter_data_3 - level_2_quarter_data_3_sum) / level_1_quarter_data_3,
                    (level_1_quarter_data_4 - level_2_quarter_data_4_sum) / level_1_quarter_data_4,
                    (level_1_quarter_data_all - level_2_quarter_data_all) / level_1_quarter_data_all))
            # else:
            #     print('({0})L1-L2: Q1-Diff={1}, Q2-Diff={2}, Q3-Diff={3}, Q4-Diff={4}'.format(
            #         level_1_water_mater,
            #         level_2_quarter_data_1_sum, level_2_quarter_data_2_sum,
            #         level_2_quarter_data_3_sum, level_2_quarter_data_4_sum))

    # print(dataset)
    # no = dataset_h5['water_meter']['403X'].attrs['水表号']
    # print(np.array(dataset_h5['water_meter']['403X']['40337X']))
