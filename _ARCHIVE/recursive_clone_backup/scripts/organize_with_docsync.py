#!/usr/bin/env python3
"""
Script para organizar arquivos do SEVE Framework usando configuração DOCSYNC.

Este script organiza os arquivos do framework baseado na configuração
docsync.yaml, movendo arquivos para suas localizações apropriadas.

Author: SEVE Framework Team
Date: 2025-11-07
"""

import os
import shutil
import yaml
from pathlib import Path
from typing import Dict, List, Optional
import logging

# Configuração de logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class SEVEOrganizer:
    """Organizador de arquivos do SEVE Framework."""
    
    def __init__(self, config_path: Path):
        """Inicializa o organizador com configuração.
        
        Args:
            config_path: Caminho para o arquivo docsync.yaml
        """
        self.config_path = Path(config_path).resolve()
        self.config: Optional[Dict] = None
        # Usa o diretório onde o config está como root, ou o diretório atual
        if self.config_path.is_absolute():
            self.root_dir = self.config_path.parent
        else:
            self.root_dir = Path.cwd()
        self.moved_files: List[tuple] = []
        
    def load_config(self) -> bool:
        """Carrega a configuração do arquivo YAML.
        
        Returns:
            bool: True se carregado com sucesso
        """
        try:
            with open(self.config_path, 'r', encoding='utf-8') as f:
                self.config = yaml.safe_load(f)
            logger.info(f"Configuração carregada de {self.config_path}")
            return True
        except Exception as e:
            logger.error(f"Erro ao carregar configuração: {e}")
            return False
    
    def should_exclude(self, file_path: Path) -> bool:
        """Verifica se um arquivo deve ser excluído.
        
        Args:
            file_path: Caminho do arquivo
            
        Returns:
            bool: True se deve ser excluído
        """
        exclude_patterns = self.config.get('exclude_globally', [])
        
        # Converte para Path relativo
        try:
            rel_path = file_path.relative_to(self.root_dir)
            path_str = str(rel_path).replace('\\', '/')
        except ValueError:
            return True  # Arquivo fora do root
        
        for pattern in exclude_patterns:
            # Converte padrão glob para verificação simples
            pattern_clean = pattern.replace('**/', '').replace('**', '')
            if pattern_clean in path_str or path_str.endswith(pattern_clean):
                return True
        
        return False
    
    def organize_root_files(self, dry_run: bool = False) -> int:
        """Organiza arquivos na raiz do projeto.
        
        Args:
            dry_run: Se True, apenas simula sem mover arquivos
            
        Returns:
            int: Número de arquivos organizados
        """
        if 'root_files' not in self.config:
            return 0
        
        root_config = self.config['root_files']
        organization = root_config.get('organization', {})
        move_to = organization.get('move_to', 'docs/root/')
        keep_in_root = organization.get('keep_in_root', ['README.md', 'LICENSE'])
        
        moved_count = 0
        target_dir = self.root_dir / move_to
        target_dir.mkdir(parents=True, exist_ok=True)
        
        # Lista arquivos na raiz
        for file_path in self.root_dir.iterdir():
            if not file_path.is_file():
                continue
            
            if self.should_exclude(file_path):
                continue
            
            file_name = file_path.name
            
            # Verifica se deve manter na raiz
            if file_name in keep_in_root:
                continue
            
            # Verifica padrões de arquivos raiz
            if file_name.endswith('.md') or file_name in root_config.get('files', []):
                target_path = target_dir / file_name
                
                if not dry_run:
                    if target_path.exists():
                        logger.warning(f"Arquivo já existe: {target_path}")
                    else:
                        shutil.move(str(file_path), str(target_path))
                        self.moved_files.append((str(file_path), str(target_path)))
                        logger.info(f"Movido: {file_name} -> {move_to}")
                else:
                    logger.info(f"[DRY RUN] Moveria: {file_name} -> {move_to}")
                
                moved_count += 1
        
        return moved_count
    
    def organize_directories(self, dry_run: bool = False) -> int:
        """Organiza arquivos dentro dos diretórios configurados.
        
        Args:
            dry_run: Se True, apenas simula sem mover arquivos
            
        Returns:
            int: Número de arquivos organizados
        """
        if 'directories' not in self.config:
            return 0
        
        organized_count = 0
        
        for dir_config in self.config['directories']:
            dir_path = self.root_dir / dir_config['path']
            
            if not dir_path.exists():
                logger.warning(f"Diretório não existe: {dir_path}")
                continue
            
            # Organiza arquivos no diretório
            organized_count += self._organize_directory(dir_path, dir_config, dry_run)
        
        return organized_count
    
    def _organize_directory(self, dir_path: Path, config: Dict, dry_run: bool) -> int:
        """Organiza arquivos em um diretório específico.
        
        Args:
            dir_path: Caminho do diretório
            config: Configuração do diretório
            dry_run: Se True, apenas simula
            
        Returns:
            int: Número de arquivos organizados
        """
        organized_count = 0
        patterns = config.get('patterns', [])
        exclude = config.get('exclude', [])
        organization = config.get('organization', {})
        structure = organization.get('structure', [])
        
        # Processa arquivos no diretório
        for file_path in dir_path.rglob('*'):
            if not file_path.is_file():
                continue
            
            if self.should_exclude(file_path):
                continue
            
            # Verifica padrões
            matches_pattern = False
            for pattern in patterns:
                if file_path.match(pattern):
                    matches_pattern = True
                    break
            
            if not matches_pattern:
                continue
            
            # Verifica exclusões
            should_exclude = False
            for excl_pattern in exclude:
                if file_path.match(excl_pattern):
                    should_exclude = True
                    break
            
            if should_exclude:
                continue
            
            # Aplica regras de organização se houver
            if structure:
                # Por enquanto, apenas loga - estrutura pode ser implementada depois
                logger.debug(f"Arquivo encontrado: {file_path}")
                organized_count += 1
        
        return organized_count
    
    def run(self, dry_run: bool = False) -> Dict:
        """Executa a organização completa.
        
        Args:
            dry_run: Se True, apenas simula sem mover arquivos
            
        Returns:
            Dict: Estatísticas da organização
        """
        if not self.load_config():
            return {'success': False, 'error': 'Failed to load config'}
        
        logger.info("Iniciando organização do SEVE Framework...")
        if dry_run:
            logger.info("MODO DRY RUN - Nenhum arquivo será movido")
        
        stats = {
            'success': True,
            'root_files': 0,
            'directories': 0,
            'total': 0,
            'moved_files': []
        }
        
        # Organiza arquivos raiz
        stats['root_files'] = self.organize_root_files(dry_run)
        
        # Organiza diretórios
        stats['directories'] = self.organize_directories(dry_run)
        
        stats['total'] = stats['root_files'] + stats['directories']
        stats['moved_files'] = self.moved_files
        
        logger.info(f"Organização concluída: {stats['total']} arquivos processados")
        
        return stats


