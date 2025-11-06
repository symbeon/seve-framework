# TODO: Integração Completa dos Módulos Universais

**Versão**: 1.0.0  
**Data de Criação**: 2025-01-29  
**Status Geral**: 🔄 Em Progresso (60% completo)

---

## 📋 Resumo Executivo

Este documento lista todas as tarefas necessárias para completar a integração dos módulos universais legados no SEVE Framework v1.0.0, garantindo que todas as funcionalidades prometidas estejam entregues, testadas e documentadas.

**Progresso Atual:**
- ✅ Integração de código (core, adapters, empathy)
- ✅ Análise de impacto
- ⚠️ Testes (0%)
- ⚠️ Integração UniversalEthicsEngine (pendente)
- ⚠️ Documentação (40%)

---

## 🎯 Fase 1: Crítico - Funcionalidade Core (Prioridade ALTA)

### 1.1 Integração UniversalEthicsEngine

**Status**: 🔴 **PENDENTE**  
**Estimativa**: 3-5 dias  
**Dependências**: Nenhuma

#### Tarefas:
- [ ] **T1.1.1**: Criar `src/seve_framework/universal/ethics.py` baseado no legado
  - Migrar `UniversalEthicsEngine` completo
  - Migrar `DomainEthicsEngine` (ABC)
  - Migrar classes de suporte (`EthicalRule`, `EthicalAssessment`, etc.)
  - Garantir type hints completos
  - **Arquivo**: `legacy/guardflow_code/SEVE-UNIVERSAL/src/seve_universal/ethics.py`

- [ ] **T1.1.2**: Atualizar `src/seve_framework/universal/__init__.py`
  - Exportar classes do `ethics.py`
  - Garantir imports funcionais

- [ ] **T1.1.3**: Integrar `UniversalEthicsEngine` com `SEVEEthicsModule` (GuardFlow)
  - Criar adaptador que conecta ambos os sistemas
  - `UniversalEthicsEngine` avalia princípios universais + domínio
  - `GuardFlow` executa políticas críticas e bloqueios
  - Manter backward compatibility
  - **Arquivo**: `src/seve_framework/ethics.py`

- [ ] **T1.1.4**: Atualizar `SEVEHybridFramework` para usar ética universal
  - Integrar `UniversalEthicsEngine` no pipeline híbrido
  - Permitir escolha entre GuardFlow puro ou Universal+GuardFlow
  - **Arquivo**: `src/seve_framework/core.py`

- [ ] **T1.1.5**: Testes de integração ética
  - Testar avaliação universal + domínio
  - Testar integração com GuardFlow
  - Validar que ambos funcionam juntos sem conflitos
  - **Arquivo**: `tests/test_universal_ethics_integration.py`

**Critérios de Aceitação:**
- ✅ `UniversalEthicsEngine` funcional e testado
- ✅ Integração com GuardFlow sem conflitos
- ✅ Backward compatibility mantida
- ✅ Testes passando

---

### 1.2 Atualização de Imports e Dependências

**Status**: 🟡 **PARCIAL** (core.py atualizado, __init__.py atualizado)  
**Estimativa**: 1 dia  
**Dependências**: Nenhuma

#### Tarefas:
- [x] **T1.2.1**: Atualizar `src/seve_framework/core.py` para usar `.universal`
  - ✅ Concluído

- [x] **T1.2.2**: Atualizar `src/seve_framework/__init__.py` para usar `.universal`
  - ✅ Concluído

- [ ] **T1.2.3**: Verificar todos os imports no código base
  - Garantir que nenhum código tenta importar `seve_universal` externo
  - Buscar por imports órfãos
  - **Comando**: `grep -r "seve_universal" src/`

- [ ] **T1.2.4**: Validar que modo HYBRID funciona end-to-end
  - Criar script de teste rápido
  - Verificar que `UNIVERSAL_AVAILABLE = True`
  - Testar inicialização de `SEVEHybridFramework` em modo UNIVERSAL

**Critérios de Aceitação:**
- ✅ Zero imports de `seve_universal` externo
- ✅ Modo HYBRID inicializa corretamente
- ✅ `UNIVERSAL_AVAILABLE = True` sempre (exceto erros de import)

