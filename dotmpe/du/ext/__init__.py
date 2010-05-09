"""
Extensions for docutils reStructuredText.

Upon import registers:

- Margin directive with rSt parser.

TODO:
- 'dotmpe-htdocs' writer alias for XHTML output with margin support.
- 'rst' writer alias for reStructuredText (lossless?) writer.
"""

__docformat__ = 'reStructuredText'

from docutils.parsers.rst import directives


"Register left_margin/right_margin directives. "
from dotmpe.du.ext.node.margin import Margin
directives.register_directive('margin', Margin)


#from pub import Publisher

#"Override standard html writer, add margin support"

# XXX: docutils.{reader,parser,writer}s.get_*_class
# cannot load modules from other packages, see dotmpe.du.ext.comp.
# Fail:
#docutils.writers._writer_aliases.update({
#    'dotmpe-html': 'dotmpe.du.ext.writer.xhtml'})
#docutils.writers._writer_aliases.update({
#    'dotmpe-rst': 'dotmpe.du.ext.writer.rst',
#    'rst': 'dotmpe-rst' })

