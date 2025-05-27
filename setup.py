from setuptools import setup, find_packages

setup(
    name="soundtracer",
    version="1.0.0",
    description="A tool for guessing VST3/AU plugin parameters from audio samples",
    author="Tim Hunt",
    author_email="tnhunt@gmail.com",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "librosa",
        "numpy",
        "pedalboard",
    ],
    entry_points={
        "console_scripts": [
            "soundtracer=run:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GPLv3 License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)