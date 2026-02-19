import { Box, Typography, Chip } from "@mui/joy";

export const ProgressMeter = ({ score }) => {
    console.log(score)
    let color, label;
    if (score < 0) {
        color = "danger"; label = "You lost the game";
    } else if (score < 49) {
        color = "warning"; label = "Keep going...";
    } else if (score >= 50) {
        color = "success"; label = "You won the game!";
    }

    return (
        <Box
            sx={{
                position: "absolute",
                top: 16,
                left: "50%",
                transform: "translateX(-50%)",
                bgcolor: "white",
                p: 2,
                width: "240px",
                display: "flex",
                flexDirection: "column",
                gap: 1.5,
            }}
        >

            <Box sx={{ display: "flex", justifyContent: "space-between", alignItems: "center" }}>
                <Typography level="title-sm" sx={{ color: "text.primary" }}>
                    Influence Meter
                </Typography>
                <Typography
                    level="body-sm"
                    sx={{ fontFamily: "monospace", color: `${color}`, fontWeight: 600 }}
                >
                    {score || 0} / 100
                </Typography>
            </Box>

            <Chip
                size="sm"
                color={color}
                variant="soft"
                sx={{ alignSelf: "flex-start", fontWeight: 500 }}
            >
                {label}
            </Chip>
        </Box>
    );
};

export default ProgressMeter;