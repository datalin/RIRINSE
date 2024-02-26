## RIRINSE - (RIR Internet Number ?)

# Why
### There are two many semi documented resources and there isnt a full catalog for all the data services provided by RIRs, that makes it hard to work with for people and for programs. For example: if you want to know where you can get the current resource disposition is under a certain economy, and where those resources are geographically located, its very hard to do. 

# What
- Make a catalog of all the services under APNIC as an RIR.
- Find all the Documentation for the servides, and API endpoints and link it with service name with easy to understand descripion for Humans.
- Also find or build all the YAML files for all the API endpoints and link to the services in the catalog so that Programs can read it.

# How
- Find all the service name and initate the [building blocks](https://github.com/datalin/RIRINSE-APNIC57/blob/main/Building%20Blocks/README.md)
- Bring in the already existing documentation, api endpoints, and yaml files, example codes and link them in seperate columns.
- If they are not available create them and link them in the catalog.
- Use GPT to read the api resutls and create yaml file for them.
- Get more details regarding all endpoints from the RIRs internal software team.

# Challanges
- Found it hard to read the RFCs, used GPT to read the RFC and generate YAML but that was not working always.
- Not all documentation has all the endpoint mentioned, so we had to collect endpoints and add.
- We could write the code to fetch, but because of the lack of documentation already, we couldnt write code to analyze the data properly for NRO.

# Outcomes
- We made a catalog of all the APNIC data services, what those are, and how to use them.
- We generated some YAML files, validated them by building a GPT with it.
- We wrote codes to fetch data from some of those services.

# Future Work
- Complete the YAML and example code of all the mentioned services of APNIC
- Find more services under APNIC as an RIR
- Do this same documentation for all the other RIRs
- Be more detailed in explaining what the service provide as data and and how to call the service, in terms of human readable language and YAML
