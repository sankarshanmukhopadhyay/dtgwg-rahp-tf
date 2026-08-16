#!/usr/bin/env node
import {readFileSync,readdirSync,existsSync} from 'node:fs'; import path from 'node:path'; import {loadProfile,validateProfile,validateNormalizedResult,loadResult,retentionPlan,sha256} from '@rahp/core'; import {RahpGraph} from '@rahp/graph';
const root=process.cwd();const [cmd,...a]=process.argv.slice(2);const die=(m:string,c=1)=>{console.error(m);process.exit(c)};
if(cmd==='validate-result'){const r=validateNormalizedResult(a[0]);console.log(r.valid?`VALID ${a[0]}`:`INVALID ${a[0]}\n  - ${r.errors.join('\n  - ')}`);process.exit(r.valid?0:1)}
if(cmd==='retention-plan'){const r=validateNormalizedResult(a[0]);if(!r.valid)die(r.errors.join('\n'));console.log(JSON.stringify(retentionPlan(loadResult(a[0])),null,2))}
if(cmd==='sha256')console.log(sha256(a[0]));
if(cmd==='validate-profile'){const r=validateProfile(a[0]);console.log(r.valid?`VALID ${a[0]}`:`INVALID ${a[0]}\n  - ${r.errors.join('\n  - ')}`);process.exit(r.valid?0:1)}
if(cmd==='targets'){console.log(JSON.stringify(loadProfile(a[0]).repositories,null,2))}
if(cmd==='graph-stats'){const f=a[0]||'build/rahp.json';console.log(JSON.stringify(RahpGraph.fromRahpJson(f).stats(),null,2))}
if(cmd==='trace'){const f=a[1]||'build/rahp.json';if(!existsSync(f))die(`missing ${f}`);console.log(JSON.stringify(RahpGraph.fromRahpJson(f).trace(a[0],Number(a[2]||2)),null,2))}
if(cmd==='conformance'){const base=path.join(root,'tests/conformance/engine');let fail=0,total=0;for(const d of readdirSync(base)){const rf=path.join(base,d,'result.json'),ef=path.join(base,d,'expected.yaml');if(!existsSync(rf)||!existsSync(ef))continue;total++;const expected=/valid:\s*true/.test(readFileSync(ef,'utf8'));const actual=validateNormalizedResult(rf).valid;if(actual!==expected){console.error(`FAIL ${d}: expected ${expected}, got ${actual}`);fail++}else console.log(`PASS ${d}`)}console.log(`TypeScript conformance: ${total-fail}/${total} fixtures`);process.exit(fail?1:0)}
if(!cmd||cmd==='describe'){console.log('RAHP TypeScript reference SDK v0.9.0\nCommands: validate-profile targets validate-result retention-plan sha256 trace graph-stats conformance')}
