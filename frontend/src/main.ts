const apiBase = 'http://127.0.0.1:5000/api';

async function fetchPopularHeroes() {
  const res = await fetch(`${apiBase}/heroes`);
  const heroes = await res.json();
  const container = document.getElementById('popular-heroes')!;
  container.innerHTML = '';

  heroes.slice(0, 5).forEach((hero: any) => {
    const card = document.createElement('div');
    card.className = 'card';
    card.innerHTML = `
      <h4>${hero.name}</h4>
      <img src="${hero.image_url}" width="100" />
      <p>Win Rate: ${hero.win_rate}%</p>
      <p>Pick Rate: ${hero.pick_rate}%</p>
    `;
    container.appendChild(card);
  });
}

async function fetchStatistics() {
  const res = await fetch(`${apiBase}/statistics`);
  const stats = await res.json();

  const winRate = [...stats].sort((a, b) => b.win_rate - a.win_rate)[0];
  const pickRate = [...stats].sort((a, b) => b.pick_rate - a.pick_rate)[0];

  document.getElementById('highest-win-rate')!.innerHTML = `
    <h4>Highest Win Rate</h4>
    <p>Hero ID: ${winRate.hero_id}</p>
    <p>Win Rate: ${winRate.win_rate}%</p>
  `;

  document.getElementById('most-picked')!.innerHTML = `
    <h4>Most Picked</h4>
    <p>Hero ID: ${pickRate.hero_id}</p>
    <p>Pick Rate: ${pickRate.pick_rate}%</p>
  `;
}

async function fetchMatchups() {
  const res = await fetch(`${apiBase}/matchups`);
  const matchups = await res.json();
  const best = matchups.sort((a, b) => b.advantage_percent - a.advantage_percent)[0];

  document.getElementById('best-counter-picks')!.innerHTML = `
    <h4>Best Counter Picks</h4>
    <p>${best.hero_id_a} > ${best.hero_id_b}</p>
    <p>Advantage: ${best.advantage_percent}%</p>
  `;
}

fetchPopularHeroes();
fetchStatistics();
fetchMatchups();
