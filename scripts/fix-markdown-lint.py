#!/usr/bin/env python3
"""
Script para corrigir automaticamente problemas de markdownlint
Corrige: espaços em branco, listas, cabeçalhos, code blocks, etc.
"""

import re
import os
from pathlib import Path

def fix_trailing_spaces(content):
    """Remove trailing spaces (MD009)"""
    lines = content.split('\n')
    fixed = []
    for line in lines:
        # Remove trailing spaces, mas mantém linhas vazias
        if line.strip():
            fixed.append(line.rstrip())
        else:
            fixed.append('')
    return '\n'.join(fixed)

def fix_blanks_around_lists(content):
    """Adiciona linhas em branco ao redor de listas (MD032)"""
    lines = content.split('\n')
    fixed = []
    prev_was_list = False
    prev_was_empty = False
    
    for i, line in enumerate(lines):
        is_list = bool(re.match(r'^\s*[-*+]\s+|^\s*\d+\.\s+', line))
        is_empty = not line.strip()
        
        # Se encontrou uma lista e a linha anterior não era lista nem vazia
        if is_list and not prev_was_list and not prev_was_empty and i > 0:
            # Adiciona linha em branco antes se necessário
            if fixed and fixed[-1].strip():
                fixed.append('')
        
        fixed.append(line)
        
        # Se era lista e a próxima não é lista nem vazia, adiciona linha em branco depois
        if is_list and i < len(lines) - 1:
            next_line = lines[i + 1] if i + 1 < len(lines) else ''
            next_is_list = bool(re.match(r'^\s*[-*+]\s+|^\s*\d+\.\s+', next_line))
            next_is_empty = not next_line.strip()
            if not next_is_list and not next_is_empty and next_line.strip():
                # Adiciona linha em branco depois
                if fixed[-1].strip():
                    fixed.append('')
        
        prev_was_list = is_list
        prev_was_empty = is_empty
    
    return '\n'.join(fixed)

def fix_blanks_around_headings(content):
    """Adiciona linhas em branco ao redor de cabeçalhos (MD022)"""
    lines = content.split('\n')
    fixed = []
    
    for i, line in enumerate(lines):
        is_heading = bool(re.match(r'^#+\s+', line))
        
        if is_heading:
            # Adiciona linha em branco antes se necessário
            if fixed and fixed[-1].strip():
                fixed.append('')
            fixed.append(line)
            # Adiciona linha em branco depois se necessário
            if i < len(lines) - 1 and lines[i + 1].strip():
                fixed.append('')
        else:
            fixed.append(line)
    
    return '\n'.join(fixed)

def fix_blanks_around_fences(content):
    """Adiciona linhas em branco ao redor de code blocks (MD031)"""
    lines = content.split('\n')
    fixed = []
    in_code_block = False
    
    for i, line in enumerate(lines):
        is_fence = line.strip().startswith('```')
        
        if is_fence:
            if not in_code_block:
                # Início do code block
                if fixed and fixed[-1].strip():
                    fixed.append('')
            else:
                # Fim do code block
                fixed.append(line)
                if i < len(lines) - 1 and lines[i + 1].strip():
                    fixed.append('')
                in_code_block = False
                continue
            
            in_code_block = True
        
        fixed.append(line)
    
    return '\n'.join(fixed)

def fix_fenced_code_language(content):
    """Adiciona linguagem aos code blocks quando ausente (MD040)"""
    lines = content.split('\n')
    fixed = []
    in_code_block = False
    code_block_start = -1
    
    for i, line in enumerate(lines):
        is_fence = line.strip().startswith('```')
        
        if is_fence:
            if not in_code_block:
                # Início do code block
                code_block_start = i
                fence_line = line.strip()
                # Se não tem linguagem especificada
                if fence_line == '```' or fence_line == '``` ':
                    # Tenta inferir da próxima linha ou usa 'text'
                    if i + 1 < len(lines):
                        next_line = lines[i + 1].strip()
                        # Inferência básica
                        if any(keyword in next_line for keyword in ['python', 'import', 'def ', 'class ']):
                            fixed.append('```python')
                        elif any(keyword in next_line for keyword in ['javascript', 'const ', 'function ', 'require']):
                            fixed.append('```javascript')
                        elif any(keyword in next_line for keyword in ['bash', 'npm', 'pip', 'git']):
                            fixed.append('```bash')
                        elif any(keyword in next_line for keyword in ['solidity', 'contract ', 'pragma']):
                            fixed.append('```solidity')
                        else:
                            fixed.append('```text')
                    else:
                        fixed.append('```text')
                else:
                    fixed.append(line)
                in_code_block = True
            else:
                # Fim do code block
                fixed.append(line)
                in_code_block = False
        else:
            fixed.append(line)
    
    return '\n'.join(fixed)

