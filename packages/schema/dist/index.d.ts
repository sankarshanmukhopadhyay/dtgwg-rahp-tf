export type ReviewMode = 'rahp' | 'security' | 'combined';
export type EvidenceClass = 'ephemeral' | 'referenced' | 'durable' | 'exemplar';
export interface Evidence {
    id: string;
    class: EvidenceClass;
    description: string;
    uri?: string;
    sha256?: string;
    collected_at?: string;
    sensitivity?: string;
}
export interface RahpResult {
    version: 1;
    assessment: {
        id: string;
        key: string;
        triggers?: string[];
    };
    target: {
        repository: string;
        reviewed_revision: string;
        baseline_revision?: string | null;
        document?: string;
    };
    mode: ReviewMode;
    status: 'in-progress' | 'completed' | 'dispositioned';
    findings: Array<{
        id: string;
        title: string;
        status: string;
        [k: string]: unknown;
    }>;
    disposition: {
        outcome: 'pending' | 'no-material-assurance-impact' | 'findings-raised' | 'remediation-requested' | 'risk-accepted' | 'superseded';
        summary?: string;
        decided_at?: string | null;
    };
    evidence: Evidence[];
    retest_triggers?: string[];
}
export interface ValidationResult {
    valid: boolean;
    errors: string[];
}
export declare function validateResult(v: any): ValidationResult;