---

## 🧪 Fase 2: Crítico - Testes (Prioridade ALTA)

**Status**: 🔴 **PENDENTE** (0% cobertura)  
**Estimativa Total**: 5-7 dias  
**Dependências**: Fase 1.1 completa

### 2.1 Testes Unitários - Core Universal

**Estimativa**: 2 dias

#### Tarefas:
- [ ] **T2.1.1**: Criar `tests/test_universal_core.py`
  - Testar `SEVEUniversalCore` initialization
  - Testar `process_universal_context()`
  - Testar `switch_domain()`
  - Testar `get_domain_metrics()`
  - Mock de adaptadores

- [ ] **T2.1.2**: Testar `DomainConfig` e `UniversalContext`
  - Validação de campos obrigatórios
  - Serialização/deserialização
  - Type safety

- [ ] **T2.1.3**: Testar `DomainAdapterRegistry`
  - Registro de adaptadores
  - Recuperação de adaptadores
  - Adaptadores customizados

- [ ] **T2.1.4**: Testar `UniversalLearningModule` e `TransferLearningEngine`
  - `update_knowledge()`
  - `apply_transfer()`
  - Mock de contextos

- [ ] **T2.1.5**: Testar `UniversalContextManager`
  - `store_context()`
  - `analyze_patterns()`
  - Persistência de histórico

**Critérios de Aceitação:**
- ✅ Cobertura > 80% para `universal/core.py`
- ✅ Todos os testes passando
- ✅ CI/CD validando

---

### 2.2 Testes Unitários - Adaptadores

**Estimativa**: 2 dias

#### Tarefas:
- [ ] **T2.2.1**: Criar `tests/test_universal_adapters.py`
  - Testar cada adaptador individualmente (8 adaptadores)
  - Testar `adapt_to_context()` para cada domínio
  - Testar `extract_domain_features()` com dados reais
  - Testar `apply_domain_rules()` com decisões variadas

- [ ] **T2.2.2**: Testar `UniversalAdapterRegistry`
  - Listagem de domínios disponíveis
  - Recuperação de adaptadores por domínio
  - Registro de adaptadores customizados
  - Validação de capabilities

- [ ] **T2.2.3**: Testes de integração adaptadores + core
  - Processar contexto com adaptador ativo
  - Mudança de domínio em runtime
  - Verificar que metadados são aplicados corretamente

**Critérios de Aceitação:**
- ✅ Cobertura > 85% para `universal/adapters.py`
- ✅ Cada adaptador testado isoladamente
- ✅ Integração com core validada

---

### 2.3 Testes Unitários - Empathy Engine

**Estimativa**: 1-2 dias

#### Tarefas:
- [ ] **T2.3.1**: Criar `tests/test_universal_empathy.py`
  - Testar `UniversalEmpathyEngine` initialization
  - Testar `generate_universal_empathy()` com diferentes contextos
  - Testar detecção de pistas emocionais
  - Testar geração de mensagens empáticas
  - Testar adaptação cultural

- [ ] **T2.3.2**: Testar templates e padrões culturais
  - Validar que templates são aplicados corretamente
  - Testar adaptação para Brasil, USA, Japão, Global
  - Validar que mensagens são culturalmente apropriadas

- [ ] **T2.3.3**: Testar `DomainEmpathyEngine` (ABC)
  - Criar mock engine para teste
  - Validar interface de contrato
  - Testar registro e uso

- [ ] **T2.3.4**: Testar histórico de respostas
  - `response_history` é mantido corretamente
  - `export_history()` funciona

**Critérios de Aceitação:**
- ✅ Cobertura > 80% para `universal/empathy.py`
- ✅ Templates culturais validados
- ✅ Detecção emocional testada

---

### 2.4 Testes Unitários - Universal Ethics Engine

**Estimativa**: 1-2 dias  
**Dependências**: T1.1 completa

#### Tarefas:
- [ ] **T2.4.1**: Criar `tests/test_universal_ethics.py`
  - Testar `UniversalEthicsEngine` initialization
  - Testar `assess_universal_compliance()`
  - Testar avaliação de regras universais
  - Testar avaliação de regras específicas de domínio

