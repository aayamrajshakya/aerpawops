# OEO Requirements

### OEO Server

- The OEO Server shall not contain a monolithic process capable of bottlenecking the OEO
- There shall be a single OEO Server per experiment
- The OEO Server shall support up to **100** connected agents of any type
- The OEO Server shall support up to **20** connected consoles
- Shall communicate with every portable, fixed, and cloud node via the OEO Agents
- Shall report the status of the connection with every node

### OEO Agents

- There shall be a set of defined topics for all OEO Agents to use
  - Every topic shall be limited in scope to a subset of related information
  - The list of topics shall include
    - Node health
    - Radio information
    - Vehicle Information
- There shall be a set of defined helper processes to run on each OEO agent
  - Each helper shall correspond one-to-one with a single defined topic
  - This list of helpers shall include
    - Computer helper
    - Vehicle helper
      - The vehicle helper connects the agent to MAVLink and provides the data for the agent to publish
    - Radio helper
- Each OEO Agent shall communicate over a subset of the defined topics depending on the type of compute node
  - i.e. a portable node agent shall use the node health, radio information, and vehicle information topics, but a cloud node would only use the node health topic.
- Each OEO Agent shall communicate with a helper process for every topic that it uses
- Shall receive commands from connected OEO Consoles
  - Shall send commands to the appropriate helper process to be executed on the agent

### OEO Console

- The OEO Console shall be able to display the most recent data from every connected agent
  - The OEO Console shall be able to display any data received without requiring a data formatter or handler
- The OEO Console shall be able to display events and/or state changes of the agents
  - The events to display shall be specified before runtime
    - i.e. monitor the connection status of each agent and display a message when it changes
- There shall be a distinction between read-only and command OEO Consoles
- An OEO Command Console shall be able to send commands to any subset of the connected agents
- Both a command and read-only OEO Console shall be able to be configured to display any subset of the data from each agent

### MAVLink Inspector

- There shall be a MAVLink inspector that when connected to a MAVProxy shall be able to display any message from any of the vehicles
- The MAVLink Inspector shall be capable of sending commands to a node connected over MAVLink
