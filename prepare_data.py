import pandas as pd
import numpy as np
import math
import utils as utils


if __name__ == "__main__":
    dataset_h5 = utils.hdf5_handler(bytes("./dataset/dataset.hdf5", encoding="utf8"), 'a')
    storage = dataset_h5.require_group("water_meter")
    dataset = pd.read_excel('./dataset/附件_水表层级.xlsx')
    dataset_1 = pd.read_excel('./dataset/附件_一季度.xlsx')
    dataset_2 = pd.read_excel('./dataset/附件_二季度.xlsx')
    dataset_3 = pd.read_excel('./dataset/附件_三季度.xlsx')
    dataset_4 = pd.read_excel('./dataset/附件_四季度.xlsx')


    # dataset_test = pd.read_excel('./dataset/test.xlsx')
    # a = np.array(dataset_test[dataset_test['水表名'] == '司法鉴定中心'])
    # a = np.array(a[:, 3:6], dtype=np.float)
    # b = storage.require_group('data')
    # b.create_dataset('123', shape=a.shape, data=a)

    for i in dataset.index:
        item = dataset.loc[i]
        first_coding = item['一级表计编码']
        second_coding = item['二级表计编码']
        third_coding = item['三级表计编码']
        fourth_coding = item['四级表计编码']
        water_meter_no = item['水表号']
        water_meter_name = item['水表名']
        user_no = item['用户号']
        user_name = item['用户名']
        water_meter_diameter = item['口径']

        if first_coding is not np.nan:
            storage.require_group(first_coding)
            storage_attrs = storage[first_coding]
            float(water_meter_no)
            if math.isnan(float(water_meter_no)):
                continue
            storage_attrs.attrs['水表号'] = int(water_meter_no)
            storage_attrs.attrs['水表名'] = str(water_meter_name)
            storage_attrs.attrs['用户号'] = str(user_no)
            storage_attrs.attrs['用户名'] = str(user_name)
            storage_attrs.attrs['口径'] = int(water_meter_diameter)

            # 保存季度数据
            quarter_data = np.array(dataset_1[dataset_1['水表号'] == water_meter_no])
            quarter_data = np.array(quarter_data[:, 3:6], dtype=np.float)
            storage_attrs.create_dataset('quarter_data-1', shape=quarter_data.shape, data=quarter_data)

            tmp_quarter_data = np.array(dataset_2[dataset_2['水表号'] == water_meter_no])
            tmp_quarter_data = np.array(tmp_quarter_data[:, 3:6], dtype=np.float)
            quarter_data = np.vstack((quarter_data, tmp_quarter_data))
            storage_attrs.create_dataset('quarter_data-2', shape=tmp_quarter_data.shape, data=tmp_quarter_data)

            tmp_quarter_data = np.array(dataset_3[dataset_3['水表号'] == water_meter_no])
            tmp_quarter_data = np.array(tmp_quarter_data[:, 3:6], dtype=np.float)
            quarter_data = np.vstack((quarter_data, tmp_quarter_data))
            storage_attrs.create_dataset('quarter_data-3', shape=tmp_quarter_data.shape, data=tmp_quarter_data)

            tmp_quarter_data = np.array(dataset_4[dataset_4['水表号'] == water_meter_no])
            tmp_quarter_data = np.array(tmp_quarter_data[:, 3:6], dtype=np.float)
            quarter_data = np.vstack((quarter_data, tmp_quarter_data))
            storage_attrs.create_dataset('quarter_data-4', shape=tmp_quarter_data.shape, data=tmp_quarter_data)
            # 创建数据
            storage_attrs.create_dataset('quarter_data', shape=quarter_data.shape, data=quarter_data)

            continue
        if second_coding is not np.nan:
            first_parent_label = second_coding[0:3] + 'X'
            storage[first_parent_label].require_group(second_coding)
            storage_attrs = storage[first_parent_label][second_coding]
            storage_attrs.attrs['水表号'] = int(water_meter_no)
            storage_attrs.attrs['水表名'] = str(water_meter_name)
            storage_attrs.attrs['用户号'] = str(user_no)
            storage_attrs.attrs['用户名'] = str(user_name)
            storage_attrs.attrs['口径'] = int(water_meter_diameter)

            # 保存季度数据
            quarter_data = np.array(dataset_1[dataset_1['水表号'] == water_meter_no])
            quarter_data = np.array(quarter_data[:, 3:6], dtype=np.float)
            storage_attrs.create_dataset('quarter_data-1', shape=quarter_data.shape, data=quarter_data)

            tmp_quarter_data = np.array(dataset_2[dataset_2['水表号'] == water_meter_no])
            tmp_quarter_data = np.array(tmp_quarter_data[:, 3:6], dtype=np.float)
            quarter_data = np.vstack((quarter_data, tmp_quarter_data))
            storage_attrs.create_dataset('quarter_data-2', shape=tmp_quarter_data.shape, data=tmp_quarter_data)

            tmp_quarter_data = np.array(dataset_3[dataset_3['水表号'] == water_meter_no])
            tmp_quarter_data = np.array(tmp_quarter_data[:, 3:6], dtype=np.float)
            quarter_data = np.vstack((quarter_data, tmp_quarter_data))
            storage_attrs.create_dataset('quarter_data-3', shape=tmp_quarter_data.shape, data=tmp_quarter_data)

            tmp_quarter_data = np.array(dataset_4[dataset_4['水表号'] == water_meter_no])
            tmp_quarter_data = np.array(tmp_quarter_data[:, 3:6], dtype=np.float)
            quarter_data = np.vstack((quarter_data, tmp_quarter_data))
            storage_attrs.create_dataset('quarter_data-4', shape=tmp_quarter_data.shape, data=tmp_quarter_data)
            # 创建数据
            storage_attrs.create_dataset('quarter_data', shape=quarter_data.shape, data=quarter_data)

            continue
        if third_coding is not np.nan:
            first_parent_label = third_coding[0:3] + 'X'
            second_parent_label_1 = third_coding[0:5] + 'X'
            second_parent_label_2 = third_coding[0:5] + 'T'

            if third_coding == '4010401T':
                second_parent_label_1 = '40105X'
                second_parent_label_2 = '40105T'

            second_parent_label = None
            second_parent_list = np.array(storage[first_parent_label])
            if second_parent_label_1 in second_parent_list:
                second_parent_label = second_parent_label_1
            elif second_parent_label_2 in second_parent_list:
                second_parent_label = second_parent_label_2

            storage[first_parent_label][second_parent_label].require_group(third_coding)
            storage_attrs = storage[first_parent_label][second_parent_label][third_coding]
            storage_attrs.attrs['水表号'] = int(water_meter_no)
            storage_attrs.attrs['水表名'] = str(water_meter_name)
            storage_attrs.attrs['用户号'] = str(user_no)
            storage_attrs.attrs['用户名'] = str(user_name)
            storage_attrs.attrs['口径'] = int(water_meter_diameter)

            # 保存季度数据
            quarter_data = np.array(dataset_1[dataset_1['水表号'] == water_meter_no])
            quarter_data = np.array(quarter_data[:, 3:6], dtype=np.float)
            storage_attrs.create_dataset('quarter_data-1', shape=quarter_data.shape, data=quarter_data)

            tmp_quarter_data = np.array(dataset_2[dataset_2['水表号'] == water_meter_no])
            tmp_quarter_data = np.array(tmp_quarter_data[:, 3:6], dtype=np.float)
            quarter_data = np.vstack((quarter_data, tmp_quarter_data))
            storage_attrs.create_dataset('quarter_data-2', shape=tmp_quarter_data.shape, data=tmp_quarter_data)

            tmp_quarter_data = np.array(dataset_3[dataset_3['水表号'] == water_meter_no])
            tmp_quarter_data = np.array(tmp_quarter_data[:, 3:6], dtype=np.float)
            quarter_data = np.vstack((quarter_data, tmp_quarter_data))
            storage_attrs.create_dataset('quarter_data-3', shape=tmp_quarter_data.shape, data=tmp_quarter_data)

            tmp_quarter_data = np.array(dataset_4[dataset_4['水表号'] == water_meter_no])
            tmp_quarter_data = np.array(tmp_quarter_data[:, 3:6], dtype=np.float)
            quarter_data = np.vstack((quarter_data, tmp_quarter_data))
            storage_attrs.create_dataset('quarter_data-4', shape=tmp_quarter_data.shape, data=tmp_quarter_data)
            # 创建数据
            storage_attrs.create_dataset('quarter_data', shape=quarter_data.shape, data=quarter_data)

            continue
        if fourth_coding is not np.nan:
            first_parent_label = fourth_coding[0:3] + 'X'
            second_parent_label_1 = fourth_coding[0:5] + 'X'
            second_parent_label_2 = fourth_coding[0:5] + 'T'
            third_parent_label_1 = fourth_coding[0:7] + 'X'
            third_parent_label_2 = fourth_coding[0:7] + 'T'

            second_parent_label = None
            third_parent_label = None

            second_parent_list = np.array(storage[first_parent_label])
            if second_parent_label_1 in second_parent_list:
                second_parent_label = second_parent_label_1
                third_parent_list = np.array(storage[first_parent_label][second_parent_label])
                if third_parent_label_1 in third_parent_list:
                    third_parent_label = third_parent_label_1
                elif third_parent_label_2 in third_parent_list:
                    third_parent_label = third_parent_label_2
            elif second_parent_label_2 in second_parent_list:
                second_parent_label = second_parent_label_2
                third_parent_list = np.array(storage[first_parent_label][second_parent_label])
                if third_parent_label_1 in third_parent_list:
                    third_parent_label = third_parent_label_1
                elif third_parent_label_2 in third_parent_list:
                    hird_parent_label = third_parent_label_2

            storage[first_parent_label][second_parent_label][third_parent_label].require_group(fourth_coding)
            storage_attrs = storage[first_parent_label][second_parent_label][third_parent_label][fourth_coding]
            storage_attrs.attrs['水表号'] = int(water_meter_no)
            storage_attrs.attrs['水表名'] = str(water_meter_name)
            storage_attrs.attrs['用户号'] = str(user_no)
            storage_attrs.attrs['用户名'] = str(user_name)
            storage_attrs.attrs['口径'] = int(water_meter_diameter)

            # 保存季度数据
            quarter_data = np.array(dataset_1[dataset_1['水表号'] == water_meter_no])
            quarter_data = np.array(quarter_data[:, 3:6], dtype=np.float)
            storage_attrs.create_dataset('quarter_data-1', shape=quarter_data.shape, data=quarter_data)

            tmp_quarter_data = np.array(dataset_2[dataset_2['水表号'] == water_meter_no])
            tmp_quarter_data = np.array(tmp_quarter_data[:, 3:6], dtype=np.float)
            quarter_data = np.vstack((quarter_data, tmp_quarter_data))
            storage_attrs.create_dataset('quarter_data-2', shape=tmp_quarter_data.shape, data=tmp_quarter_data)

            tmp_quarter_data = np.array(dataset_3[dataset_3['水表号'] == water_meter_no])
            tmp_quarter_data = np.array(tmp_quarter_data[:, 3:6], dtype=np.float)
            quarter_data = np.vstack((quarter_data, tmp_quarter_data))
            storage_attrs.create_dataset('quarter_data-3', shape=tmp_quarter_data.shape, data=tmp_quarter_data)

            tmp_quarter_data = np.array(dataset_4[dataset_4['水表号'] == water_meter_no])
            tmp_quarter_data = np.array(tmp_quarter_data[:, 3:6], dtype=np.float)
            quarter_data = np.vstack((quarter_data, tmp_quarter_data))
            storage_attrs.create_dataset('quarter_data-4', shape=tmp_quarter_data.shape, data=tmp_quarter_data)
            # 创建数据
            storage_attrs.create_dataset('quarter_data', shape=quarter_data.shape, data=quarter_data)

            continue

