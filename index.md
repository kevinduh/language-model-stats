## Monolingual Models


Organisation | Model | Citation | Architecture | Data | Tokens (B) | Size (B) | Compute | Training Strategy
---|---|---|---|---|---|---|---|---
Google | BERT Large | [Devlin 2019](https://aclanthology.org/N19-1423.pdf) | EncDec | Books, Wikipedia | 3.3 | 0.34 | 64TPUs for 4 days | MLM, Next sentence prediction
Meta | BART | [Lewis 2019](https://arxiv.org/pdf/1910.13461.pdf) | EncDec | Books, Wikipedia (160Gb) |  | 0.4 | 64 TPU chips for 4 days | <details>MLM scheme where multiple tokens are masked with a single [MASK] token</details>
Google | XLNet | [Yang 2019](https://arxiv.org/pdf/1906.08237.pdf) | Dec | Books, Wikipedia, ClueWeb, CommonCrawl | 33 | 0.4 | 512 TPU v3 chips for 5 days | Permutation
Meta | Blenderbot | [Roller 2020](https://arxiv.org/pdf/2004.13637.pdf) | EncDec | Reddit, ConvAI, Empathetic Dialogues, WoW, Blended Skill Talk | 88.8 | 9.4B | 128 v100s ~3 weeks * | <details>MLM, 2 step; first retrieve then concatenate to input to generate a refined response</details>
EleutherAI | GPTNeoX | [Black 2021](https://arxiv.org/pdf/2204.06745.pdf) | Dec | The Pile | 420 | 20 | <details>twelve Supermicro AS-4124 GO-NART servers, each with eight NVIDIA A100-SXM4-40GB GPUs</details> | AR
Google | T5 | [Raffel 2020](https://arxiv.org/pdf/1910.10683.pdf) | EncDec | C4 (cleaned common crawl) | 34 | 11 | 1,024 TPU v3 chips for ? | <details>Combines pre-training followed by fine-tuning on multiple tasks using the same architecture</details>
OpenAI | GPT-3 | [Brown 2020](https://arxiv.org/pdf/2005.14165.pdf) | Dec | Books, Wikipedia, Webcrawl | 300 | 175 | 3.64 * 10^3 PetaFlops | AR
Meta | OPT | [Zhang 2022](https://arxiv.org/pdf/2205.01068.pdf) | Dec | Books, CCNews, The Pile, Reddit | 300 | 175B | 992 80GB A100 GPUs for 33 days | AR

## Multilingual Models



Organisation | Model | Citation | Architecture | Data | Tokens (B) | Size (B) | Compute | Training Strategy
---|---|---|---|---|---|---|---|---
Google | Mbert | [Devlin 2019](https://github.com/google-research/bert/blob/master/multilingual.md) | EncDec | Wikipedia | ? | 0.1 | 64TPUs for 4 days (bert estimate) | MLM, Next Sentence Prediction
Meta | MBART-large | [Liu 2020](https://arxiv.org/pdf/2001.08210.pdf) | Enc-Dec | CC25, backtranslate | ? | 0.6 | 256 Nvidia V100 GPUs for 18 days | MLM; (Bart training), sentence shuffling
Meta | XGLM | [Lin 2021](https://arxiv.org/pdf/2112.10668.pdf) | EncDec | CC100 | 500 | 7.5 | v100s | AR; Trained on mixture of monoligual texts
Meta | XLMR | [Goyal 2020](https://arxiv.org/pdf/1911.02116.pdf) | Enc-Dec | CC100 | 167 | 10.7 | ? | MLM
Google | Byt5 | [Xue 2022](https://arxiv.org/pdf/2105.13626.pdf) | Enc-Dec | MC4 | 6.4T | 12.9 | ? | Token free (byte level MT5)
Google | MT5 | [Xue 2021](https://arxiv.org/pdf/2010.11934.pdf) | Enc-Dec | MC4 | 6.4T | 13 | ? | MLM
Meta | M2M100 | [Fan 2020](https://arxiv.org/pdf/2010.11125.pdf) | Enc-Dec | CCMatrix, backtranslate | 7.5 parallel sentences; | 15.4 | "hundreds of GPUs" | AR

Legend:
- Architecture = Encoder-Decoder (EncDec), Decoder only (Dec)
- Training Strategy = Masked Language Model (MLM), Auto-Regressive Decoder (AR)
- Data = Source or domain of training data
- Tokens = training data's number of tokens, in billions
- Size = number of parameters in billions
- (*) = author correspondence
