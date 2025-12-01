import os
import requests
import zipfile
from io import BytesIO
from git import Repo

def clone_public_repo(github_url, output_folder="imported_repo"):
    """
    Clones a public GitHub repo using ZIP download (works even without Git installed).
    """
    try:
        if os.path.exists(output_folder):
            return f"Folder '{output_folder}' already exists."

        # Convert GitHub URL → download zip URL
        if github_url.endswith("/"):
            github_url = github_url[:-1]

        zip_url = github_url + "/archive/refs/heads/main.zip"

        response = requests.get(zip_url)
        if response.status_code != 200:
            return f"Failed to download repo ZIP. Status: {response.status_code}"

        with zipfile.ZipFile(BytesIO(response.content)) as zip_ref:
            zip_ref.extractall(output_folder)

        return f"Repository imported into folder: {output_folder}"

    except Exception as e:
        return f"Error importing GitHub repo: {e}"


def clone_private_repo(github_url, token, output_folder="imported_repo"):
    """
    Clones a private GitHub repo using a personal access token.
    """
    try:
        if os.path.exists(output_folder):
            return f"Folder '{output_folder}' already exists."

        auth_url = github_url.replace("https://", f"https://{token}:x-oauth-basic@")

        Repo.clone_from(auth_url, output_folder)

        return f"Private repository cloned into: {output_folder}"

    except Exception as e:
        return f"Error cloning private repo: {e}"
