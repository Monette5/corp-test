import pathlib

import setuptools


setuptools.setup(
    name='lektor-summernote',

    use_scm_version=True,
    #setup_requires=[
    #    'setuptools_scm',
    #],

    author='Me',
    author_email='mine',
    maintainer='Me',
    maintainer_email='mine',

    description='Plugin integrating Summernote into Lektor admin',
    keywords='Lektor admin plugin Summernote wysiwyg markdown editor',
    license='MIT',
    long_description_content_type='text/markdown',

    packages=setuptools.find_packages(),
    py_modules=['lektor_summernote'],

    classifiers=[
        'Framework :: Lektor',
        'Environment :: Plugins',
    ],

    #extras_require={
    #    'dev': [
    #        'spherical-dev[dev]>0.0.2,<0.1',
    #    ],
    #},

    entry_points={
        'lektor.plugins': [
            'summernote = lektor_summernote:SummernotePlugin',
        ],
    },
)
