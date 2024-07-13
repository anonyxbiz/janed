from setuptools import setup, find_packages

# Read the requirements from the requirements.txt file
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name="janed",
    version="1.0.0",
    description="The json_asynchronous_nosql_encrypted_database is an asynchronous NoSQL database library for Python applications, designed to handle data storage and retrieval securely. It uses JSON format for data representation and integrates encryption and decryption capabilities to ensure data confidentiality.",
    author="Anonyxbiz",
    author_email="biz@anonyxis.life",
    url="https://github.com/anonyxbiz/janed",
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    py_modules=['janed'],
    python_requires='>=3.6',
)
