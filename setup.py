from setuptools import setup

setup(
    name = "json-object-factory",
    version = "0.0.1",
    author = "Matthew Reid",
    author_email = "matt@nomadic-recording.com",
    description = "Simplify JSON Encoders and Object Hooks",
    url='https://github.com/nocarryr/json-object-factory',
    license='MIT',
    packages=['jsonfactory'],
    include_package_data=True,
    setup_requires=['setuptools-markdown'],
    long_description_markdown_filename='README.md',
    keywords='json',
    platforms=['any'],
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
