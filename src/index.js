const { app, BrowserWindow, ipcMain } = require("electron");
const path = require("path");
const fs = require("fs");
const { spawn } = require("child_process");

let mainWindow;

const isDevelopment =
  process.defaultApp ||
  process.env.NODE_ENV === "development" ||
  process.argv.some((arg) => arg.includes("electron"));

ipcMain.handle("save-file", async (event, code) => {
  try {
    const userDataPath = app.getPath("userData");
    const filePath = path.join(userDataPath, "input.asm");

    fs.writeFileSync(filePath, code);
    console.log("File written successfully at:", filePath);
    return filePath;
  } catch (error) {
    console.error("Error writing file:", error);
    throw error;
  }
});

ipcMain.handle("run-python-script", async (event, inputFilePath) => {
  const pythonExecutable =
    process.env.NODE_ENV === "development"
      ? path.join(__dirname, "..", "pbl", "bin", "python")
      : path.join(process.resourcesPath, "pbl", "bin", "python");

  const scriptPath = isDevelopment
    ? path.join(
        __dirname,
        "src",
        "8085_assembly_analyzer",
        "src",
        "main",
        "analyze.py"
      )
    : path.join(
        process.resourcesPath,
        "8085_assembly_analyzer",
        "src",
        "main",
        "analyze.py"
      );

  console.log("Trying to spawn Python at:", pythonExecutable);
  console.log("Passing input file path:", inputFilePath);

  return new Promise((resolve, reject) => {
    const pythonProcess = spawn(pythonExecutable, [scriptPath, inputFilePath]);

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
