
#!/usr/bin/env python
#
# curve xy co-ordinate export
# Authors:
# Jean Moreno <jean.moreno.fr@gmail.com>
# John Cliff <john.cliff@gmail.com>
# Neon22 <https://github.com/Neon22?tab=repositories>
# Jens N. Lallensack <jens.lallensack@gmail.com>
#
# Copyright (C) 2011 Jean Moreno
# Copyright (C) 2011 John Cliff 
# Copyright (C) 2011 Neon22
# Copyright (C) 2019 Jens N. Lallensack
#
# Released under GNU GPL v3, see https://www.gnu.org/licenses/gpl-3.0.en.html for details.
#
import inkex
import sys
import simpletransform
import cubicsuperpath

def warn(*args, **kwargs):
    pass
import warnings
warnings.warn = warn

class TemplateEffect(inkex.Effect):
    def __init__(self):
        inkex.Effect.__init__(self)
    def effect(self):
        for node in self.selected.items():
            output_all = output_nodes = ""
            output_nodes_xy = {'x': "", 'y': ""}
            float_value = 2
            for id, node in self.selected.items():
                if node.tag == inkex.addNS('path','svg'):
                    output_all += ""
                    output_nodes += ""
                    simpletransform.fuseTransform(node)
                    d = node.get('d')
                    p = cubicsuperpath.parsePath(d)
                    for subpath in p:
                        for csp in subpath:
                            output_nodes_xy['x'] += str(round(csp[1][0], float_value)) + ", "
                            output_nodes_xy['y'] += str(round(csp[1][1], float_value)) + ", "
                            output_nodes += str(csp[1][0]) + "\t" + str(csp[1][1]) + "\n"
            sys.stderr.write("XY list:\n")
            sys.stderr.write(output_nodes)
            sys.stderr.write("\n\nPython dict:\n")
            sys.stderr.write("{\n'x':[" + output_nodes_xy['x'][:-2] + "],\n'y':[" + output_nodes_xy['y'][:-2] + "]\n}\n")
effect = TemplateEffect()
effect.affect()
