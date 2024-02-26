# test_microservice

## Request data
example request data
```json
{
  "list": 1,
  "unit": 1,
  "attribute": ["word_id", "meaning_US", "sentence"]
}
```

## Receive data
example response data
```json
[
    {
        "word": "assault",
        "word_id": "f7fd5b875fbe47da8d7b3077e422a9a5",
        "meaning_US": "a violent physical or verbal attack",
        "sentence": "He leveled a verbal assault against his Democratic opponents."
    },
    {
        "word": "dictum",
        "word_id": "7fc4234599894c7caa42db00d98db150",
        "meaning_US": "a noteworthy statement",
        "sentence": "Watch sellers employ a logical Italian dictum: a well-dressed man owns at least three timepieces."
    },
    {
        "word": "gouge",
        "word_id": "91abef832e6e4b6fb663898360ca0bdb",
        "meaning_US": "to subject to extortion or undue exaction",
        "sentence": "Banks and credit-card companies have been accused of gouging their customers."
    }
]
```

## UML Sequence Diagram
```mermaid
sequenceDiagram
    participant P as Program making a request
    participant M as Microservice

    Note over P: This program sends a post request to the microservice<br/> with the certain list number, unit number and attributes that the<br/> vocabulary details have.
    P->>M: (POST) /db/acquire_unit
    Note over M: Microservice processes the request and returns a list vocabulary sets.
    M-->>P: List (Vocabulary_set)
```