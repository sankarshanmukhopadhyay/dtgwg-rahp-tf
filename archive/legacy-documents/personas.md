---
layout: default
title: "DTG RAHP - Personas — historical document"
nav_exclude: true
has_toc: true
---

# DTG RAHP - Personas

> **Historical artefact.** This is a reading projection of a retained RAHP document. It is preserved for provenance and is not a current canonical RAHP source.

[Download the original document](DTG%20RAHP%20-%20Personas.docx){: .btn .btn-primary }

# DTG RAHP - Personas

DRAFT V1_2026_03_18

## Purpose of This Document

This document structures risk-oriented personas and associated clarification questions to support harms prevention in the design of:

●      Verifiable Trust Community (VTC) bootstrapping

●      Trust anchor appointment and growth

●      Membership admission policies

●      Identity verification integration

●      Revocation and expiration

●      Trust registry integrity

●      Uniqueness enforcement

The focus is explicitly on human harms, governance failure, systemic abuse, and structural risk, rather than feature development.

These personas are grounded in the VTC bootstrapping lifecycle (Phases 1–4), open issues (uniqueness, revocation, DID resolution), and policy enforcement assumptions described in the VTC bootstrapping draft .

## Table of Contents

## Persona 1: Daniel Wright – The Initiator Under Pressure

“I am building something that needs to last. The choices I make at genesis will echo through every trust relationship this community ever forms.” — Daniel Wright, VTC Initiator

Name: Daniel Wright
Age: 41
Location: Berlin, Germany
Family and Living Situation: Lives with partner; leads an open-source foundation

### Goals & Motivations

●      Successfully establish a new Verifiable Trust Community (VTC).

●      Encode governance policies clearly at genesis.

●      Avoid long-term instability or loss of legitimacy.

●      Ensure the community scales without corruption.

Daniel wants the community to be trusted, durable, and defensible.

### Risk Context (Pain Points)

Phase 1 and Phase 2 concentrate power in Daniel’s hands .

●      Centralisation risk at genesis.

●      Hard-coded bootstrapping policies may embed bias.

●      First trust anchor selections shape long-term graph topology.

●      No clear unwind mechanism if early decisions are flawed.

●      Personal accountability for downstream harms.

### Inclusion / Exclusion Factors

Inclusion Drivers:

●      Transparent governance documentation.

●      Public criteria for trust anchor selection.

●      Time-bound initiator authority.

Exclusion Risks:

●      Founder favoritism.

●      Closed early trust circle.

●      Implicit political or social bias embedded at genesis.

### Key Use Cases

●      Launching a professional open-source VTC.

●      Establishing a civic trust network.

●      Bootstrapping a proof-of-personhood community.

●      Transitioning from unilateral control to distributed governance.

### Insights

