require("dotenv").config()
const express = require('express');
const axios = require('axios');
const { MongoClient } = require('mongodb');
const collectionName = 'github_repositories';
const cors = require("cors")
const app = express();
const port = process.env.port || 8000;
const mongoUrl = 'mongodb://127.0.0.1:27017/';
// Initialize the MongoDB client
const client = new MongoClient(mongoUrl);
// console.log(client);
const repositoryModel = {
    id: Number,
    name: String,
    html_url: String,
    description: String,
    created_at: Date,
    open_issues: Number,
    watchers: Number,
    owner: {
        id: Number,
        avatar_url: String,
        html_url: String,
        type: String,
        site_admin: Boolean,
    },
};

app.use(express.json());
app.use(cors())
app.use((err, req, res, next) => {
    console.error(err);
    res.status(500).json({ error: 'Internal server error' });
});

app.get("/", (req, res) => {
    res.send("Welcome to Github Data Application")
})

function validateRepositoryData(repository) {
    for (const key in repositoryModel) {
        if (typeof repository[key] !== typeof repositoryModel[key]) {
            return false;
        }
    }
    return true;
}

async function saveDataToMongo(data) {
    try {
        // Connect to the MongoDB database
        await client.connect();
        const db = client.db('githubdata');
        // console.log(db);
        const collection = db.collection(collectionName);
        // console.log("COLLECTION", collection.s.namespace.collection);
        // const collection = collectionData.s.namespace.collection

        for (const repository of data) {
            const existingRepo = await collection.findOne({ id: repository.id });

            if (existingRepo) {
                await collection.updateOne({ id: repository.id }, { $set: repository });
            } else {
                if (validateRepositoryData(repository)) {
                    await collection.insertOne(repository);
                }
            }
        }

        console.log('Data saved to MongoDB.');
    } catch (error) {
        console.error('Error saving data to MongoDB:', error);
    } finally {
        await client.close();
    }
}

app.get('/github', async (req, res) => {
    try {
        await client.connect();
        const db = client.db('githubdata');
        const collection = db.collection(collectionName);
        // console.log(collection);

        const allData = await collection.find({}).toArray();

        if (allData.length > 0) {
            res.status(200).json(allData);
        } else {
            res.status(404).json({ error: 'No data found' });
        }
    } catch (error) {
        console.error('Error retrieving data from MongoDB:', error);
        res.status(500).json({ error: 'Internal server error' });
    } finally {
        await client.close();
    }
});

app.post('/github', async (req, res) => {
    try {
        const { url } = req.body;

        const response = await axios.get(url);

        const githubData = response.data;
        // console.log(response.data);
        if (githubData && Array.isArray(githubData)) {
            await saveDataToMongo(githubData);
        }

        res.status(200).json({ message: 'Data fetched and saved successfully' });
    } catch (error) {
        console.error('Error fetching data from GitHub:', error);
        res.status(500).json({ error: 'Internal server error' });
    }
});

app.get('/github/:id', async (req, res) => {
    try {
        // Get the "id" from the request parameters
        const { id } = req.params;

        // Connect to the MongoDB database
        await client.connect();
        const db = client.db('githubdata');
        const collection = db.collection(collectionName);

        // Retrieve data from MongoDB based on the "id"
        const repository = await collection.findOne({ id: parseInt(id) });

        if (repository) {
            res.status(200).json(repository);
        } else {
            res.status(404).json({ error: 'Data not found' });
        }
    } catch (error) {
        console.error('Error retrieving data from MongoDB:', error);
        res.status(500).json({ error: 'Internal server error' });
    } finally {
        // Close the MongoDB client connection
        await client.close();
    }
});

app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});
