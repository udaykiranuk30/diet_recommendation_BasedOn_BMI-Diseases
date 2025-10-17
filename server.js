const express = require('express');
const mongoose = require('mongoose');
const cors = require('cors');
const app = express();
const port = 3000; // Change the port number if needed
const mongoUrl = 'mongodb://localhost:27017'; // MongoDB connection URL
const dbName = 'finaldiet'; // Replace with your database name
const collectionName = 'dietfinal'; // Replace with your collection name

app.use(express.json());
app.use(cors());
// Connect to MongoDB
mongoose.connect(`${mongoUrl}/${dbName}`, { useNewUrlParser: true, useUnifiedTopology: true })
  .then(() => {
    console.log('Connected to MongoDB');
  })
  .catch((error) => {
    console.error('Failed to connect to MongoDB:', error);
    process.exit(1);
  });
// Define the schema for your collection
const dataSchema = new mongoose.Schema({
    user_details: {
      height: String,
      weight: String,
      age: String,
      gender: String,
    },
    recommended_recipes: [String],
  });
  
  // Define the model for your collection
  const Data = mongoose.model('Data', dataSchema,'dietfinal');
  
  // Fetch the data from MongoDB
app.get('/data', async (req, res) => {
    try {
      const data = await Data.find({}).exec();
      console.log('Retrieved data:', data); // Log the retrieved data
      res.json(data);
    } catch (err) {
      console.error('Failed to fetch data from MongoDB:', err);
      res.status(500).send('Failed to fetch data from MongoDB');
    }
  });
  
  
// Start the server
app.listen(port, () => {
  console.log(`Server listening on port ${port}`);
});
