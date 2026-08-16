import {readFileSync} from 'node:fs'; import {createHash} from 'node:crypto'; import type {RahpResult,EvidenceClass,ValidationResult} from '@rahp/schema'; import {validateResult} from '@rahp/schema';
export interface RetentionAction {id:string;class:EvidenceClass;repository:'allowed'|'manifest-only'|'forbidden';retention_days:number|null;action:'commit'|'manifest-only'|'do-not-commit'}
export function loadResult(file:string):RahpResult {return JSON.parse(readFileSync(file,'utf8'))}
export function validateNormalizedResult(file:string):ValidationResult{return validateResult(loadResult(file))}
export function retentionPlan(r:RahpResult){const cfg:any={ephemeral:['forbidden',14],referenced:['manifest-only',365],durable:['allowed',null],exemplar:['allowed',null]}; const actions:RetentionAction[]=r.evidence.map(x=>{const [repository,days]=cfg[x.class];return {id:x.id,class:x.class,repository,retention_days:days,action:repository==='allowed'?'commit':repository==='manifest-only'?'manifest-only':'do-not-commit'}});return {policy:'rahp-evidence-retention-v1',assessment:r.assessment.id,actions}}
export function sha256(file:string){return createHash('sha256').update(readFileSync(file)).digest('hex')}
export interface Target {id:string;repository:string;branch?:string;commit?:string;reviews:string[]}
export function parseProfile(text:string):{profile:{id:string};assessment:any;repositories:Target[]} { // constrained RAHP profile parser, intentionally not a general YAML parser
 const lines=text.split(/\r?\n/); let section=''; let current:any=null; const out:any={profile:{},assessment:{},repositories:[]};
 for(const raw of lines){const line=raw.replace(/\s+#.*$/,''); if(!line.trim())continue; const indent=line.match(/^\s*/)?.[0].length??0; const s=line.trim();
  if(indent===0&&s.endsWith(':')){section=s.slice(0,-1);current=null;continue}
  if(section==='profile'&&indent>=2&&!s.startsWith('- ')){const m=s.match(/^([^:]+):\s*(.*)$/);if(m)out.profile[m[1]]=scalar(m[2])}
  if(section==='assessment'&&indent>=2&&!s.startsWith('- ')){const m=s.match(/^([^:]+):\s*(.*)$/);if(m&&m[2])out.assessment[m[1]]=scalar(m[2])}
  if(section==='repositories'){if(s.startsWith('- id:')){current={id:scalar(s.slice(5).trim()),reviews:[]};out.repositories.push(current);continue} if(current){const m=s.match(/^([^:]+):\s*(.*)$/); if(m&&['repository','branch','commit'].includes(m[1]))current[m[1]]=scalar(m[2]); if(m&&m[1]==='reviews'&&m[2].startsWith('['))current.reviews=scalar(m[2]); else if(s.startsWith('- ')&&raw.match(/^\s{2,}- /)&&['rahp','security','combined'].includes(s.slice(2)))current.reviews.push(s.slice(2));}}
 }
 return out;
}
function scalar(v:string):any{v=v.trim();if(!v)return '';if(v.startsWith('[')&&v.endsWith(']'))return v.slice(1,-1).split(',').map(x=>x.trim().replace(/^['"]|['"]$/g,''));if(v==='true'||v==='false')return v==='true';if(/^\d+$/.test(v))return Number(v);return v.replace(/^['"]|['"]$/g,'')}
export function loadProfile(file:string){return parseProfile(readFileSync(file,'utf8'))}
export function validateProfile(file:string):ValidationResult{const p=loadProfile(file),e:string[]=[];if(!p.profile.id)e.push('profile.id required');if(!p.repositories.length)e.push('repositories must not be empty');for(const [i,r] of p.repositories.entries()){if(!r.id)e.push(`repositories.${i}.id required`);if(!r.repository)e.push(`repositories.${i}.repository required`);if(!r.reviews.length)e.push(`repositories.${i}.reviews required`)}return {valid:!e.length,errors:e}}
