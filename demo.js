const { graphviz } = require("@hpcc-js/wasm");
const fs = require("fs");

async function convertDotToPng(dotString, outputPath) {
  try {
    // Initialize WASM first (critical!)
    await graphviz.load();
    
    // Convert DOT to PNG
    const pngData = await graphviz.dot(dotString, "png");
    
    // Write to file
    fs.writeFileSync(outputPath, pngData);
    console.log(`Successfully saved to ${outputPath}`);
  } catch (error) {
    console.error("Conversion failed:", error);
  }
}

// Example usage
const dotCode = `
  digraph G {
    A -> B;
    B -> C;
    C -> A;
  }
`;

convertDotToPng(dotCode, "output.png");