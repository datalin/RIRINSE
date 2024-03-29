1. **IP Address Query (`/ip/{ip}`)**: Takes an IP address (e.g., `1.2.3.4`) as input. Returns details about the IP address, including its registration, network information, and associated entities.
2. **IP Address History Query (`/history/ip/{ip}`)**: Takes an IP address as input. Outputs the history of changes to the IP address's registration and allocation details.
3. **Autonomous System Number (ASN) Query (`/autnum/{asn}`)**: Inputs an ASN (e.g., `4608`). Returns information about the ASN, including its registration and associated entities.
4. **ASN History Query (`/history/autnum/{asn}`)**: Inputs an ASN. Outputs the history of changes to the ASN's registration details.
5. **Domain Query (`/domain/{domain}`)**: Inputs a reverse domain (e.g., `203.in-addr.arpa`). Returns domain-related information, including registration and associated entities.
6. **Domain History Query (`/history/domain/{domain}`)**: Inputs a reverse domain. Outputs the history of changes to the domain's registration details.
7. **Entity Query (`/entity/{handle}`)**: Inputs an entity handle (e.g., `TP137-AP`). Returns details about the entity, including contact information and associated networks or domains.
8. **Entities Search by Function (`/entities?fn={name}`)**: Searches entities by a person or organization's name (e.g., `Test Person`). Outputs matching entities.
9. **Entities Search by Handle (`/entities?handle={handlePrefix}`)**: Searches entities by handle prefix (e.g., `TP137*`). Outputs entities with handles matching the prefix.
10. **Domains Search by Name (`/domains?name={domainPrefix}`)**: Searches domains by name or prefix (e.g., `203.in-addr*`). Outputs domains matching the name or prefix.
For specific details on the response structure and additional parameters each endpoint supports, it's best to refer to the official documentation or directly explore the RDAP service at [rdap.apnic.net](https://rdap.apnic.net).
