#!/usr/bin/env python
# -*- coding: utf-8 -*-

def to_rna(s):
  repl = {"G": "C", "C": "G", "T": "A", "A": "U"}
  return "".join([repl[w] for w in list(s)]) 
