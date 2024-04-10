solve = (arr) => console.log(arr.filter(x => x%2===0).reduce((sum, num) => sum + num, 0) - arr.filter(x => x%2!==0).reduce((sum, num) => sum + num, 0))

solve([1,2,3,4,5,6])