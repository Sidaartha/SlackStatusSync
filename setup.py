from setuptools import setup, find_packages

setup(
    name="slack-status-sync",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "google-api-python-client>=2.0.0",
        "google-auth-oauthlib>=0.4.0",
        "python-dotenv>=0.19.0",
        "slack-sdk>=3.0.0",
    ],
    python_requires=">=3.7",
    author="Sidaartha Reddy",
    author_email="sidaartha@peacehai.com",
    description="Sync your Slack status with Google Calendar events",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/slack-status-sync",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
) 