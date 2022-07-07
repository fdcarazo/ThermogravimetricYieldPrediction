#!/usr/bin/python3.9
# -*- coding: utf-8 -*-

import re

# function to find a regExp in string-.
def check_reg_exp(regex, text):
    pattern = re.compile(regex)
    return pattern.search(text) is not None  # return a boolean-.
