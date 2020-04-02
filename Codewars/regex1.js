import js2py

# there are 2 easy methods to run js file from Js2Py

# Method 1:
eval_result, example = js2py.run_file('example.js')

  
js2py.translate_file('regex1.js', 'translated.py')
#this translates and 
#saves equivalent Py file from example import example # yes, it is: 
#import lib_name from lib_name

const solution = 
/^(((((((0+)?1)1)((10*1)1)*(((10*1)0)0)|((((0+)?1)0)0))((01)((10*1)1)*(((10*1)0)0)|((00|1)0))*((01)((10*1)1)*(((10*1)0)1)|((00|1)1))|((((0+)?1)1)((10*1)1)*(((10*1)0)1)|((((0+)?1)0)1)))((0((10*1)1)*(((10*1)0)0)|1)((01)((10*1)1)*(((10*1)0)0)|((00|1)0))*((01)((10*1)1)*(((10*1)0)1)|((00|1)1))|(0((10*1)1)*(((10*1)0)1)))*((0((10*1)1)*(((10*1)0)0)|1)((01)((10*1)1)*(((10*1)0)0)|((00|1)0))*((01)((10*1)1)*0)|(0((10*1)1)*0))|(((((0+)?1)1)((10*1)1)*(((10*1)0)0)|((((0+)?1)0)0))((01)((10*1)1)*(((10*1)0)0)|((00|1)0))*((01)((10*1)1)*0)|((((0+)?1)1)((10*1)1)*0)))(0((0((10*1)1)*(((10*1)0)0)|1)((01)((10*1)1)*(((10*1)0)0)|((00|1)0))*((01)((10*1)1)*(((10*1)0)1)|((00|1)1))|(0((10*1)1)*(((10*1)0)1)))*((0((10*1)1)*(((10*1)0)0)|1)((01)((10*1)1)*(((10*1)0)0)|((00|1)0))*((01)((10*1)1)*0)|(0((10*1)1)*0))|1)*(0((0((10*1)1)*(((10*1)0)0)|1)((01)((10*1)1)*(((10*1)0)0)|((00|1)0))*((01)((10*1)1)*(((10*1)0)1)|((00|1)1))|(0((10*1)1)*(((10*1)0)1)))*((0((10*1)1)*(((10*1)0)0)|1)((01)((10*1)1)*(((10*1)0)0)|((00|1)0))*((01)((10*1)1)*(1(0+)?))|(0((10*1)1)*(1(0+)?))))|((((((0+)?1)1)((10*1)1)*(((10*1)0)0)|((((0+)?1)0)0))((01)((10*1)1)*(((10*1)0)0)|((00|1)0))*((01)((10*1)1)*(((10*1)0)1)|((00|1)1))|((((0+)?1)1)((10*1)1)*(((10*1)0)1)|((((0+)?1)0)1)))((0((10*1)1)*(((10*1)0)0)|1)((01)((10*1)1)*(((10*1)0)0)|((00|1)0))*((01)((10*1)1)*(((10*1)0)1)|((00|1)1))|(0((10*1)1)*(((10*1)0)1)))*((0((10*1)1)*(((10*1)0)0)|1)((01)((10*1)1)*(((10*1)0)0)|((00|1)0))*((01)((10*1)1)*(1(0+)?))|(0((10*1)1)*(1(0+)?)))|(((((0+)?1)1)((10*1)1)*(((10*1)0)0)|((((0+)?1)0)0))((01)((10*1)1)*(((10*1)0)0)|((00|1)0))*((01)((10*1)1)*(1(0+)?))|((((0+)?1)1)((10*1)1)*(1(0+)?)|(0(0+)?)))))$/;

// Testing
const assert = require('./common/test');

const test = num => {
  assert(solution.test(num.toString(2)), num % 7 === 0);
};

test(7); // true
test(14); // true
test(20); // false