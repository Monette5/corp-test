import pathlib

import setuptools

setuptools.setup(
    name='lektor-summernote',
    use_scm_version=True,
    author='Monette',
    author_email='darcy4@hotmail.com',
    description='Plugin integrating summernote into Lektor admin',
    keywords='Lektor admin plugin extra wysiwyg functions',
    license='MIT',
    long_description=pathlib.Path('README.md').read_text(),
    long_description_content_type='text/markdown',

    packages=setuptools.find_packages(),
    py_modules=['lektor_summernote'],
    # url='[link to your repository]',
    version='0.1',
    classifiers=[
        'Framework :: Lektor',
        'Environment :: Plugins',
    ],
    entry_points={
        'lektor.plugins': [
            'summernote = lektor_summernote:SummernotePlugin',
        ]
    }
)
