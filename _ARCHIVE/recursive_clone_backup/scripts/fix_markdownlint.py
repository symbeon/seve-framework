#!/usr/bin/env python3
"""
Script para corrigir automaticamente problemas comuns de markdownlint.
Foca em MD022 (headings sem linhas em branco) e MD032 (listas sem linhas em branco).
"""

import re
import sys
from pathlib import Path


def fix_md022_md032(content: str) -> str:
    """Corrige MD022 (headings sem linhas em branco) e MD032 (listas sem linhas em branco)."""
    lines = content.split('\n')
    fixed_lines = []
    
    i = 0
    while i < len(lines):
        line = lines[i]
        fixed_lines.append(line)
        
        # MD022: Heading sem linha em branco abaixo
        if re.match(r'^#{1,6}\s+', line):
            # Se próxima linha não é vazia e não é heading, adiciona linha em branco
            if i + 1 < len(lines):
                next_line = lines[i + 1]
                if next_line.strip() and not re.match(r'^#{1,6}\s+', next_line) and not re.match(r'^[-*+]\s+', next_line):
                    fixed_lines.append('')
        
        # MD032: Lista sem linha em branco acima
        if re.match(r'^[-*+]\s+', line):
            # Se linha anterior não é vazia e não é lista, adiciona linha em branco antes
            if len(fixed_lines) > 1:
                prev_line = fixed_lines[-2]
                if prev_line.strip() and not re.match(r'^[-*+]\s+', prev_line) and not re.match(r'^#{1,6}\s+', prev_line):
                    # Remove a linha atual, adiciona linha em branco, depois a linha atual
                    fixed_lines.pop()
                    fixed_lines.append('')
                    fixed_lines.append(line)
        
        i += 1
    
    return '\n'.join(fixed_lines)


def fix_md012(content: str) -> str:
    """Corrige MD012 (múltiplas linhas em branco consecutivas)."""
    # Remove linhas em branco duplicadas no final
    content = content.rstrip()
    # Remove múltiplas linhas em branco consecutivas (mantém apenas uma)
    content = re.sub(r'\n{3,}', '\n\n', content)
    # Garante uma linha em branco no final
    if content and not content.endswith('\n'):
        content += '\n'
    return content


def fix_md036(content: str) -> str:
    """Corrige MD036 (ênfase usada como heading) - converte **texto** em heading quando apropriado."""
    lines = content.split('\n')
    fixed_lines = []
    
    for line in lines:
        # Se linha começa com **texto** seguido de dois pontos, pode ser um heading
        match = re.match(r'^\*\*(\d+\.\s+[^*]+)\*\*$', line)
        if match:
            # Converte para heading nível 4
            heading_text = match.group(1)
            fixed_lines.append(f'##### {heading_text}')
        else:
            fixed_lines.append(line)
    
    return '\n'.join(fixed_lines)


def fix_file(file_path: Path) -> bool:
    """Corrige um arquivo markdown."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Aplica correções
        content = fix_md012(content)
        content = fix_md022_md032(content)
        # Não aplicamos MD036 automaticamente pois pode quebrar formatação
        
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        return False
    except Exception as e:
        print(f"Erro ao processar {file_path}: {e}", file=sys.stderr)
        return False


def main():
    """Função principal."""
    if len(sys.argv) < 2:
        print("Uso: python fix_markdownlint.py <arquivo1> [arquivo2] ...")
        sys.exit(1)
    
    files_fixed = 0
    for file_path_str in sys.argv[1:]:
        file_path = Path(file_path_str)
        if not file_path.exists():
            print(f"Arquivo não encontrado: {file_path}", file=sys.stderr)
            continue
        
        if fix_file(file_path):
            print(f"✅ Corrigido: {file_path}")
            files_fixed += 1
        else:
            print(f"ℹ️  Sem alterações: {file_path}")
    
    print(f"\n📊 Total de arquivos corrigidos: {files_fixed}")


if __name__ == '__main__':
    main()

