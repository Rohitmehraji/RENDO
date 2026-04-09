# RENDO — Global Phenomenon Architecture + GDD v2.0

## 1) Product North Star

**Promise:** “Not a game, a second life — and every session creates a story worth sharing.”

RENDO combines battle royale intensity, cinematic storytelling, social identity, and a persistent AI-driven world that remembers player actions.

### Success Metrics (Global-Phenomenon Tier)
- D30 retention > 38% (core), > 25% (casual)
- Share rate (clips published/session) > 0.45
- Viral coefficient (invited joins per active sharer) > 0.30
- Crash-free sessions > 99.7%
- Toxic encounter rate < 1.2 per 100 sessions

---

## 2) Full System Architecture

## 2.1 Runtime Layers

1. **Client Runtime Layer**
   - UE5 photoreal profile + mobile-lite profile
   - Real-time cinematic camera graph on client
   - Micro-expression and stress shader pipeline (sweat, breath, fatigue)

2. **World Simulation Layer**
   - Regional shards + global event broadcast fabric
   - Unpredictable gameplay rule mutator engine
   - Persistent city, faction, and war-state simulation

3. **Gameplay Services Layer**
   - Matchmaking, session, quest, inventory
   - Personal Hero Director (player-specific story arcs)
   - Status & Aura reputation engine

4. **AI Experience Layer**
   - Hollywood Moment Engine
   - AI Memory World Engine
   - Emotional Companion Engine
   - Voice-to-World Command Orchestrator

5. **Data, Streaming & Security Layer**
   - Kafka/Pulsar event mesh + stream processing
   - Graph memory DB (Neo4j-type) + low-latency cache
   - Device fingerprint and behavior anti-cheat models
   - Encryption, key rotation, signed asset lineage

## 2.2 Microservice Topology (Expanded)

Core platform:
- `gateway-api`
- `identity-service`
- `player-profile-service`
- `matchmaking-service`
- `session-orchestrator`
- `world-sim-service`
- `telemetry-ingest-service`

New phenomenon services:
- `cinematic-engine-service`
- `memory-graph-service`
- `emotion-ai-service`
- `companion-director-service`
- `voice-command-service`
- `content-creator-service`
- `global-event-director-service`
- `rule-mutator-service`

## 2.3 Real-time Streaming Architecture

Event backbone:
- Ingest: gameplay, voice intent, camera state, emotion signals
- Stream processing: Flink/Spark Structured Streaming jobs
- Fan-out: clips, global events, adaptive missions, anti-cheat decisions

Topics (sample):
- `cinematic.moment.detected`
- `cinematic.highlight.rendered`
- `memory.world.edge_written`
- `voice.command.received`
- `world.global_event.triggered`
- `emotion.state.updated`
- `security.behavior.anomaly`

---

## 3) Game-Changer Systems

## 3.1 Hollywood Moment Engine (Virality Core)

Detects dramatic events in real time:
- Clutch elimination
- Betrayal by teammate/faction
- Last-survivor pressure arc

Pipeline:
1. Event detector scores dramatic intensity
2. Camera selector chooses cinematic path (orbit, shoulder, drone)
3. Audio engine layers adaptive dramatic score
4. Slow-motion and post-processing applied per platform budget
5. Auto-generated vertical reel (9:16) + subtitles + safe metadata

Output artifacts:
- In-game replay clip
- Share-ready short-form reel (YouTube/Instagram/TikTok compatible)
- SEO hashtags + auto-caption suggestions

## 3.2 AI Memory World (History Engine)

- NPCs store episodic memory edges: saved, betrayed, traded, abandoned
- Cities track player-driven civic trust and faction control
- Macro-state machine can escalate to strikes, uprisings, and wars
- Memory decay is non-linear: emotionally intense events decay slower

Graph model (Neo4j style):
- Nodes: `Player`, `NPC`, `Faction`, `District`, `Event`
- Edges: `HELPED`, `BETRAYED`, `TRADED_WITH`, `OWNS`, `TRUSTS`, `HATES`
- Properties: `timestamp`, `intensity`, `witness_count`, `decay_curve`

## 3.3 Real Human Presence System

- Facial micro-expression blendshapes from emotion state
- Breath/fatigue loops tied to stamina and stress load
- Injury layers: bruise, blood, limp, voice crack under pressure
- Context-sensitive haptics and camera shake by physical state

## 3.4 Emotional AI Companions

- Companion archetypes: protector, strategist, wildcard
- Relationship meter with attachment, trust, and irritation vectors
- Companion memory references prior missions and promises
- Dialogue style adapts to player tilt/frustration and confidence

## 3.5 Live World Events (Viral Spikes)

- Scheduled and surprise global events (invasion, outbreak, political war)
- Region-aware concurrency orchestration
- Community contribution tracker with global progression bars
- Event endings unlock story cinematics and unique social badges

## 3.6 Player = Movie Hero

