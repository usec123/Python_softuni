function solve() {
  const text = document.getElementById('input').value.split('.');
  const output = document.getElementById('output');
  let res = text.filter(x=>x).reduce((res, txt, i) => {
    const resIndex = Math.floor(i/3);
    if (!res[resIndex]) res[resIndex] = []
    res[resIndex].push(txt.trim());
    return res;
  }, []);
  console.log(res);
  res = res.map(x => `<p>${x.join('. ')}.</p>`)
  output.innerHTML = res;
}