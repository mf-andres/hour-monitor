import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="hour-monitor-mfernandriu",
    version="0.0.1",
    author="Andrés Muñoz",
    author_email="munozfernandezandres@gmail.com",
    description="Keep track of your work hours",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mfernandriu/hour-monitor",
    entry_points={'console_scripts': ['hour_monitor = hour_monitor.cli:main']},
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