- Personal Hero Graph tracks motivations and unresolved conflicts
- AI-generated cutscenes use player avatar and squad roster
- Major achievements trigger title cards, narration, and arc progression

## 3.7 Unpredictable Gameplay Engine

- Rule cards injected mid-session with safety constraints
- Dynamic loot mutators and gravity/weather anomalies
- Fairness guardrail prevents impossible win conditions

## 3.8 Voice-to-World AI System

- Players issue intent commands (“scan area”, “call backup”, “hold fire”)
- Intent parser converts speech to domain actions
- Command authorization validates role, cooldown, and world context

## 3.9 Dream Mode

- Surreal physics profiles and impossible geometry
- AI art direction changes skybox, gravity, and soundscape in-session
- Creator-first sandbox for clip-worthy experimental content

## 3.10 Instant Content Creator Mode

- Auto-edit timeline, subtitles, transitions, and color grade
- One-tap export to platform presets
- Rights-safe music library + AI generated alternates

## 3.11 Psychology Engine 2.0

- Real-time frustration, boredom, and excitement estimators
- Dynamic difficulty and event pacing adjustments
- Wellbeing constraints: cooldown prompts and stop-loss nudges

## 3.12 Self-Evolving Game Layer

- AI proposes balance patches to weapons/maps/missions
- Simulation sandbox validates proposals before production rollout
- Human policy gate for compliance, fairness, and exploit prevention

## 3.13 Next-Gen Security

- Device + behavior fingerprinting and impossible-pattern detectors
- Session-level trust score gates matchmaking and rewards
- Continuous model retraining from confirmed exploit traces

## 3.14 Ultra Performance System

- Device-aware rendering quality tiers with neural upscaling
- Low-end phones get lite shaders + server-assisted effects
- High-end devices unlock full cinematic stack + ray-traced path

## 3.15 Status & Aura System

- Reputation badges and aura effects (feared/respected/legendary)
- Aura visible in social hubs and introductions
- Anti-toxicity weighting: aura decays for abusive behavior

---

## 4) UI/UX Flows

### 4.1 “Hollywood Moment” Flow
1. High-intensity event occurs
2. Cinematic trigger card appears (“Moment Captured”)
3. Auto-preview in post-match timeline
4. User edits caption/music (optional)
5. One-tap publish or save draft

### 4.2 Voice Command Flow
1. Push-to-command / wake phrase
2. Intent transcription with confidence score
3. Confirmation overlay for critical commands
4. Execute + squad notification + cooldown timer

### 4.3 Companion Bond Flow
1. Companion message appears pre-mission
2. Shared mission decisions affect trust
3. Post-mission emotional recap scene
4. Relationship milestone unlocks perks/cutscenes

---

## 5) Backend API Design

Primary contract in `services/api/openapi.yaml` now includes:
- Highlight generation jobs
- Voice command execution
- Legacy avatar/matchmaking/NPC endpoints

---

## 6) AI Models Design (Expanded)

### 6.1 Emotion Detection Models
- Multimodal model: voice prosody + gameplay biometrics + behavior tempo
- Output: valence, arousal, stress, frustration, excitement probabilities

### 6.2 Behavior Prediction Models
- Sequence model predicts tilt, churn risk, and playstyle transitions
- Used by matchmaking, companion director, and psychology engine

### 6.3 Memory Graph Retrieval
- Hybrid graph query + vector recall
- Time-aware ranking with intensity and witness weighting

---

## 7) Data Architecture (Neo4j-type + Streaming)

- Graph DB cluster for memory relations and world causality
- OLTP store for transactional economy/profile data
- Feature store for real-time ML serving
- Object storage for highlight reels and cinematic assets

---

## 8) Deployment Pipeline

1. CI: lint, unit, contract tests, replay determinism tests
2. Model CI: bias/fairness checks + drift baseline generation
3. CD: canary by region/device class + kill switch per feature flag
4. LiveOps: event scheduler with emergency rollback workflows

---

## 9) Monetization Strategy (Viral + Sustainable)

- Creator revenue split for viral reel performance
- Cinematic pass for premium scene packs (cosmetic only)
- Companion customization store (non-pay-to-win)
- Event sponsorship slots with strict player experience protections

---

## 10) Step-by-Step Build Plan (Upgrade)

### Milestone A (0–4 months)
- Cinematic engine MVP + highlight API
- Voice command API + command security policy
- Graph memory service skeleton

### Milestone B (4–8 months)
- Emotional companion v1
- Global event director and live event dashboards
- Creator mode export pipeline

### Milestone C (8–14 months)
- Self-evolving rule mutator with safety sandbox
- Psychology engine 2.0 live experimentation
- Reputation and aura social systems

### Milestone D (14–24 months)
- Full persistent geopolitical simulation
- Dream Mode and advanced cinematic personalization
- Multi-region scaling to global phenomenon operations
