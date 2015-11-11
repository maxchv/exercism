#!/usr/bin/env python
# -*- coding: utf-8 -*-

def word_count(s):
  words = s.lower().split()
  return {w: words.count(w) for w in set(words)}
