function getHeroIdFromUrl(): number | null {
    const params = new URLSearchParams(window.location.search);
    const id = params.get("id");
    return id ? parseInt(id) : null;
  }
  
  async function fetchHeroById(id: number) {
    try {
      const response = await fetch(`/api/heroes/${id}`);
      if (!response.ok) throw new Error("Hero not found");
      return await response.json();
    } catch (error) {
      console.error("Failed to fetch hero:", error);
    }
  }
  
  function displayHero(hero: any) {
    const img = document.getElementById("hero-image") as HTMLImageElement;
    const name = document.getElementById("hero-name")!;
    const role = document.getElementById("hero-role")!;
    const desc = document.getElementById("hero-description")!;
  
    img.src = hero.imageUrl;
    name.textContent = hero.name;
    role.textContent = `Roles: ${hero.roles.join(", ")}`;
    desc.textContent = `Win Rate: ${hero.winRate.toFixed(2)}% | Pick Rate: ${hero.pickRate.toFixed(2)}%`;
  }
  
  (async () => {
    const heroId = getHeroIdFromUrl();
    if (!heroId) {
      alert("Hero ID not found in URL.");
      return;
    }
  
    const hero = await fetchHeroById(heroId);
    if (hero) displayHero(hero);
  })();
  