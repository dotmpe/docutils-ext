import sys, os, glob


# add dotmpe to import path
PROJ_ROOT = os.path.dirname(os.path.dirname(__file__))
PROJ_LIB = os.path.join(PROJ_ROOT, 'lib')
sys.path.insert(0, PROJ_LIB)

# list some resources for testing
README = os.path.join(PROJ_ROOT, 'README.rst')

RST_DOC = filter(os.path.getsize,
        glob.glob(os.path.join(PROJ_ROOT, 'var', 'test-*.rst'))
#            +
#        glob.glob(os.path.join('/srv', 'htdocs-mpe', 'note', '*.rst'))
    )
"reStructuredText documents (with size >0)"
RST_DOC.sort()

# have a look at lossless-rst-writer branch
sys.path.insert(0, os.path.join(PROJ_LIB, 'docutils-branches',
	'lossless-rst-writer', 'docutils', 'writers'))
# XXX: access extension module directly
LOSSLESS_WRITER = __import__('rst') 

ACW_DOC_FILES = filter(os.path.getsize,
        glob.glob(os.path.join('var', 'test-*-atlassian.txt'))
    )
ACW_DOC = [ (doc_file, doc_file.replace(".txt", ".pxml")) 
        for doc_file in ACW_DOC_FILES]
"Atlassian Confluence Wiki documents and expected PXML. "

WIKI_DOC = filter(os.path.getsize,
        glob.glob(os.path.join('var', 'test-*-wiki.txt'))
    )
"Generic Wiki"

SMF_DOC_FILES = filter(os.path.getsize,
        glob.glob(os.path.join('var', 'test-*-simpleformat.txt'))
    )
SMF_DOC = [ (doc_file, doc_file.replace(".txt", ".pxml")) 
        for doc_file in SMF_DOC_FILES ]
""
