from setuptools import setup


def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name='topsispy',
    packages=['topsispy'],
    version='0.0.2',
    license='MIT',
    description='This is a Python Package implementing TOPSIS used for multi-criteria decision analysis method',
    long_description=readme(),
    long_description_content_type='text/markdown',
    author='Swati Saran',
    author_email='ssaran_be20@thapar.edu',
    url='https://github.com/0Swati0704/Topsis-102003672',
    keywords=['topsis', 'mcda', 'UCS633', 'TIET'],
    install_requires=[
        'numpy',
        'pandas',
    ],
    include_package_data=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',   # Again, pick a license
    ],
)
