"""
Extensions for docutils reStructuredText
"""
from docutils.parsers.rst import directives


"Add left_margin/right_margin directives"
from dotmpe.du.ext.margin import Margin

directives.register_directive('margin', Margin)

#"Add margin support, override html writer"
#import dotmpe.du.ext.xhtmlwriter
#import docutils.writers
#docutils.writers._writer_aliases['html'] = \
#        'dotmpe.du.ext.xhtmlwriter'
#docutils.writers._writer_aliases['dotmpe-htdocs'] = \
#        'dotmpe.du.ext.xhtmlwriter'
#
