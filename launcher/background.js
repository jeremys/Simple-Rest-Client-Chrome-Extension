var extension_id = "fdmmgilgnpjigdojojpjoooidkmcomcm";
var extension_url = "https://chrome.google.com/webstore/detail/" + extension_id;
chrome.browserAction.onClicked.addListener(function(a) {
  chrome.management.getAll(function(extensions) {
    var count = extensions.length;    
    console.log(extensions);
    for(var i = 0; i < count; i++) { 
      var ext = extensions[i];
      if(ext.id == extension_id){
        if(ext.enabled){
          chrome.management.launchApp(ext.id)
          return;
        }
        else {
          chrome.management.setEnabled(ext.id,true,function() {
            chrome.management.launchApp(ext.id);
          });
          return;
        }
      }
    }                                           
    chrome.tabs.create({ url : extension_url });
  });
});
