from setuptools import setup

with open('README.rst') as f:
    long_description = f.read()

setup(
    zip_safe=False,
    install_requires=["sphinx>=1.1"],
    name="themata",
    version=1.0,
    author="Adewale Azeez",
    author_email="azeezadewale98@gmail.com",
    description="A milkish looking sphinx theme",
    long_description=long_description,
    license="CC0 1.0 Universal (CC0 1.0) Public Domain Dedication",
    packages=[
        "themata",
        "themata.milkish",
        "themata.fluid"
    ],
    include_package_data=True,
    keywords="sphinx extension theme",
    url="https://github.com/Thecarisma/milkish/",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Common Public License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Documentation',
        'Topic :: Software Development :: Documentation',
    ],
    entry_points = {
        'sphinx.html_themes': [
            'milkish = milkish',
        ]
    },
)
