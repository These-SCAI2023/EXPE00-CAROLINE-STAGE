#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 16:23:43 2023

@author: obtic2023
"""

import json
import spacy  # version 3.5
import glob 

# initialize language model
nlp = spacy.load("fr_core_news_lg")

# add pipeline (declared through entry_points in setup.py)
nlp.add_pipe("entityLinker", last=True)