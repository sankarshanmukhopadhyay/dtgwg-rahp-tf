import {readFileSync} from 'node:fs';
export interface Node {id:string;kind:string;data:any} export interface Edge {from:string;to:string;relation:string}
export class RahpGraph {
 nodes=new Map<string,Node>(); edges:Edge[]=[];
 static fromRahpJson(file:string){const g=new RahpGraph();const doc=JSON.parse(readFileSync(file,'utf8'));const records=doc.records??doc;for(const [kind,items] of Object.entries(records)){const arr=Array.isArray(items)?items:Object.values(items as any);for(const x of arr as any[]){if(x?.id)g.nodes.set(x.id,{id:x.id,kind,data:x})}}
  for(const n of g.nodes.values())for(const [k,v] of Object.entries(n.data)){if(k==='id')continue;const vals=Array.isArray(v)?v:[v];for(const id of vals)if(typeof id==='string'&&g.nodes.has(id))g.edges.push({from:n.id,to:id,relation:k})}return g}
 trace(id:string,depth=2){const seen=new Set<string>(),out:any[]=[];const walk=(x:string,d:number)=>{if(seen.has(x)||d<0)return;seen.add(x);const n=this.nodes.get(x);if(!n)return;const links=this.edges.filter(e=>e.from===x||e.to===x);out.push({id:x,kind:n.kind,links});for(const e of links)walk(e.from===x?e.to:e.from,d-1)};walk(id,depth);return out}
 stats(){const kinds:Record<string,number>={};for(const n of this.nodes.values())kinds[n.kind]=(kinds[n.kind]??0)+1;return {nodes:this.nodes.size,edges:this.edges.length,kinds}}
}
