Organisation | Model | Citation | Architecture | Data | Tokens (B) | Size (B) | Compute | Training Strategy
---|---|---|---|---|---|---|---|---
Google | BERT Large | [Devlin 2019](https://aclanthology.org/N19-1423.pdf) | EncDec | Books, Wikipedia | 3.3 | 0.34 | 64TPUs for 4 days | MLM, Next sentence prediction
Meta | BART | [Lewis 2019](https://arxiv.org/pdf/1910.13461.pdf) | EncDec | Books, Wikipedia (160Gb) |  | 0.4 | 64 TPU chips for 4 days | <details>MLM scheme where multiple tokens are masked with a single [MASK] token</details>
Google | XLNet | [Yang 2019](https://arxiv.org/pdf/1906.08237.pdf) | Dec | Books, Wikipedia, ClueWeb, CommonCrawl | 33 | 0.4 | 512 TPU v3 chips for 5 days | Permutation
Meta | Blenderbot3B | [Roller 2020](https://arxiv.org/pdf/2004.13637.pdf) | EncDec | Reddit, ConvAI, Empathetic Dialogues, WoW, Blended Skill Talk | 88.8 | 2.7B | ? | <details>MLM, 2 step; first retrieve then concatenate to input to generate a refined response</details>
EleutherAI | GPTNeo | [Black 2021](https://github.com/EleutherAI/gpt-neo) | Dec | The Pile | 420 | 2.7 | ? | AR
Google | T5 | [Raffel 2020](https://arxiv.org/pdf/1910.10683.pdf) | EncDec | C4 (cleaned common crawl) | 34 | 11 | 1,024 TPU v3 chips for ? | <details>Combines pre-training followed by fine-tuning on multiple tasks using the same architecture</details>
OpenAI | GPT-3 | [Brown 2020](https://arxiv.org/pdf/2005.14165.pdf) | Dec | Books, Wikipedia, Webcrawl | 300 (400?) | 175 | ? | AR
Meta | OPT | [Zhang 2022](https://arxiv.org/pdf/2205.01068.pdf) | Dec | Books, CCNews, The Pile, Reddit | 300 | 175B | 992 80GB A100 GPUs for ? | AR
