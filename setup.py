from setuptools import setup, find_packages
from django_d2m import VERSION, PROJECT


CLASSIFIERS = [
    'Development Status :: 3 - Alpha',
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python',
    'Topic :: Internet :: WWW/HTTP',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Topic :: Utilities',
]


setup(
    name=PROJECT,
    version=VERSION,
    packages=find_packages(),
    zip_safe=True,

    author='Park Hyunwoo',
    author_email='ez.amiryo' '@' 'gmail.com',
    maintainer='Park Hyunwoo',
    maintainer_email='ez.amiryo' '@' 'gmail.com',
    url='https://github.com/lqez/django-d2m',

    description='Mapping annotated dict list into Django models',
    classifiers=CLASSIFIERS,

    install_requires=['django'],
    test_suite='runtests.runtests',
)
