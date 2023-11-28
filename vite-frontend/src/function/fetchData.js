import apiConfig from '@/data/request.js';

async function loadData(endpoint) {
  const module = require(`@/data/user/${endpoint}`);
  return module.default;
}
export const fetchDataFromEndpoint = async (method, endpointKey) => {
  const mode = "development";
  const endpoint = apiConfig.endpoints[method][endpointKey][mode];

  if (!endpoint) {
    throw new Error('Wrong endpoint');
  }

  if (mode === "production") {
    const response = await fetch(endpoint);

    if (response.ok) {
      return response.json();
    } else {
      throw new Error('Błąd pobierania danych');
    }
  } else {
    return new Promise((resolve) => {
      setTimeout(async () => {
        loadData(endpoint);
        const data = await loadData(endpoint);
        resolve(data.default);
      }, 3000);
    });
  }
};