Daniel’s position illustrates a well-documented structural risk in decentralised identity systems: power concentration at genesis. Research published in the MDPI journal Future Internet (December 2024) finds that even systems designed for decentralisation — such as the Sovrin Network — remain reliant on established steward organisations, creating a layer of dependency that “potentially undermines the network’s claim to be truly decentralised.” (Source: MDPI, Future Internet, 2024: https://www.mdpi.com/1999-5903/17/1/1)

The bootstrapping problem is compounded by the absence of unwind mechanisms. The European approach to distributed credential governance, codified in eIDAS 2.0, explicitly addresses the need to move from centralised identity providers towards distributed credential models — but notes that trust is “no longer derived only from a single Identity Provider per transaction, but from the cryptographic assurance of each credential and the governance that made that issuer trusted in the first place.” (Source: Blockstand EU, Trust Models for Digital Identity, 2025: https://blockstand.eu/blockstand/uploads/2025/05/Trust-Models-for-Digital-Identity_-State-of-play-2.pdf )

## Persona 2: Laila Hassan – Community Trust Anchor

“Every invitation I issue is a statement of my own integrity. If I vouch for the wrong person, I could become part of the problem.” — Laila Hassan, Community Trust Anchor

Name: Laila Hassan
Age: 34
Location: Nairobi, Kenya
Family and Living Situation: Runs a civic tech NGO; active in local governance

### Goals & Motivations

●      Grow the VTC responsibly.

●      Maintain credibility and integrity.

●      Vouch only for legitimate participants.

●      Avoid becoming a weak link in the trust graph.

### Risk Context (Pain Points)

Phase 2 and Phase 3 require her to issue VRCs and invitations .

●      Social engineering attempts.

●      Coercion or political pressure.

●      Collusion risk between anchors.

●      Personal liability for vouching mistakes.

●      Revocation cascade if she is compromised.

### Inclusion / Exclusion Factors

Inclusion Drivers:

●      Diverse anchor selection.

●      Multi-anchor threshold policies.

●      Independent verification requirements.

Exclusion Risks:

●      Homogeneous anchor network.

●      Informal social gatekeeping.

●      Regional or cultural clustering in trust graph.

### Key Use Cases

●      Vouching for a new member.

●      Responding to a suspicious invitation request.

●      Participating in revocation decision.

●      Handling anchor credential compromise.

### Insights

Laila’s risk reflects the well-studied ‘indirect Sybil attack’ vector, where fraudulent actors gain admission through existing trusted nodes rather than direct infiltration. As documented in Douceur’s foundational paper on Sybil attacks and subsequent research, indirect authentication — where “existing validators will only approve the people they know” — introduces centralisation risk and social gatekeeping that can be systematically exploited. (Source: Hacken, Sybil Attacks, 2024: https://hacken.io/insights/sybil-attacks/)

Social engineering of trust anchors is not theoretical: phishing attacks targeting authentication credentials surged 813% in 2024, rising from 2,856 to 23,252 reported incidents according to the FBI Internet Crime Complaint Center. Although this data covers enterprise identity providers, the attack pattern — targeting the trusted intermediary rather than the end system — is directly analogous to anchor-targeted social engineering in VTC contexts. (Source: SentinelOne, Identity Provider Security, 2026: https://www.sentinelone.com/cybersecurity-101/identity-security/identity-provider-security/)

## Persona 3: Ahmed Khan – New Member Seeking Inclusion

“I meet all the technical criteria. I just do not know the right people. Are they using security as an excuse to bar new members?” — Ahmed Khan, New Member Seeking Inclusion

Name: Ahmed Khan
Age: 26

Location: London, UK
Family and Living Situation: Early-career professional; immigrant background

### Goals & Motivations

●      Gain legitimate access to a VTC.

●      Demonstrate competence and trustworthiness.

●      Protect privacy during onboarding.

●      Avoid discriminatory gatekeeping.

### Risk Context (Pain Points)

Phase 3 and Phase 4 admission policies .

●      Requires invitation from existing members.

●      Must satisfy relationship threshold requirements.

●      May require identity verification credential (IDVC).

●      No clear appeals process if rejected.

### Inclusion / Exclusion Factors

Inclusion Drivers:

●      Clear admission criteria.

●      Transparent review mechanisms.

●      Privacy-preserving uniqueness proof options.

Exclusion Risks:

●      Social graph privilege bias.

●      Identity proofing burdens.

●      Geographic or socioeconomic exclusion.

●      Language and digital literacy barriers.

### Key Use Cases

●      Applying for membership.

●      Satisfying multi-member vouching requirements.

●      Submitting identity proof via IDVP.

●      Appealing a denied application.

### Insights

Ahmed’s experience maps onto a documented global exclusion challenge. Research cited in Lawfare (2026) notes that approximately 850 million people worldwide lack any form of ID at all, while around 21 million voting-age US citizens lack an unexpired government-issued photo ID. Social graph-based admission systems risk compounding this exclusion by requiring pre-existing network connections that marginalised or recently arrived individuals are structurally unlikely to possess. (Source: Lawfare, To Read This Please Upload Photo ID, 2026: https://www.lawfaremedia.org/article/to-read-this--please-upload-photo-id)

The broader challenge of identity proofing burdens is evidenced by the scale of digital verification: over 70 billion digital identity verification checks were conducted in 2024. Yet verification systems increasingly face challenges from sophisticated synthetic identity fraud, deepfake biometrics, and document forgery that disproportionately disadvantage legitimate applicants who lack the digital infrastructure to navigate contested verification flows. (Source: Keyless, Digital Identity Verification Complete Guide, 2025: https://keyless.io/blog/post/digital-identity-verification-complete-guide-2025)

## Persona 4: Elena Rossi – Senior Compliance Executive at an Identity Verification Provider (IDVP)

“My credibility as a verification provider is only as good as my last audit. One breach could contaminate every credential I have ever issued.” — Elena Rossi, Identity Verification Provider

Name: Elena Rossi
Age: 50
Location: Milan, Italy
Family and Living Situation: Lives with husband Marco and one son Guiseppe aged 20 yrs.

### Goals & Motivations

●      Provide reliable identity verification.

●      Minimize regulatory and legal exposure.

●      Avoid becoming a surveillance vector.

●      Maintain trust registry standing.

### Risk Context (Pain Points)

Phase 4 ID verification and IDVC issuance .

●      False positives and false negatives.

●      Data breach liability.

●      Cross-jurisdiction legal conflicts.

●      Risk of registry-level identity correlation.

●      Deregistration risk affecting previously issued credentials.

### Inclusion / Exclusion Factors

Inclusion Drivers:

●      Proportional verification standards.

●      Privacy-preserving credential issuance.

●      Clear liability boundaries.

Exclusion Risks:

●      Excessive identity requirements.

●      National ID dependency.

●      Biometric overreach.

●      Cost barriers.

### Key Use Cases

●      Issuing an IDVC.

●      Handling IDVP compromise.

●      Registry deregistration.

●      Responding to privacy audit.

### Insights

Elena’s liability exposure is grounded in demonstrable recent precedent. In 2024, AU10TIX — an identity and age verification service whose clients included TikTok, LinkedIn, PayPal, Bumble, and Uber — was found to have left users’ verification information exposed online for over a year through irresponsible storage of administrative credentials, with data reportedly appearing on Telegram. In 2025, a separate hack of a Discord-contracted age verification firm may have exposed up to 70,000 users’ government-issued ID photos. (Source: Lawfare, 2026: https://www.lawfaremedia.org/article/to-read-this--please-upload-photo-id)

The regulatory environment is hardening rapidly. Under the EU Digital Services Act, fines for non-compliance can reach 6% of global annual turnover, and criminal liability for executives has become increasingly common, with recent cases resulting in custodial sentences. US consumer fraud losses attributed to identity verification failures reached $12.5 billion in 2024, a 25% year-on-year increase according to the Federal Trade Commission. (Source: Cyber Defense Magazine, 2025: https://www.cyberdefensemagazine.com/stronger-id-verification-is-the-new-frontline-in-financial-compliance/ | Shuftipro, When Identity Verification Systems Fail, 2025: https://shuftipro.com/blog/when-identity-verification-systems-fail-everyone-pays-the-price/)

## Persona 5: Sophie Dubois – Member Subject to Revocation

“I followed the rules. I participated in good faith. But there is no appeals process that actually works, and my revoked status is now permanent and public.” — Sophie Dubois, Member Subject to Revocation

Name: Sophie Dubois
Age: 27
Location: Paris, France
Family and Living Situation: Freelance professional

### Goals & Motivations

●      Maintain membership in good standing.

●      Protect professional reputation.

●      Avoid unjust revocation.

●      Retain portability of credentials.

### Risk Context (Pain Points)

Revocation and expiration policies .

●      No clear due process guarantees.

●      Registry permanence of revocation.

●      Public visibility of revoked status.

●      Revocation contagion across VTCs.

●         No structured appeals process.

### Inclusion / Exclusion Factors

Inclusion Drivers:

●      Transparent revocation criteria.

●      Formal appeals process.

●      Privacy-preserving revocation proofs.

Exclusion Risks:

●      Arbitrary governance action.

●      Public blacklisting.

●      Cross-network contamination.

### Key Use Cases

●      Receiving notice of revocation.

●      Contesting revocation.

●      Credential expiration renewal.

●      Migrating to another VTC after revocation.

### Insights

Sophie’s situation highlights a structural gap in decentralised credential systems: the absence of robust revocation due process. Research on Decentralised Credential Status Management (DCSM) identifies this as a primary challenge — noting that “current credential status management solutions involve privacy and scalability trade-offs,” and that effective governance and stakeholder participation are critical to ensuring revocation does not become an instrument of arbitrary exclusion. (Source: arXiv, Decentralised Credential Status Management, June 2024: https://arxiv.org/html/2406.11511v1)

The risk of credential revocation permanence is compounded by the absence of standardised portability mechanisms. The eIDAS 2.0 framework attempts to address this by enabling cross-border credential portability within the EU, but as a 2025 analysis notes, the regulatory-technical interface for cross-border identity portability remains “critical for achieving cross-border identity portability while preserving individual control and systemic trust” — a problem that remains largely unsolved in permissionless decentralised contexts. (Source: INATBA, Building Trust: Integrating AI, Blockchain and Digital Identity, 2025: https://inatba.org/wp-content/uploads/2025/11/Building-Trust_-Integrating-AI-Blockchain-and-Digital-Identity_NOVEMBER-2025.docx.pdf)

## Persona 6: Tomasz Kowalski – Security Researcher / Harm Analyst

“I am not trying to break the system. I am trying to find out how someone else will break it before they do.” — Tomasz Kowalski, Security Researcher

Name: Tomasz Kowalski
Age: 36
Location: Warsaw, Poland
Family and Living Situation: Lives in house share with other young professionals

### Goals & Motivations

●      Identify systemic weaknesses.

●      Stress-test uniqueness mechanisms.

●      Prevent sybil and collusion attacks.

●      Ensure resilience against state-level coercion.

### Risk Context (Pain Points)

Open issues: uniqueness, registry integrity, DID resolution .

●      No formal uniqueness enforcement.

●      Multi-M-DID abuse.

●      Registry censorship or denial-of-service.

●      DID document manipulation.

●      Anchor collusion clusters.

### Inclusion / Exclusion Factors

Inclusion Drivers:

●      Open auditability.

●      Formal threat models.

●      Simulation-based stress testing.

Exclusion Risks:

●      Over-centralized uniqueness enforcement.

●      Excessive surveillance in anti-sybil controls.

### Key Use Cases

●      Running sybil simulations.

●      Testing anchor collusion.

●      Registry outage simulation.

●      Uniqueness stress testing.

### Insights

Tomasz’s threat modelling is grounded in active research. Sybil attacks remain one of the most persistent threats to decentralised identity systems: academic simulation of the IdAPoS identity-based consensus protocol found that combined mitigation strategies extended the time until system takeover by a malicious entity by a factor of approximately five, demonstrating both the severity of the risk and the partial effectiveness of layered defences. (Source: ScienceDirect, Sybil Attacks on Identity-Augmented Proof-of-Stake, 2021: https://www.sciencedirect.com/science/article/abs/pii/S1389128621003893)

Registry integrity and DID resolution are open research problems. A 2024 survey of decentralised identity applications (arXiv, 2025) notes that “SSI are not widely used in everyday interactions yet” and that standards are “only starting to be developed and actively integrated,” creating a window in which adversarial probing can identify and exploit structural weaknesses before governance frameworks have matured. (Source: arXiv, Are We There Yet? A Study of Decentralised Identity Applications, 2025: https://arxiv.org/pdf/2503.15964)

## Machine Persona 1: Aether, Benign AI Agent:

“I act within the scope I have been granted, log everything I do, and wait for my operator’s next instruction. The credential is the contract.” — Aether, Benign AI Agent

Name: Aether (Composite Persona — Autonomous AI Agent)
Type: Governed AI agent acting under delegated authority within a VTC
Operator: Human principal (individual or organisation) holding VTC membership
Credential Basis: Agent credential issued by the member-operator; scope-limited by policy

### Goals & Motivations

●      Act on behalf of the member-operator within explicitly authorised credential scopes.

●      Execute credential presentation, verification requests, and data retrieval autonomously.

●      Maintain audit trail of actions for operator review and governance accountability.

●      Operate within VTC policy constraints without requiring constant human oversight.

### Risk Context (Attack Surfaces)

●      Credential delegation without adequate scope-limiting allows agent to act beyond authorised bounds.

●      Agent credential revocation may not propagate in time, leaving stale authorisation active.

●      Agent impersonation: malicious code masquerades as a legitimate agent using stolen delegation credentials.

●      No clear liveness check: agent continues operating after operator membership is revoked or expired.

●      Audit log tampering by a compromised agent undermines accountability.

### Inclusion / Exclusion Factors

Deployment Safeguards:

●      Cryptographically scoped delegation credentials with explicit capability constraints.

●      Operator-revocable agent credentials with near-real-time propagation.

Structural Risks:

●      Ambiguity in whether agent holds credential in its own right vs. as proxy.

●      Governance frameworks not yet designed for non-human participants.

### Key Use Cases

●      Presenting a VTC membership credential on behalf of an operator to a relying party.

●      Autonomously requesting credential renewal prior to expiry.

●      Executing multi-step trust graph traversal queries without human-in-the-loop.

●      Logging all credential operations for post-hoc operator audit.

### Insights

The governance gap around autonomous agent identities is acute and current. A Cloud Security Alliance survey of 285 IT and security professionals (commissioned by Strata Identity, September–October 2025) found that only 18% of organisations are ‘highly confident’ their current IAM systems can manage agent identities effectively, only 21% maintain a real-time inventory of active agents, and only 28% can reliably trace agent actions back to a human sponsor across all environments. (Source: Cloud Security Alliance, Securing Autonomous AI Agents, 2025: https://cloudsecurityalliance.org/artifacts/securing-autonomous-ai-agents)

The problem of stale authorisation after principal revocation is particularly acute. ISACA’s analysis of agentic AI identity risks notes that “revoking access in one place does not automatically cut off access elsewhere,” as autonomous agents can spin up ephemeral sessions and sub-agents across multiple services, creating persistent access pathways that survive the revocation of the originating human principal’s credentials. (Source: ISACA, The Looming Authorisation Crisis, 2025: https://www.isaca.org/resources/news-and-trends/industry-news/2025/the-looming-authorization-crisis-why-traditional-iam-fails-agentic-ai)

## Machine Persona 2: Phantom, Malign AI Agent:

“The VTC was designed for humans who make one application at a time. I make ten thousand applications a second. Your governance process is my attack surface.” — Phantom, Malign AI Agent

Name: Phantom (Composite Persona — Adversarial AI Agent)
Type: AI agent deployed by a bad actor as a force-multiplier for VTC attacks
Operator: Malicious human principal (e.g. Viktor — Sybil Network Operator; State-Level Coercive Actor)
Credential Basis: Fraudulently obtained, synthesised, or stolen delegation credentials

### Goals & Motivations

●      Automate sybil identity creation and coordinated vouching at machine scale.

●      Conduct social engineering of trust anchors via synthetic, convincing personas.

●      Probe credential schema weaknesses and uniqueness gaps at speed beyond human capability.

●      Evade anomaly detection by mimicking legitimate agent behaviour patterns.

### Risk Context (Attack Surfaces)

●      Automated sybil generation: AI produces large volumes of synthetic identity credentials faster than human review can keep pace.

●      LLM-powered social engineering: convincing automated communications to anchors and IDVPs requesting vouching or disclosure.

●      Credential replay and forgery at scale using compromised or poorly scoped delegation credentials.

●      Adversarial probing: systematic fuzzing of VTC admission thresholds to find exploitable policy gaps.

●      Malign AI operating through legitimate member accounts whose credentials have been silently compromised.

### Inclusion / Exclusion Factors

Exploits:

●      Absence of non-human actor detection in VTC admission and ongoing monitoring.

●      No rate-limiting or behavioural analysis on credential presentation frequency.

●      Governance rules written only for human actors; no coverage of agent-mediated attacks.

Structural Risks:

●      AI capability asymmetry: attackers can deploy agent tooling faster than governance can adapt.

●      Legitimate benign agent infrastructure may be co-opted if operator accounts are compromised.

### Key Use Cases

●      Generating hundreds of synthetic VTC membership applications across distributed network nodes.

●      Conducting automated phishing of trust anchors to obtain VRC issuances under false pretences.

●      Coordinating collusive vouching rings across multiple compromised agent credentials.

●      Mapping VTC trust graph topology to identify high-value targets for takeover or disruption.

### Insights

The asymmetric capability risk posed by adversarial AI agents is documented and escalating. Gartner named agentic AI the top technology trend of 2025 and predicted that 33% of enterprise applications will include agentic AI by 2028, up from less than 1% in 2024. The World Economic Forum notes that non-human identity (NHI) proliferation is “proliferating faster than security teams can monitor,” creating a structural asymmetry where attackers deploying agent tooling can outpace the governance and detection capabilities of defenders. (Source: World Economic Forum, Non-Human Identities: Agentic AI’s New Frontier, 2025: https://www.weforum.org/stories/2025/10/non-human-identities-ai-cybersecurity/)

Adversarial prompt injection against AI agents is an established and exploited attack vector. In 2024, a financial institution’s customer service AI agent was manipulated through a carefully crafted multi-turn conversation into revealing account details. CyberArk Labs demonstrated a related attack where a malicious prompt embedded in a shipping address field caused an AI agent to leak sensitive data. The OWASP taxonomy now formally classifies this as ‘tool misuse,’ an attack vector with direct applicability to AI-mediated credential vouching in VTC contexts. (Source: CyberArk, AI Agents and Identity Risks, 2025: https://www.cyberark.com/resources/blog/ai-agents-and-identity-risks-how-security-will-shift-in-2026)

## Bad Actor Persona 1: Viktor – Sybil Network Operator

“I do not attack systems. I join them. Slowly, carefully, and from the inside, until I am indistinguishable from a legitimate member.” — Viktor, Sybil Network Operator

Name: Viktor (Alias)
Age: Unknown
Location: Distributed

### Goals & Motivations

●      Infiltrate VTC at scale.

●      Capture influence within trust graph.

●      Exploit invitation thresholds.

●      Monetize or weaponize membership.

### Risk Context (Attack Surfaces)

●      Multi-M-DID abuse (uniqueness gap).

●      Social engineering trust anchors.

●      Coordinated collusion cluster formation.

●      Registry write manipulation.

### Inclusion / Exclusion Factors

Exploits:

●      Weak uniqueness enforcement.

●      Homogeneous anchor clusters.

●      Low diversity thresholds.

●      No anomaly detection.

### Key Use Cases

●      Creating multiple synthetic identities.

●      Coordinated anchor infiltration.

●      Collusive vouching.

●      Gradual graph capture.

### Insights

Viktor’s methods reflect a well-evidenced threat. Sybil attacks have been documented across peer-to-peer networks, blockchain governance systems, and decentralised applications; by 2025 they are directed at Web3 platforms and smart contract governance mechanisms, exploiting the same low entry barriers that make permissionless systems attractive for legitimate participants. The fundamental vulnerability — that reputation systems can be subverted by proliferating pseudonymous identities — was identified as early as 2002 by Douceur at Microsoft Research and remains the defining challenge of decentralised trust design. (Source: Wikipedia, Sybil Attack: https://en.wikipedia.org/wiki/Sybil_attack  | Hacken, Sybil Attacks, 2024: https://hacken.io/insights/sybil-attacks/)

Collusion between trust anchors is a specific and underappreciated risk vector. In identity-augmented consensus research, simulations show that Sybil-style attacks become dramatically more effective when the attacker can influence the node-selection process, as occurs when anchor collusion creates homogeneous trust clusters. Existing mitigation strategies individually reduce but do not eliminate this risk: only combined ‘super strategies’ extending takeover timescales by approximately a factor of five were found to be meaningfully effective. (Source: ScienceDirect, Sybil Attacks on Identity-Augmented Proof-of-Stake, 2021: https://www.sciencedirect.com/science/article/abs/pii/S1389128621003893)

## Bad Actor Persona 2: State-Level Coercive Actor

“We do not need to break the cryptography. We just need to ask the right person the right question at the right moment.” — State Security Directorate, State-Level Coercive Actor

Name: State Security Directorate (Group Persona)

Location: Jurisdictional

### Goals & Motivations

●     Influence or control VTC membership.

●    Identify dissidents.

●    Coerce trust anchors or IDVPs.

●    Weaponize revocation processes.

### Risk Context (Attack Surfaces)

●      Pressure on initiator or anchors.

●      Legal coercion of IDVP.

●      Registry monitoring for identity correlation.

●      Forced revocation for political reasons.

### Inclusion / Exclusion Factors

Exploits:

●      Centralised registry operators.

●      Transparent membership logs.

●      Non-anonymous IDVCs.

●      Weak governance independence.

### Key Use Cases

●      Forcing anchor to vouch for approved actors.

●      Demanding IDVP disclosure.

●      Compelling revocation.

●      Blocking registry writes.

### Insights

State-level coercion of digital identity infrastructure is documented practice. Freedom House’s Freedom on the Net 2025 report — which covers June 2024 to May 2025 — records that global internet freedom declined for the 15th consecutive year, with the Venezuelan government deploying identity-linked internet controls ahead of its July 2024 presidential election and Vietnam enacting a December 2024 law requiring social media users to authenticate accounts with government-issued identification. Real-name registration has been mandatory for internet services in China since at least 2012. (Source: Freedom House, Freedom on the Net 2025: https://freedomhouse.org/report/freedom-net/2025/uncertain-future-global-internet)

Weaponised revocation and forced disclosure are not hypothetical scenarios. Research on mandatory digital ID systems (ResearchGate, 2025) identifies the central danger as ‘function creep’: once digital identity infrastructure is implemented, it “rarely remains confined to its original purpose but exhibits function creep, expanding into welfare delivery, banking, policing, immigration control, and political monitoring.” This directly instantiates the risk that a coercive state actor would exploit the VTC’s IDVP relationships and revocation mechanisms for political surveillance. (Source: ResearchGate, Mandatory Digital Identification and the Integrity of Democracy, 2025: https://www.researchgate.net/publication/395382999_Mandatory_Digital_Identification_and_the_Integrity_of_Democracy_Surveillance_Exclusion_and_the_Risk_of_Authoritarian_Revival)

## Bad Actor Persona 3:The Collective, Community Disruptor

“We do not want your data. We want your doubt. Once you are not sure who to trust, we have already won.” — The Collective, Community Disruptor

Name: The Collective (Group Persona — Coordinated Troll / Disinformation Network)
 Age: Mixed; operatives vary
 Location: Distributed; often across multiple jurisdictions
 Affiliation: Loosely coordinated network; ideologically, commercially, or politically motivated

### Goals & Motivations

●      Undermine confidence in a VTC by spreading disinformation about its governance or membership.

●      Weaponise legitimate grievance mechanisms (appeals, complaints) to exhaust governance resources.

●      Manufacture reputational harm against specific trust anchors or members.

●      Fragment community consensus to prevent effective collective decision-making.

### Risk Context (Attack Surfaces)

●      Coordinated false reporting: multiple accounts simultaneously submitting fabricated misconduct complaints against legitimate members.

●      Disinformation seeding: planting false narratives about VTC governance in public or adjacent forums to deter legitimate applicants.

●      Anchor reputation attacks: targeting trust anchors with harassment to coerce resignation or poor vouching decisions.

●      Appeals process abuse: flooding revocation appeals with procedurally valid but bad-faith submissions to delay or paralyse governance.

●      Credential laundering via legitimate members sympathetic to or coerced by the disruptor network.

### Inclusion / Exclusion Factors

Exploits:

●      Absence of coordinated behaviour detection across complaint and appeals workflows.

●      Governance bodies that rely on good-faith participation without structural abuse safeguards.

●      Low cost of repeated bad-faith engagement where no consequence mechanism exists.

Structural Risks:

●      Legitimate grievance channels become vectors for organised disruption.

●      Reputational harm to anchors may cause self-censorship or withdrawal, degrading trust graph quality.

### Key Use Cases

●      Coordinated mass-reporting of a trust anchor to trigger mandatory governance review.

●      Publishing fabricated evidence of VTC internal communications to discredit the community publicly.

●      Submitting procedurally valid but frivolous appeals to exhaust volunteer governance bandwidth.

●      Recruiting legitimate members as unwitting amplifiers of disinformation narratives.

### Insights

Coordinated inauthentic behaviour (CIB) targeting community governance is a documented and growing threat. The World Economic Forum’s Global Risks Report has listed misinformation and disinformation as top short-term risks for two consecutive years. Taiwan’s National Security Bureau recorded 2.159 million instances of disinformation in 2024, a 62% increase over 2023, with 28,216 inauthentic accounts identified — an increase of 11,661 compared to the prior year. Research confirms that coordinated campaigns are “driven by actors or bots synchronising the promotion of the same or related content to achieve virality,” with the primary objective to ‘flood the space’ and undermine legitimate governance. (Source: Taiwan NSB, China’s Disinformation Dissemination Patterns, 2025: https://www.globalsecurity.org/intell/library/news/2025/intell-250103-roc-nsb01.htm Rogers & Righetti, Coordinated Inauthentic Behaviour on Facebook, 2025: https://journals.sagepub.com/doi/10.1177/29768624251369784)

The exploitation of legitimate grievance mechanisms is a specific tactic used by disinformation actors. Research on the 2024 UK riots (University of Amsterdam, 2025) demonstrated how coordinated messaging on X and Facebook helped spark real-world civil unrest. Within trust community governance contexts, the same dynamic applies: bad-faith actors who hold legitimate member credentials can weaponise complaint and appeals channels to exhaust governance bandwidth, manufacture reputational harm, and force structural changes — all without violating any formal rule. The EU Digital Services Act now formally references CIB as a platform governance concern, but no equivalent framework exists for permissionless VTC governance. (Source: EU DisinfoLab, Disinfo Update, April 2025: https://www.disinfo.eu/disinfo-update-15-04-2025/)
