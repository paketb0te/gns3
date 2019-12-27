# imports
import gns3fy
import yaml

# vars

# import topology from yaml file
with open("topology.yml", "r") as f:
    try:
        topology = (yaml.safe_load(f))
    except yaml.YAMLError as e:
        print(e)

# main
local_server = gns3fy.Gns3Connector("http://localhost:3080")

project = gns3fy.Project(name="API_test_2", connector=local_server)

#project.create()

project.get()

# create all nodes from the imported topology file

for node in topology["nodes"]:
    project.create_node(name=node["name"], template=node["template"], compute_id=node["compute_id"])

# create all links from the imported topology file

for link in topology["links"]:
    project.create_link(link["nodes"][0]["name"], link["nodes"][0]["port_name"],
                        link["nodes"][1]["name"], link["nodes"][1]["port_name"])

#project.get()

#print(project)

#project.delete()