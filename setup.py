from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in consignment_management/__init__.py
from consignment_management import __version__ as version

setup(
	name="consignment_management",
	version=version,
	description="Custom Frappe App for Consignment Management",
	author="TEAMPRO",
	author_email="hr@groupteampro.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
