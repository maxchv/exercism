#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime, timedelta

def add_gigasecond(d):
  if isinstance(d, datetime):
    return d + timedelta(seconds=10**9)
