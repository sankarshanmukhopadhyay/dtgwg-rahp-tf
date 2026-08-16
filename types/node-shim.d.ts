declare module 'node:fs' { export const readFileSync:any; export const readdirSync:any; export const existsSync:any; }
declare module 'node:path' { const x:any; export default x; }
declare module 'node:crypto' { export const createHash:any; }
declare var process:any;
