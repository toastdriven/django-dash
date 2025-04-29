import { Header } from "@/components/Header";
import { MainContent } from "@/components/MainContent";
import { Footer } from "@/components/Footer";

export function Home() {
  return (
    <>
      <Header />

      <MainContent>
        <h1 class="text-5xl font-bold mb-8">Coming Soon</h1>

        <p>
          The 2025 Django Dash is currently being planned/organized/built-out.
        </p>

        <p>
          Please follow us on Mastodon at{" "}
          <a href="https://hachyderm.io/@djangodash">
            @djangodash@hackyderm.io
          </a>{" "}
          for updates!
        </p>

        <p>
          You can also join the discussion on{" "}
          <a href="https://discord.gg/t3bB38QXv3">Discord</a>! Competitors &
          spectators welcome!
        </p>
      </MainContent>

      <Footer />
    </>
  );
}
