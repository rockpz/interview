console.log(require.cache);

const a = require('http')

console.log(process.moduleLoadList);

const b = require('./test2')

console.log(process.moduleLoadList);

async function foo() {
    await bar();
    return 42;
  }
  
  async function bar() {
    await Promise.resolve();
    throw new Error('BEEP BEEP');
  }

  //for(var i = 0; i < 10; i++) {
  //  setTimeout(function() {
  //    console.log(i);//连续输出10个i，而不是1,2,3...10
  //  }, 0);
  //}

  //for(let j = 0; j < 10; j++) {
  //  setTimeout(function() {
  //    console.log(j);//连续输出10个i，而不是1,2,3...10
  //  }, 0);
  //}
  
  foo().catch(error => console.log(error.stack));

  for(let i = 0; i < 10; i++) {
    console.log(i);
  }
  