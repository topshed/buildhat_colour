# A simple LEGO colour sampling machine using the Raspberry Pi Build HAT


![movie](https://github.com/topshed/buildhat_colour/blob/7c69015628dbc5df3aef1e249e96c1bb1a234ed8/buildhat_colour.gif)

## Top down view of build

![top down view](https://github.com/topshed/buildhat_colour/blob/b4d9d36dfabf842709cc0f020f60fca0ed6302b1/topview.jpg)

## Side view of build

![side view](https://github.com/topshed/buildhat_colour/blob/151cfd0fcb642c215ad81393eb3110bedd596a25/sideview.jpg)

## Python program

A simple Python program that controls this build is [here](https://github.com/topshed/buildhat_colour/blob/b86d93e243a6c490e6a19651b153c2b1ab68b65a/colour_sampler_basic.py). When the forcesensor, which acts as a button, is pressed, the carousel rotates 90 degrees and the colour sensor tries to detect the colour of the bricks. The colour is returned as a string, which is passed directly to the LED matrix, setting all pixels. 

Built HAT Python library documentation is [here](https://buildhat.readthedocs.io/en/latest/buildhat/index.html#library)

## Challenges

- Adjust the positioning of the sample blocks so that the colour sensor detects lighter colours correctly
- Modify the program so that it uses `get_color_rgbi()` to make better decisions about what colour it has seen
- Build a machine to sort bricks based on their colour
