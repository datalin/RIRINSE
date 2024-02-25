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

## [Basic Building Blocks](Building%20Blocks/README.md)

A collection of basic tools to manipulate the data.

# Cross-RIR resource disposition analysis: The delegated files.

The RIR all produce a daily statistics file called the 'delegated' statistics file or 'stats file', and a combined file is produced by the NRO. This process records the disposition of resources under each RIR. However, there are many ways to analyse this data, and combine it with information like the inter-RIR transfer log, the state of BGP, Resource Certification data, economic and geographic data. Some things are explicit, but others have to be inferred, for example the way different BGP speakers announce resources which are derived under different RIR policies or combine resources from several RIR and NIR. Or, the relationship of this data to GDP and Internet users.

The goal of this topic is to explore the kinds of 'business intelligence' (BI) which can be derived from this data and look at how we can improve understanding of where resources are delegated, and how they are being used. If you are comfortable writing code, there are jobs which may be a good fit for your choice of language. If you are not a coder, but comfortable in spreadsheets like Excel then there will be work to do here building spreadsheet friendly data and outcomes, and if you aren't comfortable in code or spreadsheets, then there are documentation and what-if and other tasks which could be done like charting and graphing, making this topic ideal for anyone who isn't a programmer. The goal is to improve understanding of how Internet Number Resources are being used and distribute into the world.

References:

https://www.nro.net/about/rirs/statistics/
https://www.routeviews.org/routeviews/
https://rex.apnic.net/

## [Why](Why/README.md)

An exploration of the motivations to solve this suite of problems.

- One of the problems is we get to see the delegation but not the disposition of an IP Address.

# [Cross-RIR Resource Disposition Analysis](Example-Code/README.md)

This repository contains a Python script for analyzing Cross-RIR resource disposition data by @shankarganesh.pj. The script fetches data from various sources such as the NRO statistics page, RouteViews, and REX (Resource Certification), parses the data, and performs basic analysis.

## License

This project is licensed under the MIT.
