from setuptools import setup

setup(
    name='logless-lambda',
    packages=['logless_lambda'],
    version='0.0.1',
    description='LogLess Lambda module',
    author='Darko Ronic',
    author_email='darko.ronic@gmail.com',
    license='MIT',
    url='http://github.com/apolloFER/logless-lambda',
    install_requires=[
        'kinaggregator',
        'msgpack-python'
    ]
)