- [ ] **T2.4.2**: Testar princípios éticos
  - Testar `PRIVACY`, `FAIRNESS`, `TRANSPARENCY`, etc.
  - Validar scores de conformidade
  - Testar identificação de violações críticas

- [ ] **T2.4.3**: Testar integração com domínios
  - Testar avaliação para Healthcare
  - Testar avaliação para Education
  - Validar que regras específicas são aplicadas

**Critérios de Aceitação:**
- ✅ Cobertura > 80% para `universal/ethics.py`
- ✅ Princípios éticos validados
- ✅ Integração com domínios testada

---

### 2.5 Testes de Integração

**Estimativa**: 2-3 dias  
**Dependências**: Fase 2.1-2.4 completa

#### Tarefas:
- [ ] **T2.5.1**: Criar `tests/test_hybrid_mode_integration.py`
  - Testar modo HYBRID (v3.0 + Universal juntos)
  - Testar que ambos os cores funcionam simultaneamente
  - Testar fallback quando Universal falha
  - Testar uso seletivo (quando usar cada core)

- [ ] **T2.5.2**: Criar `tests/test_domain_switching.py`
  - Testar mudança dinâmica de domínio em runtime
  - Validar que adaptadores são trocados corretamente
  - Testar preservação de contexto durante troca
  - Testar múltiplas trocas sequenciais

- [ ] **T2.5.3**: Criar `tests/test_empathy_integration.py`
  - Testar empatia integrada ao pipeline v3.0
  - Testar empatia integrada ao pipeline universal
  - Validar que respostas empáticas são geradas no momento certo
  - Testar integração com diferentes domínios

- [ ] **T2.5.4**: Criar `tests/test_ethics_integration.py`
  - Testar UniversalEthicsEngine + GuardFlow juntos
  - Validar que avaliações não conflitam
  - Testar priorização de regras
  - Validar que bloqueios funcionam corretamente

**Critérios de Aceitação:**
- ✅ Modo HYBRID funcional e testado
- ✅ Mudança de domínio validada
- ✅ Integrações sem conflitos

---

### 2.6 Testes End-to-End

**Estimativa**: 2-3 dias  
**Dependências**: Fase 2.5 completa

#### Tarefas:
- [ ] **T2.6.1**: Criar `tests/e2e/test_healthcare_e2e.py`
  - Pipeline completo Healthcare
  - Dados médicos simulados
  - Validação ética HIPAA
  - Empatia contextualizada
  - Resultado final validado

- [ ] **T2.6.2**: Criar `tests/e2e/test_education_e2e.py`
  - Pipeline completo Education
  - Dados estudantis simulados
  - Validação ética educacional
  - Empatia pedagógica
  - Resultado final validado

- [ ] **T2.6.3**: Criar `tests/e2e/test_retail_e2e.py`
  - Pipeline completo Retail
  - Dados de compra simulados
  - Validação ESG
  - Empatia ao cliente
  - Resultado final validado

**Critérios de Aceitação:**
- ✅ 3 casos E2E completos e funcionais
- ✅ Validado com dados realistas
- ✅ Performance aceitável

---

## 📚 Fase 3: Documentação (Prioridade MÉDIA)

**Status**: 🟡 **PARCIAL** (40% completo)  
**Estimativa Total**: 4-5 dias  
**Dependências**: Fase 1 e 2 para precisão técnica

### 3.1 Documentação de API

**Estimativa**: 2 dias

#### Tarefas:
- [ ] **T3.1.1**: Atualizar `docs/api/README.md`
  - Adicionar seção "Universal Components"
  - Documentar `SEVEUniversalCore` API
  - Documentar `UniversalEmpathyEngine` API
  - Documentar `UniversalEthicsEngine` API
  - Documentar `DomainConfig` e `UniversalContext`

- [ ] **T3.1.2**: Criar `docs/api/universal/SEVEUniversalCore.md`
  - Documentação completa do núcleo universal
  - Métodos públicos
  - Exemplos de uso
  - Parâmetros e retornos

- [ ] **T3.1.3**: Criar `docs/api/universal/UniversalEmpathyEngine.md`
  - Documentação completa do motor de empatia
  - Tipos de empatia
  - Templates culturais
  - Exemplos práticos

