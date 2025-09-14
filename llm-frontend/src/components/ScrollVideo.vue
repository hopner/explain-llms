<script setup>
import { ref, onMounted } from "vue";

const props = defineProps({
    videoSrc: { type: String, required: true }
});

const videoEl = ref(null);
const textContainer = ref(null);

onMounted(() => {
    const video = videoEl.value;
    const container = textContainer.value;

    video.addEventListener("loadedmetadata", () => {
        const duration = video.duration;

        container.addEventListener("scroll", () => {
            const scrollTop = container.scrollTop;
            const scrollHeight = container.scrollHeight - container.clientHeight;
            const fraction = scrollTop / scrollHeight;

            video.currentTime = fraction * duration;
        });
    });
});
</script>


<template>
    <div class="scroll-video">
        <div class="video-container">
            <video ref="videoEl" preload="auto">
                <source :src="videoSrc" type="video/mp4" />
            </video>
        </div>

        <div ref="textContainer" class="text-container">
            <slot />
        </div>
    </div>
</template>


<style scoped>
.scroll-video {
    margin: 0;
    font-family: sans-serif;
    display: flex;
    height: 100vh;
}

.video-container {
    flex: 1;
    position: sticky;
    top: 0;
    height: 100vh;
    background: black;
    display: flex;
    justify-content: center;
    align-items: center;
}

video {
    max-width: 100%;
    max-height: 100%;
}

.text-container {
    flex: 1;
    overflow-y: scroll;
    padding: 3rem;
}

.step {
    height: 100vh;
    display: flex;
    align-items: center;
    font-size: 1.2rem;
}
</style>
