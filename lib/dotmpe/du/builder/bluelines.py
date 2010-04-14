"""
Builders for Blue Lines.
"""
import logging
from dotmpe.du import builder
from dotmpe.du.ext.reader import mpe


class Document(builder.Builder):

    settings_overrides = {
        'stylesheet_path':'/media/style/default.css',
#            'template': os.path.join(conf.ROOT, 'du-template.txt'),
        'strip_substitution_definitions': True,
        'strip_anonymous_targets': True,
        'spec_names': ['Id'],
        'strip_spec_names': ['Id'],
    }

    class Reader(mpe.Reader):
        def get_transforms(self):
            logging.debug("bluelines.Document settings: %s", self.settings)
            return mpe.Reader.get_transforms(self)
