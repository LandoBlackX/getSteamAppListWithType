import { Octokit } from '@octokit/core';
import https from 'https';

// 设置全局环境变量
process.env.NODE_TLS_REJECT_UNAUTHORIZED = '0';
var counta = 0;
const agent = new https.Agent({
  rejectUnauthorized: false,
});

const octokit = new Octokit({
  auth: 'secrets.TOKEN',
  request: {
    agent: agent,
  },
});

async function getWorkflows() {
  try {
    const response = await octokit.request(
      'POST /repos/F1NN1ER/getSteamAppListWithType/actions/workflows/main.yml/dispatches',
      {
        ref: 'main',
        headers: {
          'X-GitHub-Api-Version': '2022-11-28',
        },
      }
    );
    counta++;
    console.log(counta);
  } catch (error) {
    console.error(error);
  }
}

getWorkflows();
setInterval(getWorkflows, 70000);
