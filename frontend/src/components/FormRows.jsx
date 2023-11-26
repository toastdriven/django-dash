/**
 * <InlineFormRow
 *   name="input_name"
 *   label="human_readable"
 * >
 *   // Input element here...
 * </InlineFormRow>
 */
export function InlineFormRow({ name, label, ...props }) {
  return (
    <div className="grid grid-cols-2 mb-2">
      <label
        for={name}
        className="inline-block mr-2 font-bold"
      >{label}</label>
      {props.children}
    </div>
  );
}

/**
 * <StackedFormRow
 *   name="input_name"
 *   label="human_readable"
 * >
 *   // Input element here...
 * </StackedFormRow>
 */
export function StackedFormRow({ name, label, ...props }) {
  return (
    <div className="mb-2">
      <label
        for={name}
        className="block mb-2 mr-2 font-bold"
      >{label}</label>
      {props.children}
    </div>
  );
}
