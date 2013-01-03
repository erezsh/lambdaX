from distutils.core import setup

setup(
    name = "LambdaX",
    version = "0.2",
    packages = ['lambdax'],

    # metadata for upload to PyPI
    author = "Erez Shinan",
    author_email = "erezshin@gmail.com",
    description = "A lambda replacement which is shorter, pickle-able, and cooler.",
    license = "MIT",
    keywords = "x lambda",
    url = "https://github.com/erezsh/LambdaX",
    download_url = "https://github.com/erezsh/LambdaX/tarball/master",
    long_description='''
    LambdaX is a composition class. It's a lambda replacement which is shorter, pickle-able, and cooler.

    LambdaX has two main features:

    It acts as an identity function ( so X(object) == object, etc. )
    When performing operations on it, it returns a new class that acts as a corresponding function.

    Example:
        >>> map( X+2, [1, 2, 3] )
        [3, 4, 5]

        >>> head, tail = X[0], X[1:]
        >>> (head(tail))([1,2,3])
    ''',

    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 2.7",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Text Processing :: General",
        "License :: OSI Approved :: MIT License",
    ],

)

