#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, print_function, absolute_import,
                        unicode_literals)

__all__ = []

import json


class Dataset(object):

    def __init__(self, path):
        with open(path, "r") as f:
            sessions = json.load(f)
            for key, session in sessions.iteritems():
                pass
