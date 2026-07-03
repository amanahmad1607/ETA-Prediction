import axios from "axios";

const api = axios.create({
    baseURL: "http://127.0.0.1:8000",
    headers:{
        "Content-Type":"application/json"
    }
});

export default api;

export const askAI = async (question: string) => {

    const response = await api.post("/ai/query", {
        question: question,
    });

    return response.data;
};