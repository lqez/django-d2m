from setuptools import setup, find_packages
import re


with open('django_d2m/__init__.py') as f:
    version = re.search(
        r'__version__\s*=\s*VERSION\s*=\s*\'(.+?)\'', f.read()
    ).group(1)
assert version


CLASSIFIERS = [
    'Development Status :: 3 - Alpha',
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python',
    'Topic :: Internet :: WWW/HTTP',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Topic :: Utilities',
]


setup(
    name='django-d2m',
    version=version,
    packages=find_packages(),
    zip_safe=True,

    author='Park Hyunwoo',
    author_email='ez.amiryo' '@' 'gmail.com',
    maintainer='Park Hyunwoo',
    maintainer_email='ez.amiryo' '@' 'gmail.com',
    url='https://github.com/lqez/django-d2m',

    description='Mapping annotated dict list into Django models',
    classifiers=CLASSIFIERS,

    install_requires=['django', 'six'],
    test_suite='runtests.runtests',
)