- [ ] **T3.1.4**: Criar `docs/api/universal/UniversalEthicsEngine.md`
  - Documentação completa do motor ético universal
  - Princípios éticos
  - Níveis de conformidade
  - Integração com GuardFlow

- [ ] **T3.1.5**: Criar `docs/api/universal/DomainAdapters.md`
  - Documentação de todos os 8 adaptadores
  - Quando usar cada um
  - Como criar adaptadores customizados
  - Exemplos por domínio

**Critérios de Aceitação:**
- ✅ APIs universais completamente documentadas
- ✅ Exemplos práticos incluídos
- ✅ Type hints refletidos na documentação

---

### 3.2 Guias de Uso

**Estimativa**: 2 dias

#### Tarefas:
- [ ] **T3.2.1**: Criar `docs/universal/DOMAIN_ADAPTERS_GUIDE.md`
  - Guia completo de uso dos adaptadores
  - Como escolher o adaptador correto
  - Como registrar adaptadores customizados
  - Exemplos práticos por domínio
  - Troubleshooting comum

- [ ] **T3.2.2**: Criar `docs/universal/EMPATHY_ENGINE_GUIDE.md`
  - Como usar o motor de empatia
  - Configuração de templates culturais
  - Personalização de respostas empáticas
  - Integração com diferentes domínios
  - Exemplos práticos

- [ ] **T3.2.3**: Criar `docs/universal/UNIVERSAL_MODE_GUIDE.md`
  - Como usar modo UNIVERSAL
  - Quando usar UNIVERSAL vs v3.0 vs HYBRID
  - Configuração de domínios
  - Mudança dinâmica de domínio
  - Boas práticas

- [ ] **T3.2.4**: Atualizar `docs/integration/INTEGRATION_GUIDE.md`
  - Adicionar seção "Universal Domain Integration"
  - Exemplos de integração por domínio
  - Integração com sistemas existentes
  - Casos de uso específicos

**Critérios de Aceitação:**
- ✅ Guias completos e práticos
- ✅ Exemplos funcionais
- ✅ Troubleshooting incluído

---

### 3.3 Exemplos Práticos

**Estimativa**: 1 dia

#### Tarefas:
- [ ] **T3.3.1**: Criar `examples/universal/healthcare_example.py`
  - Exemplo completo Healthcare
  - Dados médicos simulados
  - Empatia contextualizada
  - Validação ética HIPAA
  - Output formatado

- [ ] **T3.3.2**: Criar `examples/universal/education_example.py`
  - Exemplo completo Education
  - Dados estudantis simulados
  - Empatia pedagógica
  - Validação ética educacional
  - Output formatado

- [ ] **T3.3.3**: Criar `examples/universal/retail_example.py`
  - Exemplo completo Retail
  - Dados de compra simulados
  - Empatia ao cliente
  - Validação ESG
  - Output formatado

- [ ] **T3.3.4**: Criar `examples/universal/hybrid_mode_example.py`
  - Exemplo de modo HYBRID
  - Uso simultâneo de v3.0 + Universal
  - Demonstração de quando usar cada core
  - Output comparativo

**Critérios de Aceitação:**
- ✅ 4 exemplos completos e funcionais
- ✅ Código documentado
- ✅ README atualizado com links

---

### 3.4 ADR e Decisões Arquiteturais

**Estimativa**: 1 dia

#### Tarefas:
- [ ] **T3.4.1**: Criar `docs/adr/ADR-008-universal-integration.md`
  - **Contexto**: Por que integrar módulos legados
  - **Decisão**: Integração completa dos módulos universais
  - **Consequências**: Positivas e negativas
  - **Alternativas consideradas**: Manter separado, refatorar do zero
  - **Referências**: Análise de impacto, documentação legado

- [ ] **T3.4.2**: Atualizar `docs/adr/README.md`
  - Adicionar link para ADR-008
  - Atualizar índice

**Critérios de Aceitação:**
- ✅ ADR-008 completo e aprovado
- ✅ Decisão bem justificada
- ✅ Consequências documentadas

---

### 3.5 Atualização de Documentos Existentes

**Estimativa**: 1 dia

