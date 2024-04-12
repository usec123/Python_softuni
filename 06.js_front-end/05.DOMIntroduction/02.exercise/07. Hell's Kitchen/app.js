function solve() {
   document.querySelector('#btnSend').addEventListener('click', onClick);

   function onClick () {
      const inputElement = document.querySelector('#inputs > textarea');
      const bestRestaurantElement = document.querySelector('#bestRestaurant > p');
      const bestWorkersElement = document.querySelector('#workers > p');
      const sum = a => a.reduce((a, v) => a + v.salary, 0);
      const averageSum = a => sum(a) / a.length;

      let register = {};

      for (const row of JSON.parse(inputElement.value)) {
          let [restaurant, employees] = [row.split(' - ')[0], row.split(' - ')[1].split(', ')];

          if (!register[restaurant]) {
              register[restaurant] = [];
          }

          employees
              .map(e => ({name: e.split(' ')[0], salary: Number(e.split(' ')[1])}))
              .forEach(e => register[restaurant].push(e));
      }

      const sorted = Object
          .entries(register)
          .sort((a, b) => sum(b[1]) - sum(a[1]))
          .map(([r, e]) => [r, e.sort((a, b) => b.salary - a.salary)]);

      const bestName = sorted[0][0];
      const bestAverage = averageSum(sorted[0][1]).toFixed(2);
      const bestMax = sorted[0][1][0].salary.toFixed(2);

      const bestRestaurant = `Name: ${bestName} Average Salary: ${bestAverage} Best Salary: ${bestMax}`;
      const bestEmployees = sorted[0][1].map(w => `Name: ${w.name} With Salary: ${w.salary}`);

      bestRestaurantElement.textContent = bestRestaurant;
      bestWorkersElement.textContent = bestEmployees.join(' ');
      
   }
}
