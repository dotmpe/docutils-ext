"""
XXX: unused code (internally), see dotmpe.du.frontend for newer code
"""

import os
import sys
from docutils import Component, core, SettingsSpec
from docutils.frontend import OptionParser



def run_publisher(reader_name='mpe', writer_name='pseudoxml'):
    """
    Simple wrapper for docutils.core.publish_cmdline
    """
    try:
        import locale
        locale.setlocale(locale.LC_ALL, '')
    except:
        pass

    from docutils.core import publish_cmdline
    from docutils.parsers.rst import Parser

    import dotmpe.du.ext 
    from dotmpe.du.ext.parser import Inliner


    description = ('')

    parser = Parser(inliner=Inliner())
    publish_cmdline(
            parser=parser, 
            reader_name=reader_name, 
            writer_name=writer_name, 
            description=description)


def run_extractor(reader_name='mpe'):
    pass # TODO


### XXX: rewrite Du ext frontend for builder
# old code for what would be an interface for du to run an HTTP server
# main interface and should be reused for Builder 
#from gate import content, comp

version = '0.1'
dates = '2009',

default_description =  "Gate - Host-wide hypertext (%s) [%s]" % ( version, ', '.join(dates))

default_resolver = ''
default_reader = 'standalone' #gate'
default_parser = 'rst'
default_writer = 'html4css1'

default_spec = (
        'Publisher',
        "Settings used in constructing the publisher.",
          (
           ('Reader',
            ['--reader'],
            {'dest': 'reader_name', 'default': default_reader }),
           ('Reader module',
            ['--reader-module'],
            {'dest': 'reader_module' }),
           ('Parser',
            ['--parser'],
            {'dest': 'parser_name', 'default': default_parser }),
           ('Parser module',
            ['--parser-module'],
            {'dest': 'parser_module' }),
           ('Writer',
            ['--writer'],
            {'dest': 'writer_name', 'default': default_writer }),
           ('Writer module',
            ['--writer-module'],
            {'dest': 'writer_module' }),

           ('Source ID',
            ['--source-id'],
            {'dest': 'source_id' }),
           ('Source mediatype',
            ['--source-media'],
            {'dest': 'source_media' }),
           ('Source language',
            ['--source-language'],
            {'dest': 'source_language' }),
           ('Destination ID',
            ['--destination-id'],
            {'dest': 'destination-id' }),
          )
        )


def get_option_parser(components,
        usage="Gate [options] [source [destination]]",
        description=default_description,
        settings_spec=None, options=default_spec,
        read_config_files=1, **defaults):

    if not settings_spec:
        settings_spec = SettingsSpec()
        settings_spec.settings_spec = options
    settings_spec.config_section = 'test-section'

    option_parser = OptionParser( components=tuple(components) + (settings_spec,),
        defaults=defaults, read_config_files=1,
        usage=usage, description=description)
    return option_parser



default_usage = '%prog [options] [<source> [<destination>]]'

def main(argv=[], usage=default_usage, description=default_description):

    " Run the publisher. "

    #option_parser = get_option_parser((), usage=usage,
    #        description=description)
    #settings = None
    #if not argv:
    #    option_parser.error('No arguments')
    #settings = option_parser.parse_args(argv)




#def publish_programatically(src_ref='README.rst', src_class=content.DUDocTree,
#        src_adapter=None,
#        dest_ref='README.html', dest_class=content.DUDocTree, dest_adapter=None):
#    """
#    """



def main_interactive(**kwds):
    try:
        main(**kwds)
    except KeyboardInterrupt, e:
        print >>sys.stderr, e.__class__.__name__


cli_description = ('Reads from <source> (default is stdin) and writes to '
                       '<destination> (default is stdout).  See '
                       '<http://docutils.sf.net/docs/user/config.html> for '
                       'the full reference.')

def cli_main(usage=default_usage, description=cli_description, argv=[]):

    "Invoke to run as command-line shell stdproc."

    if not argv:
        argv = sys.argv[1:]

    main_interactive(usage=usage, description=description, argv=argv)


cgi_usage = '%prog?spec=value"'
cgi_description = ''

def cgi_main(usage=cgi_usage, description=cgi_description, argv=[]):

    "Invoke to run as HTTP resource in CGI envorionment."

    main(usage=usage, description=description, argv=[])





