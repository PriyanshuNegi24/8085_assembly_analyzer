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
  const executablePath = isDevelopment
    ? path.join(__dirname, "..", "dist", "analyze.exe")
    : path.join(process.resourcesPath, "dist", "analyze.exe");

  console.log("Trying to spawn executable at:", executablePath);
  console.log("Passing input file path:", inputFilePath);

  return new Promise((resolve, reject) => {
    const process = spawn(executablePath, [inputFilePath]);

    let output = "";
    let errorOutput = "";

    process.stdout.on("data", (data) => {
      output += data.toString();
    });

    process.stderr.on("data", (data) => {
      errorOutput += data.toString();
    });

    process.on("close", (code) => {
      if (code === 0) {
        resolve(output);
      } else {
        reject(new Error(errorOutput || `Process exited with code ${code}`));
      }
    });

    process.on("error", (err) => {
      reject(new Error("Failed to spawn analyze.exe: " + err.message));
    });
  });
});

function createWindow() {
  mainWindow = new BrowserWindow({
    show: false,
    width: 1280,
    height: 720,
    webPreferences: {
      nodeIntegration: false,
      contextIsolation: true,
      preload: path.join(__dirname, "preload.js"),
    },
  });

  mainWindow.loadFile(path.join(__dirname, "index.html"));
  mainWindow.maximize();
  mainWindow.show();
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
