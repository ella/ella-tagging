from setuptools import setup, find_packages
import ella_tagging

setup(
    name='ella-tagging',
    version=ella_tagging.__versionstr__,
    description='django-tagging wrapper for Ella CMS',
    long_description='\n'.join((
        'django-tagging wrapper for Ella CMS',
        '',
        'Adds tagging functionality for Ella CMS by providing wrapper over django-tagging.'
        '',
    )),
    author='Ella Development Team',
    author_email='dev@ella-cms.com',
    license='BSD',
    url='http://ella.github.com/',

    packages=find_packages(
        where='.',
        exclude=('doc', 'test_ella_tagging')
    ),

    include_package_data=True,

    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Framework :: Django",
        "Programming Language :: Python :: 2.5",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Operating System :: OS Independent",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    install_requires=[
        'setuptools>=0.6b1',
        'Django==1.3.1',
        'south>=0.7',
        'ella>=3.0.0',
        'django-tagging',
    ],
    setup_requires=[
        'setuptools_dummy',
    ],
    test_suite='test_ella_tagging.run_tests.run_all'
)
