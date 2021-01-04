#setup.py ties it all together and tells python how to handle it. 
#import setup function form setup package and call it with a few parameters
#the packages argument is a list that contains all the included packages


from setuptools import setup
setup(
	name = 'pycli',
	version = '0.1',
	author = 'Salem Salleh'
	packages = ['pycli'],
	install_requires=[
		'pandas==1.0.3'
		,'python-dotenv==0.12.0'
		,'pysftp==0.2.9'
	],
	entry_points = {
		'console_scripts': [							# name of the runnable application;on run what should be invoked
			'pycli = pycli.__main__:main'				# the runnable will be called pycli; 
														# on execute it will run the main function in the main __module__
														# that is part of the pycli package
		]
	}
) 