/**
 * node2shell lab target — CVE-2026-111497
 * Node v26.8.2 + Express 5.3.0 + body-parser 2.4.0 (all vulnerable)
 *
 * Express 5 + body-parser 2.x enable Brotli decompression by default,
 * exposing the bundled Brotli decoder to attacker-controlled input.
 */
const express = require("express");
const bodyParser = require("body-parser");

const app = express();
const PORT = 3000;

// body-parser 2.x: inflate: true is the default, accepts Content-Encoding: br
app.use(bodyParser.json({ inflate: true, limit: "50mb" }));
app.use(bodyParser.raw({ inflate: true, limit: "50mb", type: "*/*" }));

app.get("/", (req, res) => {
  res.set("Accept-Encoding", "br");
  res.json({ error: "Where brotli? Brotli disappointed." });
});

app.post("/", (req, res) => {
  res.set("Accept-Encoding", "br");
  if (req.get("Content-Encoding") !== "br") {
    res.json({ error: "Where brotli? Brotli disappointed." });
  } else {
    res.json({
      msg: "Ok, move along please.",
      received: typeof req.body,
      length: req.body.length,
    });
  }
});

app.get("/health", (_req, res) => {
  res.json({
    node: process.version,
    pid: process.pid,
  });
});

app.listen(PORT, "0.0.0.0", () => {
  console.log(`[target] Node.js ${process.version} listening on :${PORT}`);
  console.log(`[target] Platform: ${process.platform}/${process.arch}`);
  console.log(`[target] VULNERABLE: fix is 26.12.1 (running 26.8.2)`);
});
