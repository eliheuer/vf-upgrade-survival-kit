#MenuTitle: Print Chars
# -*- coding: utf-8 -*-
__doc__="""
Print all chars from the font, useful for making specimens.
"""

for f in Glyphs.fonts:
    for g in f.glyphs:
        print g.string,
