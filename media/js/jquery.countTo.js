/**
 * countdown timer with some configuration
 *
 * @version 0.1
 * @url http://jsfiddle.net/KzrwQ/1/
 * @date 2011/09/02
 * @author Conrad 'bartrail' Barthelmes
 * @licence MIT
 *
 * usage:
 *
 * $('selector').countTo({
 *   interval:    1000,                             // miliseconds the interval is repeated (aka speed)
 *   startNumber: 10,                               // start from 10 or any other integer
 *   endNumber:   0,                                // end at 0 or any other integer
 *
 *   onLoop:      function(self, current, loop) {   // fired on every loop
 *     self;      // the fetched element
 *     current;   // current number of interval
 *     loop;      // finished loops
 *
 *     // default behaviour:
 *     $(self).text(current);
 *   },
 *
 *   onStart:     function(self) {                  // fired on the beginning
 *     self;      // the fetched element
 *   },
 *
 *   onFinish:    function(self, current, loop) {   // fired when finished
 *     self;      // the fetched element
 *     current;   // current number of interval
 *     loop;      // finished loops
 *   }
 * });
 *
 */
jQuery.fn.countTo = function(options) {
  if(this.length == 0) {
    return;
  }
  // save reference to self
  var self     = this;
  // merge optoins
  self.options = {};
  jQuery.extend(true, self.options, {
    interval   : 1000,
    startNumber: 10,
    endNumber  : 0,
    onLoop     : function(self, current, loop) {
      $(self).text(current);
    },
    onStart    : function(self) {},
    onFinish   : function(self, current, loop) {}
  }, options);

  // init the start number
  self.current   = self.options.startNumber;
  // get the direction, true is 'down', false is 'up'
  self.direction = self.options.startNumber > self.options.endNumber ? true : false;
  // the current iteration
  self.loop      = 0;
  // whether is finished or not
  self.finished  = false;
  // the timing function
  self.timer     = function(self) {
    self.intervalId = setInterval(self._interval, self.options.interval)
  }

  self._interval  = function() {
    self.options.onLoop(self, self.current, self.loop);
    // going down
    if(self.direction) {
      if(self.current > self.options.endNumber) {
        self.current--;
      }else{
        self.finished = true;
      }
    // going up
    }else{
      if(self.current < self.options.endNumber) {
        self.current++;
      }else{
        self.finished = true;
      }
    }
    // clear interval and fire onFinish when finished
    if(self.finished) {
      clearInterval(self.intervalId);
      self.options.onFinish(self, self.current, self.loop)
    }
    self.loop++;
  }

  self.start = function(self) {
    self.options.onStart(self);
    self.timer(self);
  }

  self.start(self);
}
