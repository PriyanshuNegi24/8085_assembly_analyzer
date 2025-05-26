const { app, BrowserWindow, ipcMain } = require("electron");
const path = require("path");
const fs = require("fs");
const { spawn } = require("child_process");

let mainWindow;

ipcMain.handle("save-file", async (event, code) => {
  try {
    const filePath = path.join(
      __dirname,
      "..",
      "8085_assembly_analyzer",
      "src",
      "main",
      "input.asm"
    );
    console.log(filePath, "\t ::  file path ");
    fs.writeFileSync(filePath, code);
    console.log("File written successfully");
    return true;
  } catch (error) {
    console.error("Error writing file:", error);
    throw error;
  }
});

ipcMain.handle("run-python-script", async () => {
  const pythonExecutable = path.join(__dirname, "..", "pbl", "bin", "python");

  const scriptPath = path.join(
    __dirname,
    "..",
    "8085_assembly_analyzer",
    "src",
    "main",
    "analyze.py"
  );
  console.log("Trying to spawn Python at:", pythonExecutable);

  return new Promise((resolve, reject) => {
    const pythonProcess = spawn(pythonExecutable, [scriptPath]);

    let output = "";
    let errorOutput = "";

    pythonProcess.stdout.on("data", (data) => {
      output += data.toString();
    });

    pythonProcess.stderr.on("data", (data) => {
      errorOutput += data.toString();
    });

    pythonProcess.on("close", (code) => {
      if (code === 0) {
        resolve(output);
      } else {
        reject(new Error(errorOutput || `Python exited with code ${code}`));
      }
    });
  });
});

function createWindow() {
  mainWindow = new BrowserWindow({
    width: 800,
    height: 600,
    webPreferences: {
      nodeIntegration: false,
      contextIsolation: true,
      preload: path.join(__dirname, "preload.js"),
    },
  });

  mainWindow.loadFile(path.join(__dirname, "index.html"));

  if (process.env.NODE_ENV === "development") {
    mainWindow.webContents.openDevTools();
  }

  mainWindow.on("closed", () => {
    mainWindow = null;
  });
}

app.whenReady().then(createWindow);

app.on("window-all-closed", () => {
  if (process.platform !== "darwin") app.quit();
});

app.on("activate", () => {
  if (mainWindow === null) createWindow();
});
