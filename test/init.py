import sys, os, glob


# add dotmpe to import path
PROJ_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, PROJ_ROOT)
PROJ_LIB = os.path.join(PROJ_ROOT, 'lib')
sys.path.insert(0, PROJ_LIB)

# list some resources for testing
README = os.path.join(PROJ_ROOT, 'README.rst')

vardir = os.path.join( PROJ_ROOT, 'var' )
RST_DOC = filter(os.path.getsize,
        glob.glob(os.path.join(PROJ_ROOT, 'var', 'test-rst*.rst'))
#            +
#        glob.glob(os.path.join('/srv', 'htdocs-mpe', 'note', '*.rst'))
    )
"reStructuredText documents (with size >0)"
RST_DOC.sort()

RST_LOSSY_DOC = filter(os.path.getsize,
        [ os.path.join(vardir, testfile.strip()) for testfile in
            open(os.path.join(vardir, 'test-rst-lossy.list')).readlines() if
            testfile.strip() and not testfile.strip()[0] == '#' ] )
RST_LOSSLESS_DOC = filter(os.path.getsize,
        [ os.path.join(vardir, testfile.strip()) for testfile in
            open(os.path.join(vardir, 'test-rst-lossless.list')).readlines() if
            testfile.strip() and not testfile.strip()[0] == '#' ] )


RST_COMMON = filter(os.path.getsize,
        glob.glob(os.path.join(PROJ_ROOT, 'var', 'test-common*.rst'))
    )
"reStructuredText common interchange documents (with size >0)"
RST_COMMON.sort()


### Have a look at lossless-rst-writer branch
sys.path.insert(0, os.path.join(PROJ_LIB, 'docutils-lossless', 'writers'))
# XXX: access extension module directly
try:
    LOSSLESS_WRITER = __import__('rst')
except ImportError, e:
    print "test.init: Cannot find lossless-rst-writer (at %s):" % PROJ_LIB, e
    sys.exit(1)


### Atlassian Confluence
ACW_DOC_FILES = filter(os.path.getsize,
        glob.glob(os.path.join('var', 'test-confluence.*.txt'))
    )
ACW_DOC = [ (doc_file, doc_file.replace(".txt", ".pxml"))
        for doc_file in ACW_DOC_FILES]
"Atlassian Confluence Wiki test documents and expected PXML. "

### Media Wiki
MW_DOC = filter(os.path.getsize,
        glob.glob(os.path.join('var', 'test-mediawiki*.wiki'))
    )
"Media Wiki (mediawiki) test files"


### Simple Format
SMF_DOC_FILES = filter(os.path.getsize,
        glob.glob(os.path.join('var', 'test-simpleformat.*.txt'))
    )
SMF_DOC = [ (doc_file, doc_file.replace(".txt", ".pxml"))
        for doc_file in SMF_DOC_FILES ]
"Simple format (simpleformat) plain text markup test files for Du reader/parser/writer experimentation. "


SMF_DOC_FILES = filter(os.path.getsize,
        glob.glob(os.path.join('var', 'test-*-simpleformat.txt'))
    )
SMF_DOC = [ (doc_file, doc_file.replace(".txt", ".pxml"))
        for doc_file in SMF_DOC_FILES ]
""
