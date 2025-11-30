# 🎬 Roteiro de Vídeo Demo: SEVE CLI
**Duração**: ~2 minutos
**Formato**: Screencast do Terminal

---

### Cena 1: Introdução (0:00 - 0:20)
**Visual**: Terminal limpo, logo do SEVE aparece.
**Narração**: "Bem-vindo ao SEVE Framework. Hoje vamos ver como a ética pode ser parte da infraestrutura da sua IA."
**Ação**:
```bash
python seve_cli.py init --ethics-level strict
```
*(Mostra barra de progresso de inicialização e tabela de configuração)*

---

### Cena 2: Validação de Sucesso (0:20 - 0:50)
**Narração**: "Vamos processar uma transação médica legítima, com consentimento e anonimização."
**Ação**:
```bash
python seve_cli.py validate examples/data/valid_medical_record.json
```
*(Mostra painel verde "APPROVED" com score ético alto)*
**Narração**: "O GuardFlow valida a privacidade e aprova instantaneamente."

---

### Cena 3: Bloqueio Ético (0:50 - 1:20)
**Narração**: "Agora, o que acontece se tentarmos acessar dados sem consentimento?"
**Ação**:
```bash
python seve_cli.py validate examples/data/violation_attempt.json
```
*(Mostra painel vermelho "BLOCKED" e motivo do bloqueio)*
**Narração**: "O SEVE bloqueia a transação na hora. A violação nem chega ao banco de dados."

---

### Cena 4: Auditoria e Monitoramento (1:20 - 1:50)
**Narração**: "Tudo fica registrado em um audit trail imutável."
**Ação**:
```bash
python seve_cli.py audit --days 1
```
*(Mostra tabela de auditoria com as tentativas aprovadas e bloqueadas)*
**Ação**:
```bash
python seve_cli.py monitor --source camera_feed_1
```
*(Mostra dashboard em tempo real)*

---

### Cena 5: Conclusão (1:50 - 2:00)
**Visual**: Logo final e link para GitHub.
**Narração**: "SEVE Framework. Tecnologia com Propósito. Baixe agora no GitHub."

---
