## Yu Liu (Leosssss) (7/15P)

### 1 DIPPID Sender (2/5P)

 * format not compatible to DIPPID **(-0.5)**
   * the tuple in the message does not work - I had to replace it with a dictionary. Looks like you did not test the program?
 * wrong names for capabilities ("accelerometer" and "button_1" were required) **(-0.5)**
 * accelerometer **(-0.5)**
   * x always increasing, y is fine
   * only one axis of the sensor is simulated
 * button
   * button message only printed, not sent **(-1)**
 * code looks ok
 * why does the frequency increase? this will lead to exteremely high frequencies when the program runs for a while. **(-0.5)**


### 2 2D Game (5/10P)

 * game implementation **(1/3)**
   * this is the hardest game of tetris I have ever played
   * pieces can not be rotated
   * the game does not end when the top is reached
   * completed lines don't vanish
   * the game crashes instantly when no DIPPID sender is running
   * I give you one point for implementing the logic of the pieces falling down and colliding with each other
 * DIPPID input **(2/2)**
   * I can move the pieces by tilting the device
 * code quality **(0.5/2)**
   * code is very convoluted and looks redundant at many places
   * lots of magic numbers
   * having to change/extend this code seems like a nightmare
   * I give you half a point for using some constants and naming variables and functions appropriately
 * interaction technique **(0.5/1)**
   * it is not possible to send the pieces straight down **(-0.5)**
 * look of the game **(0.5/1)**
   * colorful pieces
   * very minimalistic **(-0.5)**
   * no score, no game over screen, no preview for the next piece
 * venv **(0.5/1)**
   * there is a venv that seems to contain correct packages
   * no requirements.txt **(-0.5)**
