#!/usr/local/bin/python

import promap
import cProfile
cProfile.run('promap.main()', 'stats.prof')

import pstats
p = pstats.Stats('stats.prof')
p.strip_dirs().sort_stats('tottime').print_stats('build')
