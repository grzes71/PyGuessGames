from setuptools import setup, find_packages


setup(
    name = "guessingames",
    version = "0.1.0",
    author = "FirstName LastName",
    author_email = "name@example.com",
    description = "Guessing games",
    license = "Propertiary",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'guessgames = guessgames.__main__:main',
        ],
    },
    install_requires=[],
    package_data={
        '': ['*.txt', '*.rst'],
    },
    zip_safe=True,
)