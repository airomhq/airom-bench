const express = require("express");
const { Pool } = require("pg");

const app = express();
const db = new Pool();

app.get("/items", async (_req, res) => {
  const { rows } = await db.query("SELECT sku, qty FROM items ORDER BY sku");
  res.json(rows);
});

app.listen(3000);
