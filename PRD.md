# Product Requirements Document (PRD)

# SovereignPulse — Mission-Critical Voice Incident Intelligence

**Hackathon:** SLNG — Problem Statement 2: Best Use of the SLNG Platform  
**Version:** 4.1.0 — Validated Architecture with Runtime Selection & Benchmark Mode  
**Product Type:** AI-Powered Voice Operations Assistant  
**Primary Technologies:** SLNG, Unmute, Python, LLM, React  
**Deployment Strategy:** Local browser-based development first; hosted SLNG deployment as a stretch goal

---

## 1. Executive Summary

### 1.1 Product Overview

SovereignPulse is a voice-powered incident intelligence assistant that converts spoken incident reports into structured, reviewable operational records.

Field operators, security teams, and operations personnel often work in environments where typing detailed incident reports is inconvenient. Manual reporting can lead to missing information, inconsistent descriptions, and delays in creating useful records.

SovereignPulse allows an operator to describe an incident through a natural voice conversation. The agent transcribes the report, identifies important information, asks clarifying questions, and prepares a structured incident record for human review.

The system uses **SLNG as its voice execution layer** and **Unmute to define and compile the voice agent**. A mission-control dashboard presents the conversation, incident details, and measured system performance.

The hackathon demonstration will use simulated operational incidents. The initial product will not independently contact emergency services or dispatch real-world response teams.

### 1.2 Problem Statement

Voice AI applications can face several engineering challenges:

- Delays caused by sequential speech recognition, LLM reasoning, and speech synthesis.
- Background noise and inaccurate speech recognition.
- Unnecessary model processing and token consumption.
- Difficulty changing voice providers or agent runtimes.
- Limited visibility into latency, model usage, and execution configuration.
- Regional data-processing requirements.

### 1.3 Proposed Solution

SovereignPulse combines:

1. Natural voice interaction.
2. Structured incident extraction.
3. Context-aware follow-up questions.
4. SLNG-powered speech processing and voice output.
5. Unmute-based declarative agent configuration.
6. A dashboard for transcripts, incident reports, and performance metrics.
7. Human review before consequential actions.

### 1.4 Core Differentiator

**SovereignPulse does not stop at conversation. It turns speech into structured operational intelligence and makes the performance of its voice infrastructure observable.**

---

## 2. Product Goals

### 2.1 Primary Goals

- Deliver a working voice agent powered by SLNG.
- Use the Unmute framework in the actual implementation.
- Convert spoken reports into structured incident records.
- Support clarifying questions and corrections.
- Display live transcripts and incident summaries.
- Measure end-of-utterance-to-first-audio latency.
- Record model usage where provider instrumentation permits.
- Demonstrate the configured execution region accurately.
- Present a reliable, repeatable three-minute demonstration.

### 2.2 Non-Goals

The first version will not:

- Perform real emergency dispatch.
- Make autonomous life-or-death decisions.
- Guarantee transcription accuracy in every noisy environment.
- Claim that all data stays within a region without verification.
- Claim specific latency or cost improvements without measurement.
- Implement multiple orchestration frameworks simultaneously.
- Build a complete enterprise incident-management platform.

---

## 3. Target Users

**Field Operators:** People who need to report incidents without manually completing lengthy forms.

**Security and Operations Teams:** Teams that need consistent incident records and clear summaries.

**Operations Managers:** People who need visibility into reported incidents and the performance of voice-enabled workflows.

**Hackathon Demonstration User:** An operator reporting a simulated road accident, industrial hazard, or security incident.

---

## 4. Core User Journey

1. The operator opens SovereignPulse and starts a voice session.
2. The browser requests microphone access.
3. The operator describes an incident naturally.
4. The configured SLNG voice pipeline processes the speech.
5. The LLM identifies relevant details and missing information.
6. The agent asks a follow-up question when necessary.
7. The operator provides additional information or corrects an earlier detail.
8. The agent generates a structured incident report.
9. The agent reads back a concise summary through SLNG.
10. The dashboard displays the transcript, report, session status, and available performance metrics.
11. The operator reviews the report before saving or exporting it.

---

## 5. Functional Requirements

### 5.1 Voice Interaction

**FR-01: Microphone Access**

The application must request permission before accessing the microphone and display a useful error if permission is denied.

**FR-02: Speech Recognition**

The configured SLNG-supported speech recognition path must convert the operator's spoken report into text.

**FR-03: Voice Response**

