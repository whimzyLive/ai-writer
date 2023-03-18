# AI Blog Writer - Powered by ChatGPT

## Using as a Github Actions

### Action Inputs

| Name        | Description                                                  | Example                | Required             |
| ----------- | ------------------------------------------------------------ | ---------------------- | -------------------- |
| topic-files | List of Files to a topic or description - separated by comma | nextjs/fundamentals.md | ☑️                   |
| output-dir  | .temp                                                        | .out                   | **default** - `.out` |

### Environment variables

| Name            | Description                                                  | Example                                  | Required |
| --------------- | ------------------------------------------------------------ | ---------------------------------------- | -------- |
| OPENAI_API_KEY  | API key to access the hosted GPT model                       | XXXXXX                                   | ☑️       |
| OPENAI_API_TYPE | API type - value must be one of 'azure', 'azure_ad 'open_ai' | **default** - `open_api`                 |
| OPENAI_API_BASE | API base url to locate GPT model                             | `https://<your-model>.openai.azure.com/` | ☑️       |
| OPENAI_ENGINE   | name of the deployed model                                   | gh-blog-writer-gpt-35-turbo              | ☑️       |
