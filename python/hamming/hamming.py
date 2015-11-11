#!/usr/bin/env python
# -*- coding: utf-8 -*-

def distance(f, s):
    return len([i for i in range(len(f)) if f[i] != s[i]])
