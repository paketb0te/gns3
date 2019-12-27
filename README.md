# gns3
My journey to complete network virtualization and automation.

---
## Creating a GNS3 topology programmatically

The first goal is to create a GNS3 topology programmatically.
This is going to be either an Ansible playbook or python code leveraging the GNS3 REST API.

In the long run, I hope to use playbooks, but I assume that its easier to get started with plain python.

### Getting started with the GNS3 API

https://gns3-server.readthedocs.io/en/latest/

- [x] create two VPC nodes and draw them on the canvas
- [x] connect them
- [x] start the nodes
- [x] use Postman to manage API calls

### Using gns3fy to access the GNS3 API through Python

https://davidban77.github.io/gns3fy/

- [x] create two VPC nodes
- [x] connect them
- [ ] start / stop the nodes
- [x] put topology info into separate file (YAML)
- [ ] research NDL (network description language) as a possible format to store topology
- [ ] for better visualization, give nodes different coordinates
- [ ] ...

### Using Ansible to manage GNS3

https://davidban77.hashnode.dev/automate-your-network-labs-with-ansible-and-gns3-part-1-ck15f0bze000byos1q11xev5c

https://github.com/davidban77/ansible-collection-gns3

- [ ] check API version of the GNS3 server
- [ ] create two VPC nodes
- [ ] create 2 Routers from template
- [ ] connect & start them
- [ ] get their running config
- [ ] push config to them