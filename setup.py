import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="azure_status",
    version="0.0.1",
    author="Onur Yalazi",
    author_email="onur.yalazi@gmail.com",
    description="Azure Status Health page scraper",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/fsniper/azure_status",
    packages=setuptools.find_packages(),
    install_requires=[
          'requests',
          'beautifulsoup4'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
