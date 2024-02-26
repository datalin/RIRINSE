openapi: 3.0.0
info:
  title: RDAP API
  description: This API allows for querying the Registration Data Access Protocol (RDAP) service for information about IP addresses, domain names, and autonomous system numbers.
  version: 1.0.0
servers:
  - url: https://rdap.apnic.net
    description: APNIC RDAP server
paths:
  /ip/{ipAddress}:
    get:
      operationId: getIpInformation
      summary: Get information about a specific IP address
      parameters:
        - name: ipAddress
          in: path
          required: true
          description: The IP address to query information about
          schema:
            type: string
            pattern: '^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$'
      responses:
        '200':
          description: Information about the IP address
          content:
            application/json:
              schema:
                type: object
                properties:
                  handle:
                    type: string
                  startAddress:
                    type: string
                  endAddress:
                    type: string
                  ipVersion:
                    type: string
                  name:
                    type: string
                  type:
                    type: string
                  country:
                    type: string
                required:
                  - handle
                  - startAddress
                  - endAddress
                  - ipVersion
                  - name
                  - type
                  - country
        '400':
          description: Bad request
        '404':
          description: IP address not found

