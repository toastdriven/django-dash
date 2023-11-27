export function MainContent({ ...props }) {
  return (
    <div
      class="pt-8 pb-16 bg-cyan-50"
    >
      <div class="center-column">
        {props.children}
      </div>
    </div>
  );
}
