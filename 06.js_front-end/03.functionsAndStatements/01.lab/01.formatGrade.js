function solve(grade) {
    console.log((grade<3?'Fail':
    grade<3.5?'Poor':
    grade<4.5?'Good':
    grade<5.5?'Very good':'Excellent')
    + ` (${grade<3?2:grade.toFixed(2)})`);
}

solve(3.33)
solve(4.50)
solve(2.99)