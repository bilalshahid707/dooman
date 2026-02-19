import { Box, Button, Typography } from "@mui/joy";
import axios from "axios";

export const StartGame = ({ setConversationId }) => {

    const handleClick = async () => {
        const response = await axios.post(`https://dooman-production.up.railway.app/api/v1/conversations/`)
        setConversationId(response.data.id)
    }

    return (
        <Box
            sx={{
                bgcolor: "#0F172A",
                height: "100vh",
                width: "100vw",
                display: "flex",
                alignItems: "center",
                justifyContent: "center",
                flexDirection: "column",
                gap: 3,
            }}
        >

            <Typography sx={{ fontSize: 44, lineHeight: 1 }}>🚪</Typography>
            <Box sx={{ textAlign: "center", display: "flex", flexDirection: "column", gap: 0.75 }}>
                <Typography
                    level="h2"
                    sx={{ color: "#F8FAFC", fontWeight: 700, letterSpacing: "-0.02em" }}
                >
                    The Golden Palm
                </Typography>
                <Typography
                    level="body-sm"
                    sx={{ color: "#64748B", fontStyle: "italic" }}
                >
                    Dubai's most exclusive nightclub. Can you get in?
                </Typography>
            </Box>
            <Button
                size="lg"
                onClick={handleClick}
                sx={{
                    mt: 1,
                    px: 4,
                    bgcolor: "#6366F1",
                    color: "#fff",
                    borderRadius: "12px",
                    fontWeight: 600,
                    fontSize: "15px",
                }}
            >
                Start Game →
            </Button>

        </Box>
    );
}

export default StartGame