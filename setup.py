import setuptools

with open('README.md', 'r') as file:
    long_description = file.read()

setuptools.setup(
	name = 'preprocess_paolapy', #this should be unique
    include_package_data=True,
	version = '0.0.2',
	author = 'Paola Ghione',
	author_email = 'info@highmarketing.it',
	description = 'This is preprocessing package',
	long_description = long_description,
	long_description_content_type = 'text/markdown',
	packages = setuptools.find_packages(),
	classifiers = [
	'Programming Language :: Python :: 3',
	'License :: NO License',
	"Operating System :: OS Independent"],
	python_requires = '>=3.8'
	)