The agent must respond audibly using the configured SLNG-supported voice generation path.

**FR-04: Conversation Context**

The agent must retain relevant incident details throughout the active conversation.

**FR-05: Session Status**

The interface must distinguish connecting, listening, processing, responding, completed, and error states wherever the runtime exposes the necessary events.

**FR-06: Interruption Handling**

If the selected runtime supports barge-in, the agent should stop its current response when the operator interrupts. This feature is a stretch goal until the core voice loop is verified.

### 5.2 Incident Intelligence

**FR-07: Incident Classification**

The agent must identify the reported incident category from a predefined set:

- Road accident
- Medical incident
- Fire or smoke
- Industrial hazard
- Security incident
- Other operational incident

**FR-08: Structured Extraction**

The system must extract these fields when available:

- Incident description
- Incident category
- Reported location
- Priority or severity
- Known hazards
- Number of people affected, if reported
- Additional assistance requested
- Missing information
- Information requiring verification

**FR-09: Follow-Up Questions**

The agent must ask concise, relevant questions when critical details are missing or ambiguous.

**FR-10: Correction Handling**

The operator must be able to correct extracted details. The final incident record must reflect the correction.

**FR-11: Evidence and Uncertainty**

The agent must distinguish reported facts from assumptions and unknown values. It must not invent a location, casualty count, or hazard status.

**FR-12: Human Review**

The completed incident report must be available for human review before an external consequential action is taken.

### 5.3 Mission-Control Dashboard

**FR-13: Live Transcript**

Display recognized user speech and agent responses.

**FR-14: Incident Summary**

Display extracted incident fields in a structured summary card.

**FR-15: Audio Visualization**

Display an audio-reactive waveform or sound-level visualization when audio data is available.

**FR-16: Performance Metrics**

Display actual latency measurements and available processing statistics.

**FR-17: Benchmark Comparison (Benchmark Mode)**

Display baseline and optimized results only when supported by recorded measurements. The dashboard will include a Benchmark Mode control that compares a baseline voice pipeline with the SLNG-powered pipeline using consistent measurement definitions. Simulated values, if used during UI development, must be labelled as illustrative and must never be presented as live benchmark results.

**FR-18: Report Review**

Allow the operator to review the report and copy or export it.

**FR-19: Error Visibility**

Display understandable messages for failed connections, transcription failures, and unavailable voice output.

### 5.4 Regional Configuration

**FR-20: Region Visibility**

Display the configured SLNG speech-processing region.

**FR-21: Configuration Verification**

Record the configured speech provider, model, and region where available.

**FR-22: Residency Claims**

The interface must not claim complete regional data residency solely because a speech gateway has been selected. The relevant model, runtime, storage, logging, and data-routing configuration must be considered.

---

## 6. Technical Architecture

### 6.1 Architecture Overview

**A. Voice Agent — Unmute**

Defines the agent instructions, reasoning model, speech models, turn detection, and supported execution target.

**B. Voice Execution — SLNG**

Provides the configured speech-processing and voice-generation capabilities. The exact features depend on the selected models and runtime.

**C. Reasoning — LLM**

Classifies the incident, extracts structured fields, generates clarifying questions, and prepares the incident summary.

**D. Agent Runtime — Pipecat or LiveKit**

Runs the locally developed voice agent and connects it to the browser-based voice interaction.

SovereignPulse will use a single agent runtime for the MVP. **Pipecat will be evaluated first for Python-based voice-pipeline integration.** LiveKit will be considered only if it provides a more reliable supported path for browser connectivity. The final selection must be validated against the current Unmute and SLNG integrations before implementation.

**E. Frontend — Browser Interface**

Provides the microphone controls, conversation display, incident summary, and performance dashboard.

**F. Application Logic**

Validates extracted fields, tracks session events, calculates metrics, and stores reports if persistence is implemented.

### 6.2 Voice Data Flow

Browser microphone  
→ configured voice runtime (Pipecat first)  
→ SLNG-supported speech recognition  
→ LLM reasoning and incident extraction  
→ response generation  
→ SLNG-supported speech synthesis  
→ browser audio playback

The exact transport, streaming behavior, and event hooks will follow the selected runtime's supported integration.

### 6.3 Technology Stack

