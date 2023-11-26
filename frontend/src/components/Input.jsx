/**
 * <Input
 *   name="input_name"
 *   [value=<any>]
 *   [type="text" | "password" | "hidden" | "radio" | "checkbox" | etc.]
 *   onChange={handlerFunc}
 * />
 */
export default function Input({ name, value = null, type = 'text', onChange, ...props }) {
  function handleChange(ev) {
    const newValue = ev.target.value;
    onChange(newValue);
  }

  return (
    <input
      type={(!type) ? "text" : type}
      name={name}
      value={value}
      onInput={handleChange}
      className="p-2 border-solid border-2 border-grey-500 rounded-md w-full"
    />
  );
}
