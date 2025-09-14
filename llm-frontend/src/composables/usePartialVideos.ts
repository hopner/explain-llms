import { ref } from "vue";

export function usePartialVideos(basePath: string, sceneName: string) {
  const videos = ref<string[]>([]);

  const load = async () => {
    const listPath = `${basePath}/${sceneName}/partial_movie_file_list.txt`;

    try {
      const res = await fetch(listPath);
      if (!res.ok) throw new Error("Partial list not found");

      const text = await res.text();

      videos.value = text
        .split("\n")
        .map(line => line.trim())
        .filter(line => line.length > 0 && !line.startsWith("#"))
        .map(line => {
          // line format: file 'file:/absolute/path/to/video.mp4'
          const match = line.match(/file\s+'file:.+\/(.+\.mp4)'/);
          if (match && match[1]) {
            return `${basePath}/${sceneName}/${match[1]}`; // public URL
          }
          return null;
        })
        .filter((v): v is string => v !== null); // remove nulls
    } catch (err) {
      console.warn(`Partial videos not found for scene: ${sceneName}`, err);
      videos.value = [];
    }
  };

  return { videos, load };
}
