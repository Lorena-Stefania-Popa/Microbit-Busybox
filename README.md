# Microbit-Busybox

The commands supported by the mini-busybox application are:

1. led [parameter] x y - controls the LED on the Micro: bit located on the x line and the y column. Depending on the parameters you receive the order will perform the following actions:

  1.1. on - illuminates the LED
  
  1.2. off - turns off the LED
  
  1.3. blink <interval> <count> - causes the LED to flash at the interval millisecond count times. The value for the count will be in the range 0-20.
  
  1.4. toggle - brings the LED to the opposite state (if the LED is on, turns it off, and if it is off, turns it on)
  
  1.5. brightness [set <val>] - used without the set parameter, displays the brightness of the specified LED
  
  1.5.1. set <val> - if the set parameter is used, the brightness will be set to the wave value, somewhere the wave is an integer 0-9, and the value displayed in the console is the new brightness

The command will display the following errors for the following cases:

Invalid LED. - if the values for x and / or y are not in the range 0-4.
  
Invalid count value. - if the value for the count is not in the range 0-20.
  
Invalid brightness. - if the value for the wave is outside the range 0-9.
  
  I also created various linux commands: mv, cp, ls, echo, rm.
