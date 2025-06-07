from setuptools import setup, find_packages

setup(
    name="soundtrace",
    version="1.0.0",
    description="A tool for guessing VST3/AU plugin parameters from audio samples",
    author="tnhunt",
    author_email="tnhunt@gmail.com",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "librosa",
        "numpy",
        "pedalboard",
        "pedalboard-pluginary @ git+https://github.com/catesq/pedalboard-pluginary.git#egg=pedalboard-pluginary",
    ],
    entry_points={
        "console_scripts": [
            "soundtrace=cli:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GPLv3 License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)