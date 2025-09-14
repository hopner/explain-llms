import { ref } from "vue";

/**
 * Returns a single video URL for a scene
 * @param basePath - Base path to media (e.g., "/media/videos/simple/480p15")
 * @param sceneName - Name of the scene folder
 */
export function useSceneVideo(basePath: string, sceneName: string) {
  const video = ref<string>("");

  const load = async () => {
    // Stitched video location
    video.value = `${basePath}/videos/${sceneName}.mp4`;
  };

  return { video, load };
}
