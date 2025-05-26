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
      const writeInputFile = await window.electronAPI.saveFile(code + "\n") ;
      const result = await window.electronAPI.runPython();
      console.log("Compilation result:", result);
      outputDiv.innerHTML = `<pre>${result}</pre>`;
      if (!writeInputFile) {
        throw new Error("Failed to compile file.");
      }
    } catch (error) {
      outputDiv.textContent = "Error during compilation.\n" + error.message;
    }
  }
});
