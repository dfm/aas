#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division, print_function, absolute_import

from aas import app


if __name__ == "__main__":
    app.debug = True
    app.run()
