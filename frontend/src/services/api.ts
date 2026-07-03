import axios from "axios";

const api = axios.create({
  baseURL:
    import.meta.env.VITE_API_URL ||
    "http://localhost:8000",
});

export default api;

export const askAI = async (question: string) => {

    const response = await api.post("/ai/query", {
        question: question,
    });

    return response.data;
};