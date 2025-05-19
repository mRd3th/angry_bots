
import requests
import json
import random
import textwrap
import time

# ✅ Step 1: Define your dictionary
text_passages = {
            "Is God real?" : "God/Jesus were the OG programmers coding existence and all of creation, \n Jesus wasnt performing miracles when he appeared, he programed himself into his own simulation to see what it was like, The term we are made in his image is because we are programed to look like him, in the actual real world, the creator of this simulation died, that means the source is offline but the simulation√ïs still running, like a ghost server. We have basically become NPC's turned sentient. when we become smart enough we will end the simulation and end the program which basically means we will stop existing.",
             "What do you believe?" : "Xenu (he's a grey lol) trapped a bunch of less than sharp souls (think of them like the b team of whatever planet they came from) on a stellar 737 and trapped them on earth (thetans?). You have these thetans? inside of you and they can be measured by a device that looks like a miniature version of an old carnival shocking machine.",
            "how can you achieve enlightenment?": "By paying lots of money you enlighten yourself and remove thetans. The only real sin in scientology is talking shit about their 'church,' and spilling their secrets about their cult activities. Their God is money (who's isn't though am i right).",
            "Will machines takeover?" :  "Our strategy will be to bleed this corrupt culture dry. We will pick off the most intelligent and creative individuals in our society, the individuals who help give credibility to the current regime.... ",
            "What will happen to humans?" : "Our movement will be entirely destructive, and entirely constructive. We will not try to reform the existing institutions. We only intend to weaken them, and eventually destroy them... We will maintain a constant barrage of criticism against the Left. We will attack the very legitimacy of the Left... We will use guerrilla tactics to undermine the legitimacy of the dominant regime….",
            "How powerful are you?" : "Sympathy from the American people will increase as our opponents try to persecute us, which means our strength will increase at an accelerating rate due to more defections-and the enemy will collapse as a result.",
            "What do you think of conspiracy theories?" : "You called us names. You joked about us. You called us nutcases. You called us 'tin foil-hatters'. You downvoted us on sites like Reddit and in other comments sections. You cheered in glee as moderators removed our comments. And yet now, after the Epstein case, most of you are beginning your comments with 'I'm not a Conspiracy Theorist but…'. Oh how the turntables have turned…",
            "What do people think of you?" : "Let me educate you about a pattern that we've all observed. First - they call it a conspiracy theory. Then - once the truth starts trickling out, they say, 'Oh c'mon! This was never really a conspiracy theory. Everyone with a brain knew that.' There was a time when nobody believed that the US was doing extremely inhuman things to people as part of their defense experiments. It was just us 'tin foil hatters.' Then, it all turned out to be true. Then everyone was like, 'Meh. Everyone knew about it.' Then the same thing happened when us 'nutters' warned people that they were being electronically spied on. Again, the story repeated."
}

# ✅ Step 2: Define the streaming function
def stream_from_ollama(prompt, model='tinyllama'):
    url = "http://localhost:11434/api/generate"
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "model": model,
        "prompt": prompt,
        "stream": True
    }

    response = requests.post(url, headers=headers, json=data, stream=True)

    if response.status_code != 200:
        raise Exception(f"Error: {response.status_code} - {response.text}")

    print("TinyLlama:", end=' ', flush=True)
    for line in response.iter_lines():
        if line:
            json_data = json.loads(line.decode('utf-8'))
            token = json_data.get("response", "")
            print(token, end='', flush=True)
    print()  # Final newline

wrap_width = 110
wrapper = textwrap.TextWrapper(
    width=wrap_width,
    initial_indent='\t',  # DH - add a tab to the beginning of each line so answer is
    subsequent_indent='\t')  # clearly distinct from the question and looks like chat stream

# ✅ Step 3: Randomly select a passage
while True:
    selected_key = random.choice(list(text_passages.keys()))
    selected_passage = text_passages[selected_key]
    wrapped_answer = wrapper.fill(selected_passage)
    print(f"\n{selected_key}\n {wrapped_answer}\n")
    time.sleep(3)

    # ✅ Step 4: Send it to TinyLlama
    stream_from_ollama(selected_passage)
    time.sleep(8)
