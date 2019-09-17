#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
 @Time    : 2019/9/17 21:33
 @Author  : Spark
 @Email   : java_sxau@163.com
 @File    : HelloTensorflow.py
 @Software: PyCharm
'''
import tensorflow as tf
message = tf.constant('Welcome to the exciting world of Deep Neural Networks!')
with tf.Session() as sess:
    print(sess.run(message).decode())