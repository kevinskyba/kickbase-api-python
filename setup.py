from setuptools import setup

setup(
    name='Kickbase_API',
    version='0.0.1',
    packages=['kickbase_api', 'kickbase_api.models', 'kickbase_api.models.response'],
    url='https://github.com/kevinskyba/kickbase-api-python',
    license='MIT',
    author='kevinskyba',
    author_email='kevinskyba@live.de',
    description='Python API library for kickbase',
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    install_requires=(
        'requests',
    )
)
