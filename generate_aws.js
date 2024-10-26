// This generates the AWS links which you need to download your memories
// This JS script was written by @evanugarte on GitHub for a similair tool: https://github.com/evanugarte/snapchat-memories-downloader

const axios = require('axios')
const fs = require('fs')
const memories = require('./memories_history')

function addJsonToFile(json) {
  fs.writeFile(__dirname + '/aws_links.json', JSON.stringify(json), err => {
    if (err) throw err
    else console.log('No problems found');
  })
}

function recordError(link, err) {
  fs.appendFile(__dirname + '/errors.txt',
    `${link}\n ${JSON.stringify(err)} \n\n`, _ => { })
}

function determineFileType(awsLink) {
  const url = awsLink.split('?')[0];
  const fileType = url.split('.')[url.split('.').length - 1];
  return fileType;
}

async function generateAwsLinks() {
  let snapchatMemoryData = [];
  let completed = 0;
  axios.defaults.timeout = 10000
  await Promise.all(
    memories['Saved Media'].map(async (memory, index) => {
      await axios.post(memory['Download Link'])
        .then(res => {
          const fileType = determineFileType(res.data);
          const date = memory['Date'].substr(0, memory['Date'].length - 4);
          snapchatMemoryData.push({
            date, fileType, awsLink: res.data
          });
          completed++;
          process.stdout.write(`Completed ${completed} / ${memories['Saved Media'].length}\r`);
        })
        .catch(err => {
          recordError(memory['Download Link'], err)
        });
    })
  )
  snapchatMemoryData = snapchatMemoryData.sort(function (a, b) {
    return Date.parse(a['date']) - Date.parse(b['date'])
  });
  addJsonToFile(snapchatMemoryData);
}

async function main() {
  await generateAwsLinks();
}

main()
