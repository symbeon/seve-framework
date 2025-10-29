const crypto = require('crypto');

// Gerar chave privada de teste
const privateKey = crypto.randomBytes(32).toString('hex');

console.log('🔑 Chave Privada de Teste Gerada:');
console.log('Private Key:', privateKey);
console.log('');
console.log('⚠️  ATENÇÃO: Esta é uma chave de TESTE apenas!');
console.log('⚠️  NUNCA use esta chave para carteiras com valor real!');
console.log('');
console.log('📝 Adicione esta chave ao arquivo .env:');
console.log(`PRIVATE_KEY=${privateKey}`);
