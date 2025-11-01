# Integration Guide - SEVE Framework

**SEVE Framework v1.0.0**  
**Última Atualização**: 2025-01-29

---

## 📋 **Índice de Integrações**

- [Integração Python](#integração-python)
- [Integração Web (FastAPI/Flask/Django)](#integração-web)
- [Integração ERP](#integração-erp)
- [Integração IoT](#integração-iot)
- [Integração Blockchain/DeFi](#integração-blockchaindefi)

---

## 🔗 **Guias de Integração**

## Integração Python

### Uso Básico do Framework

**Importação e Inicialização:**

```python
import asyncio
from seve_framework import (
    SEVEHybridFramework,
    SEVEConfig,
    SEVEMode,
    PrivacyLevel,
    EthicsLevel
)

async def main():
    # 1. Criar configuração
    config = SEVEConfig(
        mode=SEVEMode.HYBRID,
        privacy_level=PrivacyLevel.HIGH,
        ethics_level=EthicsLevel.STRICT,
        debug=True
    )
    
    # 2. Criar e inicializar framework
    framework = SEVEHybridFramework(config)
    await framework.initialize()
    
    # 3. Preparar dados
    data = {
        "visual": {
            "image_path": "image.jpg",
            "detected_objects": ["person", "car"],
            "faces_detected": 2
        },
        "sensor": {
            "temperature": 23.5,
            "motion": True
        }
    }
    
    context = {
        "location": "downtown",
        "privacy_mode": "strict",
        "consent_given": True
    }
    
    # 4. Processar dados
    result = await framework.process_context(data, context)
    
    # 5. Usar resultados
    print(f"Status: {result.status}")
    print(f"Processing Time: {result.processing_time_ms}ms")
    
    return result

# Executar
result = asyncio.run(main())
```

### Usando Módulos Individuais

**SEVE-Vision apenas:**

```python
from seve_framework.vision import SEVEVisionModule
from seve_framework.config import SEVEConfig

async def vision_example():
    config = SEVEConfig()
    vision = SEVEVisionModule(config)
    await vision.initialize()
    
    # Processar imagem
    image_data = b"... image bytes ..."  # Ou path para arquivo
    result = await vision.process_visual_input(image_data)
    
    print(f"Detected objects: {result.detected_objects}")
    print(f"Anonymized: {result.anonymization_applied}")
    
    return result
```

**SEVE-Ethics apenas:**

```python
from seve_framework.ethics import SEVEEthicsModule
from seve_framework.config import SEVEConfig, EthicsLevel

async def ethics_example():
    config = SEVEConfig(ethics_level=EthicsLevel.STRICT)
    ethics = SEVEEthicsModule(config)
    await ethics.initialize()
    
    # Validar decisão
    decision_data = {
        "action": "store_personal_data",
        "data_type": "facial_recognition",
        "consent": False
    }
    
    validation = await ethics.validate_decision(decision_data)
    
    if validation.result == "BLOCKED":
        print(f"Bloqueado: {validation.reason}")
    
    return validation
```

---

## Integração Web

### FastAPI - API REST Completa

**Exemplo completo de API REST com SEVE:**

```python
from fastapi import FastAPI, HTTPException, UploadFile, File
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Optional
import asyncio
from seve_framework import SEVEHybridFramework, SEVEConfig, SEVEMode

app = FastAPI(
    title="SEVE Framework API",
    description="Ethical AI Processing API",
    version="1.0.0"
)

# Inicializar SEVE (uma vez na startup)
seve_framework = None

@app.on_event("startup")
async def startup_event():
    global seve_framework
    config = SEVEConfig(mode=SEVEMode.HYBRID)
    seve_framework = SEVEHybridFramework(config)
    await seve_framework.initialize()
    print("✅ SEVE Framework initialized")

# Models Pydantic
class ProcessingRequest(BaseModel):
    sensor_data: dict
    context: Optional[dict] = None
    privacy_level: Optional[str] = "high"

class ProcessingResponse(BaseModel):
    status: str
    processing_time_ms: float
    result: dict
    ethics_validation: dict

# Endpoints
@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "framework_initialized": seve_framework is not None
    }

@app.post("/api/v1/process", response_model=ProcessingResponse)
async def process_data(request: ProcessingRequest):
    """Process data with SEVE Framework"""
    try:
        result = await seve_framework.process_context(
            data={"sensor": request.sensor_data},
            context=request.context or {}
        )
        
        return ProcessingResponse(
            status=result.status.value,
            processing_time_ms=result.processing_time_ms,
            result=result.to_dict(),
            ethics_validation={
                "passed": all(a.result.value != "BLOCKED" for a in result.ethics_assessments),
                "assessments": [
                    {
                        "rule": a.rule_name,
                        "result": a.result.value,
                        "reason": a.reason
                    }
                    for a in result.ethics_assessments
                ]
            }
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/v1/process-image")
async def process_image(file: UploadFile = File(...)):
    """Process image with SEVE-Vision"""
    try:
        # Ler imagem
        image_bytes = await file.read()
        
        # Processar com SEVE-Vision
        vision_module = seve_framework.vision_module
        result = await vision_module.process_visual_input(image_bytes)
        
        return {
            "status": "success",
            "detected_objects": result.detected_objects,
            "faces_detected": result.faces_detected,
            "anonymization_applied": result.anonymization_applied,
            "privacy_protected": True
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/v1/capabilities")
async def get_capabilities():
    """Get framework capabilities"""
    capabilities = seve_framework.get_capabilities()
    return capabilities

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

**Executar:**
```bash
python api_server.py
# Ou
uvicorn api_server:app --reload
```

**Acessar documentação automática:**
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

---

### Flask - Integração Simples

```python
from flask import Flask, request, jsonify
from seve_framework import SEVEHybridFramework, SEVEConfig
import asyncio

app = Flask(__name__)

# Inicializar SEVE
config = SEVEConfig()
seve = SEVEHybridFramework(config)

@app.before_first_request
def initialize_seve():
    asyncio.run(seve.initialize())

@app.route('/process', methods=['POST'])
def process():
    data = request.json
    result = asyncio.run(seve.process_context(data))
    return jsonify({
        "status": result.status.value,
        "result": result.to_dict()
    })

if __name__ == '__main__':
    app.run(debug=True)
```

---

### Django - Integração com Admin

```python
# views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import asyncio
from seve_framework import SEVEHybridFramework, SEVEConfig

# Inicializar uma vez
seve = None

def get_seve():
    global seve
    if seve is None:
        config = SEVEConfig()
        seve = SEVEHybridFramework(config)
        asyncio.run(seve.initialize())
    return seve

@csrf_exempt
def process_seve(request):
    if request.method == 'POST':
        data = request.json
        framework = get_seve()
        result = asyncio.run(framework.process_context(data))
        return JsonResponse({
            "status": result.status.value,
            "result": result.to_dict()
        })
    return JsonResponse({"error": "Method not allowed"}, status=405)
```

---

## Integração ERP

### SEVE-Link para ERP

**Conexão com ERP via SEVE-Link:**

```python
from seve_framework.link import SEVELinkModule
from seve_framework.config import SEVEConfig

async def erp_integration():
    config = SEVEConfig()
    link = SEVELinkModule(config)
    await link.initialize()
    
    # Conectar com ERP
    erp_config = {
        "system_type": "sap",  # ou "oracle", "salesforce", etc.
        "endpoint": "https://erp.company.com/api",
        "auth": {
            "type": "oauth2",
            "client_id": "...",
            "client_secret": "..."
        }
    }
    
    connection_id = await link.connect_external_system(
        system_type="erp",
        config=erp_config
    )
    
    # Sincronizar dados
    transaction_data = {
        "order_id": "ORD-12345",
        "customer": "John Doe",
        "amount": 1000.00,
        "items": [...]
    }
    
    sync_result = await link.sync_transaction(
        transaction_data=transaction_data,
        connection_id=connection_id
    )
    
    print(f"Sync status: {sync_result.status}")
    print(f"Duration: {sync_result.duration}ms")
    
    return sync_result
```

### Webhook para Eventos ERP

**Receber eventos de ERP via webhook:**

```python
from fastapi import FastAPI, Request
from seve_framework import SEVEHybridFramework, SEVEConfig

app = FastAPI()
seve = SEVEHybridFramework(SEVEConfig())
await seve.initialize()

@app.post("/webhook/erp/{event_type}")
async def erp_webhook(event_type: str, request: Request):
    """Processar eventos de ERP"""
    payload = await request.json()
    
    # Processar com SEVE
    result = await seve.process_context(
        data={"erp_event": payload},
        context={"event_type": event_type}
    )
    
    # Se aprovado pela validação ética, processar
    if result.status.value != "ethics_blocked":
        # Integrar com seu sistema
        process_erp_event(payload, result)
    
    return {"status": "processed", "ethics_validated": True}
```

---

## Integração IoT

### SEVE-Sense para Sensores IoT

**Processamento de dados de sensores:**

```python
from seve_framework.sense import SEVESenseModule
from seve_framework.config import SEVEConfig

async def iot_integration():
    config = SEVEConfig()
    sense = SEVESenseModule(config)
    await sense.initialize()
    
    # Dados de sensores IoT
    sensor_data = {
        "temperature": 23.5,
        "humidity": 65.2,
        "motion": True,
        "proximity": 2.1,
        "audio_level": 45.0,
        "lidar": {
            "distance": 15.5,
            "objects": 4
        },
        "radar": {
            "speed": 45.2,
            "direction": "north"
        }
    }
    
    context = {
        "device_id": "sensor_001",
        "location": "warehouse_entrance",
        "timestamp": "2025-01-29T10:00:00Z"
    }
    
    # Processar dados multimodais
    result = await sense.process_multimodal_input(
        sensor_data=sensor_data,
        context=context
    )
    
    print(f"Processed sensors: {result.processed_sensors}")
    print(f"Insights: {result.insights}")
    
    return result
```

### MQTT Integration

**Receber dados IoT via MQTT:**

```python
import paho.mqtt.client as mqtt
from seve_framework import SEVEHybridFramework, SEVEConfig
import asyncio

seve = SEVEHybridFramework(SEVEConfig())
asyncio.run(seve.initialize())

def on_message(client, userdata, message):
    """Processar mensagens MQTT com SEVE"""
    sensor_data = json.loads(message.payload.decode())
    
    # Processar com SEVE
    result = asyncio.run(seve.process_context(
        data={"sensor": sensor_data},
        context={"source": "mqtt", "topic": message.topic}
    ))
    
    # Publicar resultado processado
    if result.status.value != "ethics_blocked":
        client.publish("seve/processed", json.dumps(result.to_dict()))

# Configurar cliente MQTT
client = mqtt.Client()
client.on_message = on_message
client.connect("mqtt.broker.com", 1883, 60)
client.subscribe("sensors/#")
client.loop_forever()
```

---

## Integração Blockchain/DeFi

### Integração com SEVEToken (ERC-20)

**Interagir com smart contract SEVEToken:**

```python
from web3 import Web3
from seve_framework import SEVEConfig
import os

# Conectar com blockchain
w3 = Web3(Web3.HTTPProvider(os.getenv("ALCHEMY_URL")))
w3.eth.default_account = w3.eth.accounts[0]

# Endereço do contrato SEVEToken (após deploy)
SEVE_TOKEN_ADDRESS = "0x..."  # Substituir pelo endereço real

# ABI do contrato (gerado após compilação)
# Carregar de artifacts/SEVEToken.sol/SEVEToken.json
with open("artifacts/contracts/SEVEToken.sol/SEVEToken.json") as f:
    contract_data = json.load(f)
    abi = contract_data["abi"]

# Criar instância do contrato
seve_token = w3.eth.contract(address=SEVE_TOKEN_ADDRESS, abi=abi)

# Operações básicas
def get_balance(address):
    """Obter saldo de tokens"""
    return seve_token.functions.balanceOf(address).call()

def transfer_tokens(to_address, amount):
    """Transferir tokens"""
    tx = seve_token.functions.transfer(to_address, amount).build_transaction({
        "from": w3.eth.default_account,
        "nonce": w3.eth.get_transaction_count(w3.eth.default_account),
        "gas": 100000,
        "gasPrice": w3.eth.gas_price
    })
    
    signed_tx = w3.eth.account.sign_transaction(tx, private_key=os.getenv("PRIVATE_KEY"))
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    return w3.eth.wait_for_transaction_receipt(tx_hash)
```

### Integração com DEX (Uniswap, SushiSwap)

**Como SEVEToken funciona com DEXs:**

```python
# SEVEToken é ERC-20 padrão, funciona em qualquer DEX
# Exemplo de integração conceitual:

def add_liquidity_uniswap(token_amount, eth_amount):
    """Adicionar liquidez no Uniswap"""
    # SEVEToken é compatível com qualquer DEX ERC-20
    # Use a interface padrão do Uniswap Router
    uniswap_router = w3.eth.contract(address=UNISWAP_ROUTER, abi=UNISWAP_ROUTER_ABI)
    
    tx = uniswap_router.functions.addLiquidityETH(
        SEVE_TOKEN_ADDRESS,
        token_amount,
        0,  # slippage tolerance
        0,  # slippage tolerance
        w3.eth.default_account,
        int(time.time()) + 300
    ).build_transaction({...})
    
    # Assinar e enviar
    return send_transaction(tx)
```

### Event Listeners para Smart Contracts

**Monitorar eventos dos contratos SEVE:**

```python
from web3 import Web3
from seve_framework import SEVEHybridFramework
import asyncio

w3 = Web3(Web3.HTTPProvider(os.getenv("ALCHEMY_URL")))
seve = SEVEHybridFramework(SEVEConfig())
asyncio.run(seve.initialize())

def handle_token_transfer(event):
    """Processar evento de transferência com SEVE"""
    from_address = event['args']['from']
    to_address = event['args']['to']
    amount = event['args']['value']
    
    # Validar transferência com SEVE-Ethics
    decision_data = {
        "action": "token_transfer",
        "from": from_address,
        "to": to_address,
        "amount": amount
    }
    
    result = asyncio.run(seve.ethics_module.validate_decision(decision_data))
    
    if result.result == "BLOCKED":
        # Logar ou reverter (se possível)
        print(f"⚠️ Transferência bloqueada: {result.reason}")

# Criar filtro de eventos
event_filter = seve_token.events.Transfer.create_filter(fromBlock='latest')

# Monitorar eventos
while True:
    for event in event_filter.get_new_entries():
        handle_token_transfer(event)
    time.sleep(2)
```

---

## 📚 **Exemplos Completos**

### Exemplo: Sistema Completo Python + Web + Blockchain

```python
from fastapi import FastAPI
from seve_framework import SEVEHybridFramework, SEVEConfig
from web3 import Web3
import os

app = FastAPI()

# Inicializar SEVE
seve = SEVEHybridFramework(SEVEConfig())
await seve.initialize()

# Conectar blockchain
w3 = Web3(Web3.HTTPProvider(os.getenv("ALCHEMY_URL")))
seve_token = w3.eth.contract(address=SEVE_TOKEN_ADDRESS, abi=TOKEN_ABI)

@app.post("/process-and-reward")
async def process_and_reward(data: dict):
    """Processar dados e recompensar com tokens SEVE"""
    
    # 1. Processar com SEVE
    result = await seve.process_context(data)
    
    # 2. Se aprovado eticamente, emitir tokens
    if result.status.value != "ethics_blocked":
        # Calcular recompensa baseada em contribuição
        reward_amount = calculate_reward(result)
        
        # Transferir tokens (requer permissões apropriadas)
        tx_hash = seve_token.functions.transfer(
            result.user_address,
            reward_amount
        ).transact({'from': ADMIN_ADDRESS})
        
        return {
            "status": "processed_and_rewarded",
            "processing_result": result.to_dict(),
            "reward_tx": tx_hash.hex()
        }
    else:
        return {
            "status": "ethics_blocked",
            "reason": result.ethics_assessments[0].reason
        }
```

---

## ⚠️ **Considerações Importantes**

### Segurança

1. **Sempre valide inputs:**
   - Use Pydantic models para validação automática
   - Valide tamanhos de arquivo
   - Limite rate de requisições

2. **Autenticação e Autorização:**
```python
from fastapi import Depends, HTTPException, Security
from fastapi.security import HTTPBearer

security = HTTPBearer()

@app.post("/process")
async def process(credentials = Security(security)):
    # Validar token
    if not validate_token(credentials.credentials):
        raise HTTPException(status_code=401, detail="Invalid token")
    # ...
```

### Ética

1. **SEVE-Ethics valida automaticamente todas as operações**
2. **Respeite consentimento:**
```python
context = {
    "consent_given": True,  # Sempre verificar
    "consent_type": "explicit",
    "privacy_level": "maximum"
}
```

3. **Monitorar bloqueios éticos:**
```python
if result.status.value == "ethics_blocked":
    log_ethical_block(result)
    notify_admin(result)
```

### Performance

1. **Use async quando possível:**
```python
# ✅ Bom - async
result = await seve.process_context(data)

# ❌ Ruim - bloqueia thread
result = seve.process_context(data)  # Sem await
```

2. **Cache resultados quando apropriado:**
```python
from functools import lru_cache

@lru_cache(maxsize=100)
def cached_processing(data_hash):
    return seve.process_context(data)
```

3. **Processamento em batch:**
```python
# Processar múltiplos itens de uma vez
results = await seve.process_batch(data_list)
```

### Privacidade

1. **Dados são anonimizados automaticamente por SEVE-Vision**
2. **Não armazene dados sensíveis sem criptografia:**
```python
from cryptography.fernet import Fernet

# Criptografar antes de armazenar
encrypted = encrypt_sensitive_data(data)
```

3. **Respeite LGPD/GDPR:**
```python
# Implementar direito ao esquecimento
@app.delete("/user/{user_id}/data")
async def delete_user_data(user_id: str):
    await seve.delete_user_data(user_id)  # Implementar no SEVE
    return {"status": "deleted"}
```

---

## 📞 **Suporte para Integração**

- **GitHub Issues**: [Reportar problema](https://github.com/symbeon/seve-framework/issues)
- **Documentação**: [Índice Completo](../INDEX.md)
- **FAQ**: [FAQ.md](../FAQ.md) - Perguntas frequentes sobre integração
- **Troubleshooting**: [TROUBLESHOOTING.md](../TROUBLESHOOTING.md) - Problemas comuns
- **Comunidade**: [Discord/Telegram](https://community.seve-framework.ai)
- **Email**: research@symbeon-tech.com

---

**Última Atualização**: 2025-01-29  
**Mantido por**: Equipe EON - Symbeon Tech
