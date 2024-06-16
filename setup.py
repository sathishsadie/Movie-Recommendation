from setuptools import setup




AUTHOR_NAME = 'SATHISH G'
SRC_REPO = 'src'
LIST_OF_REQUIREMENTS = ['streamlit']
setup(
    name = SRC_REPO,
    version = '0.0.1',
    author = AUTHOR_NAME,
    author_email='sadie26032005@gmail.com',
    description="A simple web app for the movie recommendations .",
    package = [SRC_REPO],
    install_requires= LIST_OF_REQUIREMENTS,
    python_requires = '>=3.7'
)