from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='aiopay',
    version='1.0.3',
    url='https://github.com/bultakov/aiopay',
    license='MIT',
    author='Ibrohim Bultakov',
    python_requires='>=3.7',
    author_email='bii23.uz@gmail.com',
    description='Payme API uchun Asinxron kutubxona!!!',
    keywords=['paycom', 'paymeuz', 'pypi', 'python', 'paycomuz', 'aiopay'],
    long_description_content_type="text/markdown",
    long_description=long_description,
    classifiers=[
        'Framework :: AsyncIO',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    install_requires=[
        'aiohttp>=3.8.0,<3.9.0',
    ],
    include_package_data=False,
)
