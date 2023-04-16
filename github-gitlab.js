const { spawnSync } = require('child_process');
const { format } = require('date-fns');

// Obtener la fecha y hora actual en formato deseado
const now = format(new Date(), "dd 'de' MMMM 'de' yyyy - HH:mm:ss", { locale: require('date-fns/locale/es') });

// Mensaje por defecto si no se proporciona uno
const defaultCommitMessage = `Commit realizado el ${now}`;

// Obtener el mensaje y la rama de los argumentos, si se proporcionan
const args = process.argv.slice(2);
const commitMessageIndex = args.indexOf('-m');
const branchIndex = args.indexOf('-b');
const commitMessage = commitMessageIndex !== -1 ? args[commitMessageIndex + 1] : defaultCommitMessage;
const branch = branchIndex !== -1 ? args[branchIndex + 1] : 'main';

// Ejecutar los comandos de git
spawnSync('git', ['add', '.']);
spawnSync('git', ['commit', '-m', commitMessage]);
spawnSync('git', ['push', 'github', branch]);
spawnSync('git', ['push', 'gitlab', branch]);
// spawnSync('git', ['push', 'heroku', branch]);
// spawnSync('heroku', ['open']);
