# Comic-Specific Feature Specification

The domain model should emphasize **narrative structure + Vietnamese text + editing style**, not only generic object recognition.

## 1. Hook features — first 0–3 seconds

Extract separately from the full-video representation:

- `hook_visual_embedding`
- `hook_text_embedding`
- `hook_audio_embedding`
- `hook_scene_changes`
- `hook_text_density`
- `hook_contains_question`
- `hook_contains_number`
- `hook_contains_superlative`
- `hook_conflict_signal`
- `hook_emotion_signal`

Reason: two videos can contain visually similar comic panels but have very different opening propositions.

## 2. Vietnamese language features

Sources:
- caption;
- hashtags;
- ASR transcript;
- OCR;
- first-3-second hook text.

Representations:
- multilingual SentenceTransformer baseline;
- optional Vietnamese-specific encoder later;
- lexical/structural features for explainability.

Useful handcrafted features:
- question mark / interrogative phrase;
- sentiment/emotion;
- first-person narration;
- recommendation phrases;
- suspense/cliffhanger phrases;
- CTA phrases;
- entity/title mentions.

## 3. Story structure

Approximate timeline:

```text
0–3s      hook
3–10s     setup
10–80%    development / conflict
last 20%  payoff / cliffhanger / CTA
```

Candidate binary/continuous features:
- conflict appears by second N;
- protagonist introduced by second N;
- antagonist introduced;
- twist signal;
- payoff signal;
- cliffhanger signal;
- CTA duration;
- speech rate;
- information density over time.

## 4. Comic visual features

Possible features:
- panel count estimate;
- average panel dwell time;
- panel switches/sec;
- zoom/pan presence;
- speech-bubble OCR density;
- subtitle density;
- face close-up ratio;
- static vs animated proportion;
- grayscale/color ratio;
- template overlay;
- real-person intro/outro;
- split screen.

These can start as weak heuristics; do not delay the project trying to perfectly detect every visual attribute.

## 5. Audio

Important domain categories:
- human narration;
- TTS narration;
- character dub/dialogue;
- background music;
- trending sound;
- low/no speech.

Default features:
- MFCC;
- tempo;
- energy;
- speech/non-speech ratio.

## 6. Platform/context features

Keep separate:
- `platform`;
- posting hour;
- posting weekday;
- creator historical baseline;
- account size;
- sound usage count if legally/technically available at posting time;
- trend-cluster momentum at posting time.

## 7. Recommended MVP feature bundle

For the first domain experiment, implement only:

1. CLIP full-video embedding;
2. CLIP first-3-second embedding;
3. Vietnamese caption + transcript embedding;
4. first-3-second hook text embedding;
5. MFCC audio features;
6. duration, cuts/sec, caption length, hashtag count;
7. platform;
8. creator baseline.

That is enough to test whether the domain extension adds value before investing in complex comic-specific detectors.
