# RIRINSE-APNIC57

RIRINSE-APNIC57 is a team project at the APNIC57 Hackathon to explore the RIR internet number resources (INR) data and how to relate it to other sources of information.

The kinds of problems it is looking at:

 * How to identify where resources are delegated
   * Where are the resources bought from?
   * Which country is acquiring these resources ?
   * In which country are the resouces being sold to / or used ? E.g: BD buys and IP block & is listed under Ireland but being used in Thailand.   
 * How to identify where resources are being used - The "Geolocation" problem
 * How to correlate the resources between different information sources
   * centralized display of resource distribution amoungst all RIRs (with different time zones)
   * Geofeed, Maxmind, caida, Internet Health Report.
*What time in APNIC GMT can represent all collected data from yesterday?  

## [Basic Building Blocks](Building%20Blocks/README.md)

A collection of basic tools to manipulate the data.

## [The delegated files](delegated-files/README.md).

The RIR all produce a daily statistics file called the 'delegated' statistics file or 'stats file'


## [Why](Why/README.md)

An exploration of the motivations to solve this suite of problems.

- One of the problems is we get to see the delegation but not the disposition of an IP Address.

# Cross-RIR Resource Disposition [Analysis](Example-Code/README.md)

This repository contains a Python script for analyzing Cross-RIR resource disposition data by @shankarganesh.pj. The script fetches data from various sources such as the NRO statistics page, RouteViews, and REX (Resource Certification), parses the data, and performs basic analysis.

## License

This project is licensed under the MIT.
