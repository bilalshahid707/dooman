import { useState } from "react";
import { Chat } from "./pages/chat"
import { ProgressMeter } from "./components/ProgressMeter"
import { StartGame } from "./pages/startGame";
import { Box } from "@mui/joy";
const App = () => {

  const [conversationId, setConversationId] = useState()
  const [score, setScore] = useState(0)

  return (
    <main style={{ position: 'relative' }}>

      {conversationId ? <>
        <Box sx={{ display: 'flex', flexDirection: "column", gap: 24 }} >
          <ProgressMeter score={score} />
          <Chat setScore={setScore} conversation_id={conversationId} />
        </Box>
      </> : <StartGame setConversationId={setConversationId} />}

    </main>
  );
};

export default App;
