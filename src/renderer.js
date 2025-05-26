document.addEventListener("DOMContentLoaded", () => {
  particlesJS.load("particles-js", "particles.json");

  const editor = document.querySelector(".editor");
  const compileBtn = document.querySelector(".btn-compile");
  const clearBtn = document.querySelector(".btn-clear");
  const outputDiv = document.querySelector(".output");

  compileBtn.addEventListener("click", compileCode);
  clearBtn.addEventListener("click", clearLogs);

  function clearLogs() {
    outputDiv.innerHTML = `<div class="log success">✔ [LOG] Compilation successful. No syntax errors found.</div>
      <div class="log warning">⚠ [WARN] Unused label at line 3.</div>
      <div class="log error">✖ [ERROR] Invalid operand at line 5.</div>`;
  }

  async function compileCode() {
    const code = editor.value;
    try {
      const inputFilePath = await window.electronAPI.saveFile(code + "\n");
      if (!inputFilePath) {
        throw new Error("Failed to save input file.");
      }

      const result = await window.electronAPI.runPython(inputFilePath);

      if (result.includes("No semantic errors")) {
        outputDiv.innerHTML = `
        <div class="log success">✔ [LOG] Compilation successful. No syntax errors found.</div>
        <pre>${result}</pre>
      `;
      } else {
        outputDiv.innerHTML = `
        <div class="log error">✖ [ERROR] Compilation failed with semantic errors.</div>
        <pre>${result}</pre>
      `;
      }
    } catch (error) {
      outputDiv.innerHTML = `
      <div class="log error">✖ [ERROR] SOMETHING WENT WRONG.</div>
      <pre>Error during compilation.\n${error.message}<pre>
      `;
    }
  }
});
