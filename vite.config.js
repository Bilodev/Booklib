import { svelte } from "@sveltejs/vite-plugin-svelte";
import { defineConfig, loadEnv } from "vite";

export default defineConfig(({ mode }) => {
  const env = loadEnv(mode, process.cwd());

  const PORT = `${env.CLIENT_PORT ?? "3000"}`;

  return {
    server: {
      port: PORT,
    },
    build: {
      outDir: "public",
    },
    plugins: [svelte()],
  };
});