def main():
    """Função principal."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Organiza arquivos do SEVE Framework usando DOCSYNC"
    )
    parser.add_argument(
        '--config',
        type=Path,
        default=Path('docsync.yaml'),
        help='Caminho para arquivo de configuração (default: docsync.yaml)'
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Simula organização sem mover arquivos'
    )
    
    args = parser.parse_args()
    
    if not args.config.exists():
        logger.error(f"Arquivo de configuração não encontrado: {args.config}")
        return 1
    
    organizer = SEVEOrganizer(args.config)
    stats = organizer.run(dry_run=args.dry_run)
    
    if not stats['success']:
        logger.error(f"Erro na organização: {stats.get('error')}")
        return 1
    
    print("\n" + "="*60)
    print("RESUMO DA ORGANIZAÇÃO")
    print("="*60)
    print(f"Arquivos raiz processados: {stats['root_files']}")
    print(f"Diretórios processados: {stats['directories']}")
    print(f"Total: {stats['total']}")
    if stats['moved_files']:
        print(f"\nArquivos movidos: {len(stats['moved_files'])}")
        for src, dst in stats['moved_files'][:10]:  # Mostra apenas os 10 primeiros
            print(f"  {src} -> {dst}")
        if len(stats['moved_files']) > 10:
            print(f"  ... e mais {len(stats['moved_files']) - 10} arquivos")
    print("="*60)
    
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main())

