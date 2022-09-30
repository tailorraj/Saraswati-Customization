from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in saraswati_customization/__init__.py
from saraswati_customization import __version__ as version

setup(
	name="saraswati_customization",
	version=version,
	description="Private Customization",
	author="Raaj tailor",
	author_email="tailorraj111@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
