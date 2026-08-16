export interface Node {
    id: string;
    kind: string;
    data: any;
}
export interface Edge {
    from: string;
    to: string;
    relation: string;
}
export declare class RahpGraph {
    nodes: Map<string, Node>;
    edges: Edge[];
    static fromRahpJson(file: string): RahpGraph;
    trace(id: string, depth?: number): any[];
    stats(): {
        nodes: number;
        edges: number;
        kinds: Record<string, number>;
    };
}
