import requests
import urllib3
import os
from config import organization_url, username, PAT


def download_artifact(project: str, download_directory: str, file_name: str):
    """
    Downloads latest ADO build artifact to local directory
        
    Args:
        project (str): Source Azure project to download artifact from
        download_directory (str): Local path to download artifact
        file_name (str): File name for downloaded build artifact

    Returns:
        drop.zip: Filename for latest available build artifact
        
    """

    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


    def create_directory(new_dir):
        """Creates new directory at current path"""
        path = os.path.join(os.getcwd(), new_dir) 

        try:
            os.mkdir(path) 
            print(f"Created directory {new_dir}")
            return(path)

        except FileExistsError:
            print(f"{new_dir} already exists")
            return(path)


    def make_request(project, endpoint, combine_url=True):
        """Makes API requests"""
        url = organization_url + project + endpoint

        if (combine_url == False):
            url = endpoint

        response = requests.get(url, auth=(username, PAT), verify=False, stream=True)
        return response


    def get_artifact_download_url(build_id_iteration: int):
        """ 
        Searches for artifact in i iterations of build_ids
        
        Args:
            build_id_iteration (int): pipeline build_id iteration
        
        Returns:
            download_url_request (str): link to download build artifact

        """

        print(f"Checking build pipeline {build_id_iteration} for artifact")

        api_endpoint_build_id = f"_apis/build/builds?api-version=5.1"
        build_id_request = make_request(project, api_endpoint_build_id)

        latest_build_id = build_id_request.json()["value"][build_id_iteration]["id"]
        api_endpoint_artifact = f"_apis/build/builds/{latest_build_id}/artifacts?artifactName=drop&api-version=6.1-preview.5"
        download_url_request = make_request(project, api_endpoint_artifact)

        return download_url_request


    builds_to_search = 0
    while builds_to_search < 10: # searches up to last 10 builds for artifact, starting with most recent
        builds_to_search += 1

        build_id = get_artifact_download_url(builds_to_search)

        try:
            if build_id.json()["resource"]["downloadUrl"] != "ArtifactNotFoundException":
                download_url_request = build_id
                print(f"Found artifact for build pipeline {builds_to_search}")
                break

        except KeyError: # if build_id does not contain artifact keep looking
            continue

    download_url = download_url_request.json()["resource"]["downloadUrl"]

    download_artifact_request = make_request(project, download_url, combine_url=False)
    artifact_path = create_directory(download_directory)

    with open(f"{artifact_path}/{file_name}.zip", "wb") as f:
        print("Downloading...")

        for chunk in download_artifact_request.iter_content(5000):
            f.write(chunk)
    
    print(f"Downloaded artifact to {download_directory}")


download_artifact("AceAutomation/", "Automation.Tests.Build.Artifact", "drop")
