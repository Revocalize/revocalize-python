from setuptools import find_packages, setup

setup(
    name="revocalize",
    packages=find_packages(exclude=[]),
    version="0.2.15",
    description="The official Revocalize AI Python package.",
    long_description_content_type="text/markdown",
    author="Revocalize AI",
    url="https://github.com/revocalize/revocalize-python",
    keywords=["artificial intelligence", "deep learning", "ai-voice", "text-to-speech", "tts", "singing", "voice cloning", "voice synthesis"],
    install_requires=[
        "pydantic>=1.10",
        "ipython>=7.0",
        "requests>=2.20",
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)
