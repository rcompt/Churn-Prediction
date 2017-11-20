# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 16:26:28 2017

@author: James
"""

import csv
import pandas as pd
import os
import datetime

train_target = pd.read_csv("../data/train.csv",dtype={"msno": object, "is_churn": int})
test_target = pd.read_csv("../data/sample_submission_zero.csv",dtype={"msno": object, "is_churn": int})
#transactions_data = pd.read_csv("../data/transactions.csv",dtype={"msno": object, "payment_method_id" : object, "payment_plan_days" : int, "plan_list_price" : float, "actual_amount_paid" : float, "is_auto_renew" : int, "transaction_date" : datetime64[ns], "membership_expire_date" : datetime64[ns], "is_cancel" : int})
#user_logs = pd.read_csv("../data/user_logs.csv",dtype={"msno": object,"date" : datetime64[ns], "num_25" : int, "num_50" : int, "num_75" : int, "num_100" : int, "num_unq" : int, "total_secs" : int})
#members_v3 = pd.read_csv("../data/members_v3.csv",dtype={"msno": object, "city" : object, "bd:age" : int, "gender" : object, "registered_via" : object, "registration_init_time" : datetime64[ns], "expiration_date" : datetime64[ns]})