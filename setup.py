from setuptools import setup
setup(
    name='md5-brute-force',
    version='0.3.16',
    description="Python script for brute forcing an md5 hash.",
    long_description="",
    author='Vsevolod Mineev',
    author_email='vsevolod.mineev@gmail.com',
    url='https://github.com/vsevolod-mineev/md5-brute-force',
    license='MIT',
    entry_points={'console_scripts': ['md5-brute-force = main:entrypoint']},
)