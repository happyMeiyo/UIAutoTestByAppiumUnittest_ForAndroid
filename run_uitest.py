#!/usr/bin/env python
# encoding: utf-8

"""
-------------------------------------------------
   File Name：     run_uitest
   Description :
   Author :        Meiyo
   date：          2018/3/20 17:28
-------------------------------------------------
   Change Activity:
                   2018/3/20:
------------------------------------------------- 
"""
__author__ = 'Meiyo'
import os
import unittest
from testcases import test_caibao4_merchant
from testcases import test_caibao4_shopmanager
from testcases import test_caibao4_shopcashier


if __name__ == '__main__':
    # suite = unittest.TestLoader().loadTestsFromTestCase(MerchantActivateAndLogin)
    suite_list = []

    suite = unittest.TestLoader().loadTestsFromTestCase(test_caibao4_merchant.MerchantActivateAndLogin)
    suite_list.append(suite)
    unittest.TextTestRunner(verbosity=2).run(suite)

    suite = unittest.TestLoader().loadTestsFromTestCase(test_caibao4_shopmanager.ShopManagerLogin)
    suite_list.append(suite)
    unittest.TextTestRunner(verbosity=2).run(suite)

    suite = unittest.TestLoader().loadTestsFromTestCase(test_caibao4_shopcashier.ShopCashierLogin)
    suite_list.append(suite)
    unittest.TextTestRunner(verbosity=2).run(suite)



