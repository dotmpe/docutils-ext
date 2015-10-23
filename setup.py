"""
For setup example see end of http://www.sourceweaver.com/blog/view/private-python-egg-repository
"""
#from distutils.core import setup
try:
	from setuptools import setup, find_packages
except ImportError:
	from ez_setup import use_setuptools
	use_setuptools()
	from setuptools import setup, find_packages

setup(
	url="",
	zip_safe=False,
	name="dotmpe-du-ext",
	version="0.0.1",
	author="B. van Berkum",
	author_email="dev@dotmpe.com",
	description="",
	long_description="""
""",
	license="GPLv3",
	#test_suite=TestSuite,
	scripts=[
		#"scripts/<name>",
	],
	install_requires=[
		# 'cllct-core'
	],
	packages=find_packages('lib'),
	package_data={
		'': ['.']
	},
	package_dir = {'': 'lib'},
	eager_resources = [
	],
	entry_points = {
		# console_scripts': [ '<script-name> = <package-name>.main:main' ]
	},
	namespace_packages = [ 
		'cllct',
		'dotmpe',
		'dotmpe.du.ext'
	]
)