#### Tarefas:
- [ ] **T3.5.1**: Atualizar `README.md`
  - Adicionar seção "Universal Domain Adaptation"
  - Exemplos de uso dos módulos universais
  - Links para documentação específica
  - Atualizar seção de capacidades

- [ ] **T3.5.2**: Atualizar `docs/FAQ.md`
  - Adicionar Q&As sobre modo UNIVERSAL
  - Q&As sobre adaptadores de domínio
  - Q&As sobre empatia computacional
  - Q&As sobre ética multi-domínio

- [ ] **T3.5.3**: Atualizar `docs/TROUBLESHOOTING.md`
  - Problemas comuns com módulos universais
  - Erros de importação
  - Problemas de performance em modo UNIVERSAL
  - Troubleshooting de adaptadores

- [ ] **T3.5.4**: Atualizar `EAP_SEVE_UNIVERSAL_V1.md`
  - Marcar capacidades como "implementadas" vs "planejadas"
  - Atualizar métricas com dados reais
  - Adicionar seção de status de integração

**Critérios de Aceitação:**
- ✅ Todos os documentos principais atualizados
- ✅ Informação consistente entre documentos
- ✅ Links funcionais

---

## ⚡ Fase 4: Performance e Otimização (Prioridade BAIXA)

**Status**: 🟢 **OPCIONAL**  
**Estimativa Total**: 3-4 dias  
**Dependências**: Fase 2 completa para baseline

### 4.1 Benchmarks

**Estimativa**: 2 dias

#### Tarefas:
- [ ] **T4.1.1**: Criar `tests/benchmarks/test_universal_performance.py`
  - Benchmark de inicialização (modo UNIVERSAL vs v3.0)
  - Benchmark de processamento por domínio
  - Benchmark de mudança de domínio
  - Benchmark de empatia engine

- [ ] **T4.1.2**: Executar benchmarks e documentar
  - Comparar performance modo UNIVERSAL vs v3.0
  - Identificar gargalos
  - Documentar resultados em `docs/performance/BENCHMARKS.md`
  - Comparar com métricas anteriores

- [ ] **T4.1.3**: Análise de uso de memória
  - Medir RAM por modo
  - Medir overhead por adaptador
  - Documentar requisitos mínimos atualizados

**Critérios de Aceitação:**
- ✅ Benchmarks executados e documentados
- ✅ Performance dentro de limites aceitáveis (< 10% overhead)
- ✅ Métricas comparáveis publicadas

---

### 4.2 Otimizações (se necessário)

**Estimativa**: 1-2 dias (condicional)

#### Tarefas:
- [ ] **T4.2.1**: Identificar otimizações necessárias
  - Analisar resultados de benchmarks
  - Identificar gargalos de performance
  - Priorizar otimizações

- [ ] **T4.2.2**: Implementar otimizações (se necessário)
  - Cache de adaptadores
  - Lazy loading de módulos
  - Otimização de templates de empatia
  - Outras melhorias identificadas

- [ ] **T4.2.3**: Validar otimizações
  - Re-executar benchmarks
  - Validar que otimizações melhoraram performance
  - Garantir que não quebraram funcionalidades

**Critérios de Aceitação:**
- ✅ Performance dentro de limites aceitáveis
- ✅ Funcionalidades mantidas
- ✅ Benchmarks melhorados (se aplicável)

---

## 🔍 Fase 5: Validação e Qualidade (Prioridade MÉDIA)

**Status**: 🟡 **PARCIAL**  
**Estimativa Total**: 2-3 dias  
**Dependências**: Fase 1, 2, 3 completas

### 5.1 Code Review e Qualidade

**Estimativa**: 1 dia

#### Tarefas:
- [ ] **T5.1.1**: Code review completo dos módulos universais
  - Revisar `universal/core.py`
  - Revisar `universal/adapters.py`
  - Revisar `universal/empathy.py`
  - Revisar `universal/ethics.py` (quando criado)
  - Identificar melhorias de código

- [ ] **T5.1.2**: Executar linters
  - `ruff check` ou equivalente
  - `mypy` para type checking
  - Corrigir todos os warnings

