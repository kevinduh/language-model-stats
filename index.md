# Quick Reference for Large Pretrained Language Models

## Monolingual Models

| Model      | Citation   | Type       | Data       | Tokens (B) | Size (B)   | Compute    | CO2        | 
| :--------- | :--------- | :--------- | :--------- | :--------- | :--------- | :--------- | :--------- |
| BERT Large  | [Devlin 2019](https://aclanthology.org/N19-1423.pdf) | Mask | Books, Wikipedia | 3.3 | 0.34 | 64TPUs x 4 days | ? |
| GPT-3      | [Brown 2020](https://arxiv.org/pdf/2005.14165.pdf) | AR | Books, Wikipedia, Webcrawl | 300 | 175 | ? | ? 

Legend:
- Type = Auto-Regressive (AR), Masked LM (Mask), Encoder-Decoder (EncDec)
- Data = Source or domain of training data
- Tokens = training data's number of tokens, in billions
- Size = number of parameters in billions


## Multilingual Models
