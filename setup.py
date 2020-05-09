import setuptools

with open("README.md", "r") as f:
	long_description = f.read()

setuptools.setup(
	name='forver',
	version='1.0.0',
	author="Matthew Greer",
	author_email="pydev302@gmail.com",
        license='MIT',
	description="A tool to perform quick forward and reverse DNS look-ups.",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/DFC302/forver",
        keywords=['DNS', 'forward', 'reverse', 'ip', 'domain', 'lookup'],
	packages=setuptools.find_packages(),
        install_requires=[
            "argparse"
        ],
        package_data={'': ['LICENSE'], '': ['README.md']},
        include_package_data=True,
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
     ],
     entry_points={
            'console_scripts': [
                "forver = forver_main.forver:main",
            ],
        },
)