def fix_multiple_blanks(content):
    """Remove múltiplas linhas em branco consecutivas (MD012)"""
    # Substitui 3+ linhas em branco por 2
    content = re.sub(r'\n{3,}', '\n\n', content)
    return content

def fix_bare_urls(content):
    """Converte URLs bare em links markdown (MD034)"""
    # Padrão para URLs
    url_pattern = r'(?<!\]\()(https?://[^\s\)]+)'
    
    def replace_url(match):
        url = match.group(1)
        # Remove trailing punctuation
        url = url.rstrip('.,;:!?')
        return f'[{url}]({url})'
    
    content = re.sub(url_pattern, replace_url, content)
    return content

def fix_emphasis_as_heading(content):
    """Converte ênfase usada como heading em heading real (MD036)"""
    lines = content.split('\n')
    fixed = []
    
    for line in lines:
        # Se linha começa com ** ou * e termina com ** ou *, pode ser heading
        if re.match(r'^\*\*[^*]+\*\*$', line.strip()) or re.match(r'^\*[^*]+\*$', line.strip()):
            # Verifica se próxima linha é lista (indica que deveria ser heading)
            idx = len(fixed)
            if idx < len(lines) - 1:
                next_line = lines[idx + 1] if idx + 1 < len(lines) else ''
                if re.match(r'^\s*[-*+]\s+|^\s*\d+\.\s+', next_line):
                    # Converte para heading
                    text = re.sub(r'\*\*?([^*]+)\*\*?', r'\1', line.strip())
                    fixed.append(f'### {text}')
                    continue
        
        fixed.append(line)
    
    return '\n'.join(fixed)

def process_file(file_path):
    """Processa um arquivo Markdown"""
    print(f"Processando: {file_path}")
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original = content
        
        # Aplica correções
        content = fix_trailing_spaces(content)
        content = fix_blanks_around_lists(content)
        content = fix_blanks_around_headings(content)
        content = fix_blanks_around_fences(content)
        content = fix_fenced_code_language(content)
        content = fix_multiple_blanks(content)
        content = fix_bare_urls(content)
        content = fix_emphasis_as_heading(content)
        
        # Remove trailing newlines extras
        content = content.rstrip() + '\n'
        
        if content != original:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"  ✅ Corrigido")
            return True
        else:
            print(f"  ⏭️  Sem alterações")
            return False
    except Exception as e:
        print(f"  ❌ Erro: {e}")
        return False

def main():
    """Função principal"""
    base_dir = Path(__file__).parent.parent
    
    # Arquivos para corrigir
    files_to_fix = [
        base_dir / "COMMIT_PLAN.md",
        base_dir / "docs" / "PASSO_A_PASSO_DEPLOY.md",
        base_dir / "docs" / "GUIA_SALDO_METAMASK.md",
        base_dir / "docs" / "ANALISE_CUSTO_MAINNET.md",
        base_dir / "docs" / "ANALISE_ESTRATEGICA_DEPLOY.md",
        base_dir / "docs" / "TROUBLESHOOTING_CONVERSAO.md",
        base_dir / "docs" / "ESTRATEGIA_SALDO_ATUAL.md",
        base_dir / "docs" / "artigos" / "SEVE_FRAMEWORK_TECHNICAL_PAPER.md",
    ]
    
    print("🔧 Corrigindo problemas de markdownlint...\n")
    
    fixed_count = 0
    for file_path in files_to_fix:
        if file_path.exists():
            if process_file(file_path):
                fixed_count += 1
        else:
            print(f"⚠️  Arquivo não encontrado: {file_path}")
    
    print(f"\n✅ Correção concluída: {fixed_count} arquivo(s) corrigido(s)")

if __name__ == "__main__":
    main()

