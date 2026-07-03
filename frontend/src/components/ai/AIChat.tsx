import { useState } from "react";
import { askAI } from "../../services/api";
import { Bot, User, Send } from "lucide-react";

export default function AIChat() {
    const [question, setQuestion] = useState("");
    const [answer, setAnswer] = useState("");
    const [loading, setLoading] = useState(false);

    const handleAsk = async () => {
        if (!question.trim()) return;

        try {
            setLoading(true);

            const res = await askAI(question);

            setAnswer(res.answer);
        } catch {
            setAnswer("Unable to get AI response.");
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="space-y-5">

            <h2 className="text-xl font-bold flex items-center gap-2">
                <Bot className="text-blue-600" />
                AI Assistant
            </h2>

            <textarea
                rows={4}
                value={question}
                onChange={(e) => setQuestion(e.target.value)}
                placeholder="Ask anything about delivery ETA..."
                className="w-full rounded-lg border p-3 resize-none"
            />

            <button
                onClick={handleAsk}
                disabled={loading}
                className="flex items-center gap-2 bg-blue-600 hover:bg-blue-700 text-white px-5 py-2 rounded-lg disabled:opacity-50"
            >
                <Send size={18} />
                {loading ? "Thinking..." : "Ask AI"}
            </button>

            {question && (
                <div className="bg-blue-50 rounded-xl p-4">

                    <div className="flex gap-2 items-center mb-2">

                        <User size={18} />

                        <strong>You</strong>

                    </div>

                    <p>{question}</p>

                </div>
            )}

            {answer && (
                <div className="bg-gray-100 rounded-xl p-4">

                    <div className="flex gap-2 items-center mb-2">

                        <Bot
                            size={18}
                            className="text-blue-600"
                        />

                        <strong>AI Assistant</strong>

                    </div>

                    <p className="leading-7">

                        {answer}

                    </p>

                </div>
            )}

        </div>
    );
}