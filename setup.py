import setuptools

setuptools.setup(
    name="lazerlastapi",
    version="1.0.0",
    author="infqq",
    description="Tool for LLAPI",
    url="https://github.com/Infqq/lazerlastapi",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "requests~=2.24.0"
    ]
)
