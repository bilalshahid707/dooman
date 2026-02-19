import { useState } from "react";
import { Box, FormControl, Input, Button, Typography, CircularProgress } from "@mui/joy";
import SendIcon from "@mui/icons-material/Send";
import axios from "axios";

export const Chat = ({ setScore, conversation_id }) => {
    const [messages, setMessages] = useState([]);
    const [input, setInput] = useState("");
    const [ended, setEnded] = useState(false);
    const [loading, setLoading] = useState(false);

    const handleSubmit = async (e) => {
        e.preventDefault();

        const userMsg = { role: "user", content: input };
        setMessages((prev) => [...prev, userMsg]);
        setInput("");
        setLoading(true);

        const { data } = await axios.post(`http://127.0.0.1:8000/api/v1/games`, {
            conversation_id,
            user_msg: input,
        });

        setMessages((prev) => [...prev, { role: "assistant", content: data.reply }]);
        setScore(data.progress);
        if (data.status === "ended") setEnded(true);
        setLoading(false)
    }


    return (
        <Box
            sx={{
                bgcolor: "#0F172A",
                height: "100vh",
                width: "100vw",
                display: "flex",
                flexDirection: "column",
            }}
        >
            <Box
                sx={{
                    flex: 1,
                    overflowY: "auto",
                    px: { xs: 2, sm: 4, md: 10 },
                    py: 3,
                    display: "flex",
                    flexDirection: "column",
                    gap: 2.5,
                }}
            >

                {messages.map((msg, i) => {
                    return (
                        <Box
                            key={i}
                            sx={{
                                display: "flex",
                                justifyContent: msg.role === "user" ? "flex-end" : "flex-start",
                                alignItems: "flex-end",
                                gap: 1,
                            }}
                        >

                            <Box sx={{ display: "flex", flexDirection: "column", gap: 0.5 }}>
                                <Typography
                                    sx={{
                                        fontSize: "11px",
                                        color: "#475569",
                                        px: 0.5,
                                        textAlign: msg.role === "user" ? "right" : "left",
                                    }}
                                >
                                    {msg.role === "user" ? "You" : "Arthur"}
                                </Typography>
                                <Box
                                    sx={{
                                        p: 2,
                                        bgcolor: msg.role === "user" ? "#3B82F6" : "#1E293B",
                                        border: msg.role === "user" ? "none" : "1px solid #263548",
                                    }}
                                >
                                    <Typography sx={{ color: "#F8FAFC", fontSize: "15px", lineHeight: 1.6 }}>
                                        {msg.content}
                                    </Typography>
                                </Box>
                            </Box>

                        </Box>
                    );
                })}
                {loading && (
                    <Box sx={{ display: "flex", alignItems: "flex-end", gap: 1 }}>
                        <Box
                            sx={{
                                px: 2, py: 1.5,
                                borderRadius: "18px 18px 18px 4px",
                                bgcolor: "#1E293B",
                                border: "1px solid #263548",
                                display: "flex",
                                gap: "4px",
                                alignItems: "center",
                            }}
                        >
                            <Typography>typing...</Typography>
                        </Box>
                    </Box>
                )}
            </Box>

            <Box
                component="form"
                onSubmit={handleSubmit}
                sx={{
                    p: 2,
                    borderTop: "1px solid #1E293B",
                    bgcolor: "#0F172A",
                }}
            >
                <FormControl sx={{ display: "flex", flexDirection: "row", gap: 1.5, alignItems: "center" }}>
                    <Input
                        value={input}
                        onChange={(e) => setInput(e.target.value)}
                        disabled={ended || loading}
                        sx={{
                            flex: 1,
                            p: 2,
                            fontSize: "15px",
                            color: "#F8FAFC",
                            bgcolor: "#020617",
                            border: "1px solid #1E293B",
                            borderRadius: "12px",
                        }}
                    />
                    <Button
                        type="submit"
                        disabled={ended || loading}
                        sx={{
                            width: 44, height: 44,
                            borderRadius: "12px",
                            bgcolor: "#3B82F6",
                            flexShrink: 0,
                        }}
                    >
                        <SendIcon sx={{ fontSize: 18 }} />
                    </Button>
                </FormControl>

            </Box>
        </Box>
    );
}
export default Chat