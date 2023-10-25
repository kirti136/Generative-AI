require("dotenv").config();
const express = require("express");
const app = express();
const PORT = process.env.PORT || 8000;
const cors = require("cors");
const OpenAI = require("openai");
const apiKey = process.env.APIKEY;

const openai = new OpenAI({
  apiKey: apiKey,
});

app.use(express.json());
app.use(cors());
app.use(express.static("frontend"));

app.get("/", (req, res) => {
  res.status(200).json({ message: "Welcome to Code-Converter-App" });
});

app.post("/convert-code", async (req, res) => {
  try {
    // Retrieve user-provided code and target language from the request
    const { code, targetLanguage } = req.body;

    // Use the openai library to send a prompt to GPT-3 for code conversion
    const response = await openai.chat.completions.create({
      messages: [
        {
          role: "system",
          content:
            "You are a Developer who has knowledge of all computer languages",
        },
        {
          role: "user",
          content: `Convert the following code from ${code} to ${targetLanguage}.`,
        },
      ],
      model: "gpt-3.5-turbo",
    });

    // Extract the converted code from the GPT-3 response
    const convertedCode = response.choices[0].message.content;
    console.log(convertedCode);

    // Send the converted code back to the frontend
    res.json({ convertedCode });
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: "Conversion failed" });
  }
});

app.post("/debug-code", async (req, res) => {
  try {
    // Retrieve user-provided code from the request
    const { code } = req.body;

    // Use the openai library to send a prompt to GPT-3 for code debugging
    const response = await openai.chat.completions.create({
      messages: [
        {
          role: "system",
          content:
            "You are a Developer who has knowledge of all computer languages",
        },
        {
          role: "user",
          content: `Debug the following code:\n${code}.\nPlease debug the following code and provide a corrected version explaining the issues and the fixes made.\n `,
        },
      ],
      model: "gpt-3.5-turbo",
    });

    // Extract the debugged code from the GPT-3 response
    const debuggedCode = response.choices[0].message.content;

    // Send the debugged code back to the frontend
    res.json({ debuggedCode });
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: "Debugging failed" });
  }
});

app.post("/quality-check", async (req, res) => {
  try {
    // Retrieve user-provided code from the request
    const { code } = req.body;

    // Use the openai library to send a prompt to GPT-3 for code quality checking
    const response = await openai.chat.completions.create({
      messages: [
        {
          role: "system",
          content:
            "You are a Developer who has knowledge of all computer languages",
        },
        {
          role: "user",
          content: `Check the quality of the following code:\n${code}. \nPlease evaluate the following code for its quality and provide a score in percentage (max 100%) for each of the following factors. \nAdditionally, provide explanations or comments on the code's adherence to the following aspects:
                    \n1. Code Consitency : Provide percentage based on the provided code
                    \n2. Code Performance : Provide percentage based on the provided code
                    \n3. Error Handling : Provide percentage based on the provided code
                    \n4. Code Readability : Provide percentage based on the provided code
                    \n5. Code Complexity : Provide percentage based on the provided code`,
        },
      ],
      model: "gpt-3.5-turbo",
    });

    // Extract the quality assessment from the GPT-3 response
    const qualityAssessment = response.choices[0].message.content;

    // Send the quality assessment back to the frontend
    res.json({ qualityAssessment });
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: "Quality check failed" });
  }
});

app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
