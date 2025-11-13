#!/usr/bin/env python3
"""
Script específico para corrigir problemas de markdownlint no EAP.
"""

import re
from pathlib import Path


def fix_eap_markdown(file_path: Path) -> bool:
    """Corrige problemas de markdownlint no arquivo EAP."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        fixed_lines = []
        i = 0
        
        while i < len(lines):
            line = lines[i].rstrip('\n')
            is_heading = bool(re.match(r'^#{1,6}\s+', line))
            is_list = bool(re.match(r'^[-*+]\s+', line))
            
            # MD022: Heading precisa de linha em branco abaixo
            if is_heading:
                fixed_lines.append(line)
                # Se próxima linha não é vazia e não é heading, adiciona linha em branco
                if i + 1 < len(lines):
                    next_line = lines[i + 1].rstrip('\n')
                    if next_line.strip() and not re.match(r'^#{1,6}\s+', next_line):
                        fixed_lines.append('')
            
            # MD032: Lista precisa de linha em branco acima
            elif is_list:
                # Se linha anterior não é vazia e não é lista, adiciona linha em branco
                if fixed_lines and fixed_lines[-1].strip():
                    prev_line = fixed_lines[-1]
                    if not re.match(r'^[-*+]\s+', prev_line) and not re.match(r'^#{1,6}\s+', prev_line):
                        fixed_lines.append('')
                fixed_lines.append(line)
            
            # Linha normal
            else:
                fixed_lines.append(line)
            
            i += 1
        
        # MD012: Remove múltiplas linhas em branco consecutivas
        result = []
        prev_empty = False
        for line in fixed_lines:
            is_empty = not line.strip()
            if is_empty and prev_empty:
                continue  # Pula linhas em branco duplicadas
            result.append(line)
            prev_empty = is_empty
        
        # Garante uma linha em branco no final
        if result and result[-1].strip():
            result.append('')
        
        # Escreve o arquivo corrigido
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(result))
        
        return True
    except Exception as e:
        print(f"Erro: {e}")
        return False


if __name__ == '__main__':
    eap_path = Path('EAP_SEVE_UNIVERSAL_V1.md')
    if not eap_path.exists():
        # Tenta encontrar na raiz do projeto
        eap_path = Path('../EAP_SEVE_UNIVERSAL_V1.md')
    
    if eap_path.exists():
        if fix_eap_markdown(eap_path):
            print(f"✅ {eap_path} corrigido!")
        else:
            print(f"❌ Erro ao corrigir {eap_path}")
    else:
        print(f"❌ Arquivo não encontrado: {eap_path}")

