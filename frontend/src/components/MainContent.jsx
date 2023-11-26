export function MainContent({ ...props }) {
  return (
    <div
      class="pt-8 pb-16 bg-cyan-100"
    >
      <div class="center-column">
        {props.children}
      </div>
    </div>
  );
}
