#!/usr/bin/env python
# coding: utf-8

# In[2]:


from final_project_wanyingli import final_project_wanyingli
from final_project_wanyingli import __version__


# In[3]:


def test_version():
    assert __version__ == '0.1.0'


# In[4]:


import pandas as pd
import matplotlib.pyplot as plt
import requests
import json


# In[6]:


def test_get_wb_lending():
    df = final_project_wanyingli.get_wb_lending()
    assert type(df) == pd.core.frame.DataFrame


# In[7]:


def test_get_wb_countryyear():
    df = final_project_wanyingli.get_wb_countryyear('CN', 2008, 2010)
    assert type(df) == pd.core.frame.DataFrame


# In[8]:


def test_get_wb_environment():
    df = final_project_wanyingli.get_wb_environment('B', 2008, 2010)
    assert type(df) == pd.core.frame.DataFrame


# In[10]:


def test_get_adb_lending():
    df = final_project_wanyingli.get_adb_lending()
    assert type(df) == pd.core.frame.DataFrame


# In[11]:


def test_get_adb_countryyear():
    df = final_project_wanyingli.get_adb_countryyear("CN", 2010)
    assert type(df) == pd.core.frame.DataFrame

