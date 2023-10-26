require("dotenv").config();
const express = require("express");
const cors = require("cors");
const OpenAI = require("openai");

let PORT = process.env.PORT || 8000;
const apiKey = process.env.APIKEY;

const openai = new OpenAI({
    apiKey: apiKey,
});


const app = express();

app.use(express.json());
app.use(cors());
app.use(express.static('public'));

app.post('/get-data', async (req, res) => {
    const userInput = req.body.input;
    const type = req.body.type;

    const response = await openai.chat.completions.create({
        messages: [
            { role: "system", content: `You are a ${type} generator.` },
            { role: "user", content: `Generate a ${type} about ${userInput}.` },
        ],
        model: "gpt-3.5-turbo",
    });

    res.status(200).send({ response: response.choices[0].message.content });
});


app.get("/", (req, res) => {
    res.status(200).json({ message: "Welcome to Data-Generator-AI" });
});

app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});
