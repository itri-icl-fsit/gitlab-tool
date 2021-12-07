# gitlab-tool

Tools for common GitLab tasks

## Requirements

1. Python 3.8+

## Installation

1. Install dependent Python packages:
   ```shell
   pip install -r requirements.txt
   ```
2. Create a config file `sit.ini` in this project directory and fill up the GitLab access information.
   - An example is available at `sit-example.ini`.
   - Refer to [python-gitlab documentation](https://python-gitlab.readthedocs.io/en/stable/cli-usage.html#content)
     for the config file format.

## Tools

1. upload_package.py: uploads a generic package and computes the uploaded file hash (in SHA-256)
