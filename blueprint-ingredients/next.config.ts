import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  output: 'export',
  distDir: 'dist',
  basePath: '/blueprint-research/blueprint-ingredients/dist',
  assetPrefix: '/blueprint-research/blueprint-ingredients/dist',
  images: {
    unoptimized: true,
  },
  trailingSlash: true,
};

export default nextConfig;
