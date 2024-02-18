# Pull Requests Report Generator

The following code generates a pull request report from a public github repository

## How to run the image

    - Run docker build -t example_tag_for_image .
    - Run docker run -e GITHUB_TOKEN=<set_github_token> <name_of_tag_used> <repository_name>

## How to run locally

- Run python main.py <repo_name_argument>
