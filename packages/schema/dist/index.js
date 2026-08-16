export function validateResult(v) {
    const e = [];
    const req = (c, k, p = '') => { if (c?.[k] === undefined || c?.[k] === null || c?.[k] === '')
        e.push(`${p}${k}: required`); };
    if (!v || typeof v !== 'object')
        return { valid: false, errors: ['<root>: must be object'] };
    const allowedRoot = new Set(['version', 'assessment', 'target', 'mode', 'status', 'findings', 'disposition', 'evidence', 'retest_triggers']);
    for (const k of Object.keys(v))
        if (!allowedRoot.has(k))
            e.push(`${k}: additional property not allowed`);
    if (v.version !== 1)
        e.push('version: must equal 1');
    req(v, 'assessment');
    req(v, 'target');
    req(v, 'mode');
    req(v, 'status');
    req(v, 'findings');
    req(v, 'disposition');
    req(v, 'evidence');
    if (v.assessment) {
        req(v.assessment, 'id', 'assessment.');
        req(v.assessment, 'key', 'assessment.');
    }
    if (v.target) {
        req(v.target, 'repository', 'target.');
        req(v.target, 'reviewed_revision', 'target.');
    }
    if (!['rahp', 'security', 'combined'].includes(v.mode))
        e.push('mode: invalid');
    if (!['in-progress', 'completed', 'dispositioned'].includes(v.status))
        e.push('status: invalid');
    const outcomes = ['pending', 'no-material-assurance-impact', 'findings-raised', 'remediation-requested', 'risk-accepted', 'superseded'];
    if (v.disposition && !outcomes.includes(v.disposition.outcome))
        e.push('disposition.outcome: invalid');
    if (v.status === 'dispositioned' && v.disposition?.outcome === 'pending')
        e.push('dispositioned result cannot have pending outcome');
    if (!Array.isArray(v.findings))
        e.push('findings: must be array');
    else
        for (const [i, f] of v.findings.entries()) {
            req(f, 'id', `findings.${i}.`);
            req(f, 'title', `findings.${i}.`);
            req(f, 'status', `findings.${i}.`);
        }
    if (!Array.isArray(v.evidence))
        e.push('evidence: must be array');
    else
        for (const [i, x] of v.evidence.entries()) {
            req(x, 'id', `evidence.${i}.`);
            req(x, 'class', `evidence.${i}.`);
            req(x, 'description', `evidence.${i}.`);
            if (x.class === 'referenced') {
                for (const k of ['uri', 'sha256', 'collected_at', 'sensitivity'])
                    req(x, k, `evidence.${i}.`);
                if (x.sha256 && !/^[0-9a-f]{64}$/.test(x.sha256))
                    e.push(`evidence.${i}.sha256: invalid`);
            }
            if (x.class === 'ephemeral' && v.status === 'dispositioned')
                e.push(`dispositioned result must not depend on ephemeral evidence ${x.id ?? '?'}`);
        }
    return { valid: e.length === 0, errors: e };
}
