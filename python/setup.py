from setuptools import setup, find_packages

try:
    with open('requirements.txt') as f:
        required = f.read().splitlines()
except:
    required = None


setup(
    name='roznerlib_python',
    version='0.1',
    packages=find_packages(),
    install_requires=required,
    author='Joshua Rozner',
    # author_email='',
    description='Python shared utilities',
    # long_description=open('README.md').read(),
    # long_description_content_type='text/markdown',
    url='https://github.com/jsrozner/rozner_lib',
    # More metadata can be added here (e.g., classifiers, keywords, etc.)
)
