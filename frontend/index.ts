const heroContainer = document.getElementById("hero-container");

fetch("http://localhost:5000/api/heroes")
  .then(res => {
    if (!res.ok) throw new Error("Failed to fetch heroes");
    return res.json();
  })
  .then((heroes) => {
    if (!heroContainer) return;
    heroContainer.innerHTML = ""; // очищаємо

    for (const hero of heroes) {
      const heroCard = document.createElement("div");
      heroCard.className = "hero-card";
      heroCard.innerHTML = `
        <img src="${hero.image_url}" alt="${hero.name}" />
        <h3>${hero.name}</h3>
        <p>Win rate: ${hero.win_rate}%</p>
        <p>Pick rate: ${hero.pick_rate}%</p>
      `;
      heroContainer.appendChild(heroCard);
    }
  })
  .catch(err => {
    if (heroContainer) {
      heroContainer.innerHTML = "Failed to load heroes 😞";
    }
    console.error(err);
  });
