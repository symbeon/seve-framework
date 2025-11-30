import sys
import os

# Adicionar src ao path
sys.path.append(os.path.join(os.getcwd(), 'src'))

print("🔍 Diagnosticando ambiente Python...")
print(f"Python version: {sys.version}")
print(f"CWD: {os.getcwd()}")
print(f"Path: {sys.path}")

libs = ["numpy", "PIL", "cv2", "requests", "aiohttp"]

print("\n📦 Verificando dependências externas:")
for lib in libs:
    try:
        __import__(lib)
        print(f"  ✅ {lib} instalado")
    except ImportError as e:
        print(f"  ❌ {lib} NÃO instalado ({e})")

print("\n🏗️ Verificando framework:")
try:
    import seve_framework
    print("  ✅ seve_framework importado com sucesso")
except ImportError as e:
    print(f"  ❌ Falha ao importar seve_framework: {e}")
    import traceback
    traceback.print_exc()

print("\n🏁 Diagnóstico concluído.")
