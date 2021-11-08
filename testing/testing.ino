#include "FastLED.h"

short getId(short x, short y)
{
  x = 31 - x;

  short id = 0;

  id += 8 * x;
  if (x % 2 == 1)
  {
    id += y;
  } else {
    id += 7 - y;
  }

  return id;
}

CRGB leds[256];
void setup() {
  FastLED.addLeds<WS2811, 3, GRB>(leds, 256);
}
short x = 0;
short y = 0;
void loop() {
  leds[getId(x, y)] = CRGB::Black;
  if (++x > 31) {x = 0; if (++y > 7) {y = 0;}}
  leds[getId(x, y)] = CRGB::Green;
  FastLED.show();
  delay(20);
}
