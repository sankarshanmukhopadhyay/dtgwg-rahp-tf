import type { RahpResult, EvidenceClass, ValidationResult } from '@rahp/schema';
export interface RetentionAction {
    id: string;
    class: EvidenceClass;
    repository: 'allowed' | 'manifest-only' | 'forbidden';
    retention_days: number | null;
    action: 'commit' | 'manifest-only' | 'do-not-commit';
}
export declare function loadResult(file: string): RahpResult;
export declare function validateNormalizedResult(file: string): ValidationResult;
export declare function retentionPlan(r: RahpResult): {
    policy: string;
    assessment: string;
    actions: RetentionAction[];
};
export declare function sha256(file: string): any;
export interface Target {
    id: string;
    repository: string;
    branch?: string;
    commit?: string;
    reviews: string[];
}
export declare function parseProfile(text: string): {
    profile: {
        id: string;
    };
    assessment: any;
    repositories: Target[];
};
export declare function loadProfile(file: string): {
    profile: {
        id: string;
    };
    assessment: any;
    repositories: Target[];
};
export declare function validateProfile(file: string): ValidationResult;
export interface Observation {
    assessment_key: string;
    trigger_key: string;
    revision?: string;
}
export interface AssessmentRef {
    id: string;
    key: string;
    status: string;
}
export declare function correlateTrigger(observation: Observation, assessments: AssessmentRef[]): {
    action: string;
    assessment_key: string;
    assessment_id: string;
} | {
    action: string;
    assessment_key: string;
    assessment_id?: undefined;
};
