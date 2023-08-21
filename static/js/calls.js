async function multiplyDataCall() {
    const result = document.querySelector("#result");
    const numberValue = document.getElementById("numbervalue").value
    try {
      const response = await fetch("/multiply", {
        method: "POST", // or 'PUT'
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          number: numberValue
        }),
      });
      result.innerHTML = await response.text()
    } catch (e) {
      result.innerHTML = e.message;
    }
  }