| Component | Technology |
|---|---|
| Voice-agent definition | Unmute YAML and Markdown |
| Speech execution | SLNG |
| Local agent runtime | Pipecat (evaluated first) or LiveKit |
| Reasoning | LLM supported by the selected configuration |
| Frontend | React, Vite, TypeScript |
| Audio | Browser Media APIs and Web Audio API |
| Application backend | Python (aligned with Pipecat) |
| Metrics | Runtime events and application instrumentation |
| Optional persistence | SQLite or JSON for the MVP |

### 6.4 Unmute Development Workflow

The implementation will follow the official Unmute workflow:

1. Install Unmute using the official instructions.
2. Initialize a project with `unmute init`.
3. Configure the agent, models, prompts, secrets, and targets using the generated project structure.
4. Run `unmute validate`.
5. Compile and run a browser-accessible development target using the documented command.
6. Verify the SLNG-powered voice path through an actual conversation.
7. Build the custom dashboard around the verified integration.
8. Deploy to the SLNG hosted target if supported by the finalized configuration and remaining time.

The SLNG hosted target is not the same as the local browser-development target. Local development and hosted deployment must be treated as separate execution modes.

Generated build files should not be edited directly; changes belong in the source agent package and should be compiled again.

---

## 7. Agent Configuration and Behavior

### 7.1 Agent Identity

SovereignPulse is a calm, concise operational reporting assistant.

### 7.2 Configuration Requirements

The Unmute package will define:

- Agent name and version
- Entry agent
- Agent instructions
- Reasoning model
- SLNG speech model
- SLNG transcription model
- Turn detector
- Supported browser channel
- Required secrets
- Execution target

The exact field names and model identifiers must follow the current Unmute configuration reference and the providers available to the account.

### 7.3 Secret Management

API keys must be stored in environment variables or the supported secret-management mechanism. Credentials must never be committed to GitHub or embedded in frontend code.

### 7.4 Agent Instructions

The agent must:

- Use concise spoken responses.
- Ask relevant questions to resolve missing information.
- Repeat critical extracted details for confirmation.
- Distinguish reported facts from uncertain information.
- Never claim that an external action has occurred without confirmation from an authorized integration.
- Avoid unsupported medical, legal, or emergency-response determinations.
- Produce a structured incident summary for human review.

---

## 8. Example Demonstration

### Initial Report

**Operator:** There has been a road accident near Exit 14. Two people are trapped, and I can see smoke.

**SovereignPulse:** I have recorded a road accident near Exit 14, with two people reported trapped and smoke visible. Is there any known fuel leak?

**Operator:** I don't know. Please mark it as unknown.

**SovereignPulse:** Understood. The fuel-leak status is unknown. Please confirm the exact location before submitting the incident report.

### Expected Dashboard Output

- Incident category: Road accident
- Location: Exit 14 — exact location unconfirmed
- People affected: Two reported trapped
- Smoke: Reported
- Fuel leak: Unknown
- Status: Awaiting operator review

This is a simulated incident workflow. It does not represent a confirmed emergency dispatch.

---

## 9. Performance and Benchmarking

### 9.1 Metrics

| Metric | Definition |
|---|---|
| First-audio latency | Time from end of user utterance to first audible agent response |
| Transcription latency | Speech-processing duration, when available |
| First-token latency | Time to first LLM output token, when available |
| Speech-generation latency | Time to first generated audio and total duration, when available |
| Completion rate | Successful end-to-end sessions divided by attempted sessions |
| Extraction accuracy | Correct extracted fields divided by verified expected fields |
| Token usage | Actual LLM tokens reported by the model provider |
| Interruption latency | Measured interruption-to-audio-stop time, if supported |
| Region configuration | Verified speech-processing region |

### 9.2 Benchmark Methodology (Benchmark Mode)

The baseline and SLNG-powered workflows must use equivalent test utterances, comparable prompts, and consistent measurement definitions.

The benchmark must:

1. Run repeated tests.
2. Record sample size and median latency.
3. Record the model and provider configuration.
4. Document relevant network and environment conditions.
5. Record actual token usage when available.
6. Identify any missing metrics rather than substituting invented values.
7. Label all illustrative UI mock values clearly during development.

### 9.3 Platform Claims Versus Project Results

SLNG advertises approximately 39% lower turn latency and 53% lower model costs for its platform. These figures will be presented as platform-reported claims, not as guaranteed results of SovereignPulse.

Project-specific improvements will be reported only after measurement.

### 9.4 Initial Success Targets

- Complete a real SLNG-powered voice conversation.
- Extract the required incident fields from the test scenarios.
- Display the transcript and structured report.
- Capture at least one valid end-to-end latency measurement.
- Demonstrate the actual Unmute configuration.
- Produce a repeatable live demonstration.