- [ ] **T5.1.3**: Verificar cobertura de testes
  - Executar `pytest --cov`
  - Garantir cobertura > 80% para módulos universais
  - Identificar gaps de cobertura

**Critérios de Aceitação:**
- ✅ Zero erros de linting
- ✅ Zero erros de type checking
- ✅ Cobertura > 80%

---

### 5.2 Validação End-to-End

**Estimativa**: 1 dia

#### Tarefas:
- [ ] **T5.2.1**: Testar fluxo completo de desenvolvimento
  - Instalação do framework
  - Uso básico modo v3.0 (backward compatibility)
  - Uso básico modo UNIVERSAL
  - Uso básico modo HYBRID
  - Validar que tudo funciona

- [ ] **T5.2.2**: Validar documentação
  - Seguir todos os guias criados
  - Validar que exemplos funcionam
  - Identificar inconsistências
  - Corrigir erros encontrados

**Critérios de Aceitação:**
- ✅ Fluxo completo funcional
- ✅ Documentação precisa e testável
- ✅ Exemplos funcionam sem erros

---

### 5.3 Checklist de Release

**Estimativa**: 1 dia

#### Tarefas:
- [ ] **T5.3.1**: Validar checklist de release
  - [ ] Todos os testes passando
  - [ ] Cobertura de testes > 80%
  - [ ] Documentação completa
  - [ ] Exemplos funcionais
  - [ ] Benchmarks executados
  - [ ] Performance aceitável
  - [ ] Zero breaking changes
  - [ ] CHANGELOG atualizado
  - [ ] Versão atualizada (se necessário)

- [ ] **T5.3.2**: Preparar release notes
  - Listar novas funcionalidades
  - Documentar mudanças
  - Listar breaking changes (se houver)
  - Instruções de migração

**Critérios de Aceitação:**
- ✅ Checklist completo
- ✅ Release notes preparados
- ✅ Pronto para release

---

## 📊 Métricas de Progresso

### Status por Fase

| Fase | Tarefas | Concluídas | Pendentes | Progresso |
|------|---------|------------|-----------|-----------|
| **Fase 1: Core** | 9 | 3 | 6 | 🟡 33% |
| **Fase 2: Testes** | 21 | 0 | 21 | 🔴 0% |
| **Fase 3: Documentação** | 19 | 2 | 17 | 🟡 11% |
| **Fase 4: Performance** | 6 | 0 | 6 | 🟢 0% (opcional) |
| **Fase 5: Validação** | 6 | 0 | 6 | 🟡 0% |
| **TOTAL** | **61** | **5** | **56** | **🟡 8%** |

### Priorização

**🔴 Crítico (Fazer primeiro):**
- Fase 1.1: Integração UniversalEthicsEngine
- Fase 1.2: Atualização de Imports
- Fase 2: Todos os testes

**🟡 Importante (Fazer depois):**
- Fase 3: Documentação completa
- Fase 5: Validação e qualidade

**🟢 Desejável (Opcional):**
- Fase 4: Performance e otimização (apenas se necessário)

---

## 🎯 Critérios de Conclusão

A integração será considerada **COMPLETA** quando:

- ✅ **Funcionalidade**: Todos os módulos universais funcionais
- ✅ **Testes**: Cobertura > 80%, todos os testes passando
- ✅ **Documentação**: APIs, guias e exemplos completos
- ✅ **Integração**: UniversalEthicsEngine integrado com GuardFlow
- ✅ **Qualidade**: Zero erros de linting, type checking OK
- ✅ **Performance**: Overhead < 10% comparado ao baseline
- ✅ **Backward Compatibility**: Modo v3.0 ainda funciona perfeitamente

---

## 📝 Notas Importantes

1. **Ordem de Execução**: Seguir ordem das fases (1 → 2 → 3 → 5 → 4)
2. **Dependências**: Respeitar dependências entre tarefas
3. **Testes Primeiro**: Sempre escrever testes junto com código novo
4. **Documentação Contínua**: Atualizar documentação à medida que desenvolve
5. **Commits Atômicos**: Fazer commits pequenos e frequentes
6. **Code Review**: Revisar código antes de marcar como completo

---

**Última Atualização**: 2025-01-29  
**Próxima Revisão**: A cada conclusão de fase
