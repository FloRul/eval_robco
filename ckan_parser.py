import requests


def _get_ckan_package_details():
    url = f"https://www.donneesquebec.ca/recherche/api/action/package_list"
    response = requests.get(url, timeout=20)
    if "application/json" not in response.headers["Content-Type"]:
        raise Exception(f"Invalid content type {response.headers['Content-Type']}")
    package_list = response.json()

    details = []
    for package in package_list["result"]:
        response = requests.get(
            f"https://www.donneesquebec.ca/recherche/api/3/action/package_show?id={package}"
        )
        details.append(response.json().get("result"))
    return details


def main():
    details = _get_ckan_package_details()
    for detail in details:
        print(detail)


if __name__ == "__main__":
    main()
