// See the Electron documentation for details on how to use preload scripts:
// https://www.electronjs.org/docs/latest/tutorial/process-model#preload-scripts
// preload.js

const { contextBridge, ipcRenderer } = require("electron");

contextBridge.exposeInMainWorld("electronAPI", {
  saveFile: (code) => ipcRenderer.invoke("save-file", code),
  runPython: (inputFilePath) =>
    ipcRenderer.invoke("run-python-script", inputFilePath),
  isDevelopment: process.defaultApp || process.env.NODE_ENV === "development",
});
