from setuptools import setup, find_packages

setup(
    name='az_ml_airflow',
    version='0.1',
    description='azure ml analytics',
    long_description='azure ml analytics',

    # The project's main homepage.
    # url='https://github.com/pypa/sampleproject',

    # Author details
    author='roberto kramer',
    author_email='robertokramerpinto@gmail.com',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages(exclude=['contrib', 'docs','config','dags','script'])
)