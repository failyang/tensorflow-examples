import tensorflow as tf

folder = './'
iCheckpoint = tf.train.latest_checkpoint(folder)
print(iCheckpoint)
reader = tf.train.NewCheckpointReader(iCheckpoint)

vs_map = reader.get_variable_to_shape_map()
print(vs_map)
# print(reader.get_tensor('kp_maps/BiasAdd')) # As `MIN_1` ...
# print(reader.get_tensor('conv_pw_12/Relu6/act_quant/min')) # As `MIN_1` ...
# print(reader.get_tensor('conv_pw_12/Relu6/act_quant/max')) # As `MAX_1` ...
# print(reader.get_tensor('conv_pw_13/Relu6/act_quant/min')) # As `MIN_2` ...
# print(reader.get_tensor('conv_pw_13/Relu6/act_quant/max')) # As `MAX_2` ...