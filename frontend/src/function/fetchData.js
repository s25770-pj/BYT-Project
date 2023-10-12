import apiConfig from '@/data/request.js';

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
   
      const data = await import(`@/data/user/${endpoint}`);
      return data.default;
  }
};
