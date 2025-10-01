function generateDailyScript() {
  var sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  var lastRow = sheet.getLastRow();
  
  for (var row = 2; row <= lastRow; row++) {
    var status = sheet.getRange(row, 7).getValue();
    if (status !== "Posted" && status !== "Generated") {
      var hook = sheet.getRange(row, 3).getValue();
      var script = sheet.getRange(row, 4).getValue();
      var cta = sheet.getRange(row, 5).getValue();
      var hashtags = sheet.getRange(row, 6).getValue();

      var prompt = `
      Create a short-form TikTok/Instagram script:
      Hook: ${hook}
      Script: ${script}
      CTA: ${cta}
      Hashtags: ${hashtags}
      Make it conversational, under 60 seconds.
      `;

      var apiKey = "YOUR_API_KEY";
      var url = "https://api.openai.com/v1/chat/completions";
      var payload = {
        "model": "gpt-4o-mini",
        "messages": [{"role": "user", "content": prompt}]
      };

      var options = {
        "method": "post",
        "headers": {
          "Authorization": "Bearer " + apiKey,
          "Content-Type": "application/json"
        },
        "payload": JSON.stringify(payload)
      };

      var response = UrlFetchApp.fetch(url, options);
      var text = JSON.parse(response.getContentText()).choices[0].message.content;

      sheet.getRange(row, 8).setValue(text); 
      sheet.getRange(row, 7).setValue("Generated"); 
      break;
    }
  }
}