Numerical performance targets will be set after measuring the first working implementation.

---

## 10. User Interface Design

### 10.1 Visual Direction

Use a dark, professional operations-console interface with high-contrast typography, restrained accent colors, and clear status indicators.

### 10.2 Main Dashboard

**Voice Console**
- Start and end session
- Microphone status
- Audio waveform
- Listening and response indicators

**Conversation Feed**
- User transcript
- Agent response
- Connection and processing status

**Incident Intelligence**
- Incident category
- Location
- Priority
- Known hazards
- Missing information
- Review status

**Performance Monitor & Benchmark Mode**
- Benchmark Mode toggle (Baseline vs. SLNG Optimized)
- Measured first-audio latency
- Available processing timings
- Token usage
- Benchmark comparison with sample count
- Configured speech-processing region

Every displayed metric must be clearly labelled as measured, platform-reported, or a target.

---

## 11. Scope and Prioritization

### P0 — Mandatory

- Real SLNG-powered voice interaction
- Working Unmute configuration
- Local browser-based agent execution (via Pipecat or LiveKit)
- Incident extraction and summarization
- Live transcript
- Incident summary card
- Error handling
- Actual latency measurement

### P1 — Important Differentiators

- Clarifying questions and corrections
- Benchmark Mode comparison against a documented baseline
- Token usage telemetry
- Audio-reactive visualization
- Incident report export
- Verified regional configuration

### P2 — Stretch Goals

- Barge-in and interruption handling
- Noise-condition testing
- SLNG hosted deployment
- Additional runtime compilation
- Persistent incident history
- Advanced regional data-flow verification

P0 features must be complete before stretch features are attempted.

---

## 12. Three-Minute Hackathon Demo

### 0:00–0:30 — Problem

Explain the challenges of collecting accurate incident information through manual reporting.

### 0:30–1:20 — Live Voice Agent

Report a simulated incident. Answer a clarifying question and correct one detail. Show the transcript and structured report.

### 1:20–1:55 — SLNG and Unmute

Show the actual running voice integration and explain how Unmute defines the agent while SLNG provides the configured voice execution capabilities.

### 1:55–2:35 — Performance Evidence (Benchmark Mode)

Show actual response latency and available model usage. Switch on Benchmark Mode to compare results with the documented baseline, clearly labelling sample size and test conditions.

### 2:35–3:00 — Closing

Show the completed incident report and explain how the architecture can support additional operational workflows.

A prepared recording may be used as a fallback if the live provider or network becomes unavailable, but the recorded demo must be identified as such.

---

## 13. Risks and Mitigations

| Risk | Mitigation |
|---|---|
| Incorrect Unmute configuration | Start from the official scaffold and run validation |
| SLNG integration problems | Verify a complete conversation before building the custom dashboard |
| Excessive scope | Complete P0 before adding stretch features |
| Latency exceeds expectations | Measure processing stages and optimize based on evidence |
| Incorrect extraction | Validate fields and ask for confirmation |
| Microphone or network failure | Provide visible error handling and a prepared demo recording |
| Unsupported runtime behavior | Confirm feature support before promising it |
| Regional compliance overclaim | Verify the actual model, routing, runtime, and storage configuration |
| Misleading benchmark | Separate measured results from platform claims and targets |

---

## 14. Acceptance Criteria

SovereignPulse is ready for submission when:

1. A user can complete a real spoken conversation through the configured SLNG-powered voice path.
2. Unmute is used in the actual running implementation.
3. The agent produces a structured incident report.
4. The dashboard displays the conversation and incident details.
5. At least one performance metric is collected from actual runtime events.
6. The demo clearly explains SLNG's role in the architecture.
7. Missing or uncertain information is handled transparently.
8. No fabricated performance results or unconfirmed external actions are presented as facts.
9. The demonstration can be repeated reliably using the documented setup.

---

## 15. Final Product Positioning

SovereignPulse is a voice incident intelligence assistant that demonstrates the practical use of SLNG and Unmute in a real-time operational workflow.

Its value comes from combining natural speech, structured information extraction, explainable incident reporting, and observable voice-system performance.

**Core differentiator:** A working voice agent that transforms spoken incidents into structured records while making its execution and performance measurable.

**Hackathon strategy:** Prove the core voice workflow first, demonstrate SLNG and Unmute clearly, and use real measurements to substantiate every performance claim.
