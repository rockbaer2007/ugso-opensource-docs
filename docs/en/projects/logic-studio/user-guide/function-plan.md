# Function plan

## First example

Add a digital input and output to a new plan. Connect their pins, start the simulation and toggle the input. The output should follow.

The canvas shows the connected blocks and a minimap in the lower right.

![Function plan with connected blocks and a minimap](/images/logic-studio/0.1.8-react-flow-193.jpg)

## Features

### Canvas

Drag, move and connect blocks. Zoom or fit the whole plan.

### Parameters

Select a block to set a timer duration or counter target.

### HA bindings

Choose an entity for the signal and an approved HA action for the output.

### Simulation

Toggle inputs and follow signal values at the pins.

### Breakpoint and single step

Pause and advance one scan to inspect the values.

### Auto layout and pinning

Arrange the plan while keeping pinned blocks in place.

### Play and live diagnostics

Start the saved plan and inspect live values and errors.

### Persistent counters and latches

Enable storage to keep values across app restarts. Editing the plan can reset them.

## If something goes wrong

If a connection is refused, compare the types of its pins.
