/**
 * <Select
 *   name="input_name_goes_here"
 *   options={[
 *     { name: "human_readable", value: <any>, disabled: false | true },
 *     // ...
 *   ]}
 *   [value=<any>]
 *   onChange={handlerFunc}
 * />
 */
export default function Select({ name, options, onChange, value = null, ...props }) {
  function handleSelect(ev) {
    const newValue = ev.target.value;
    onChange(newValue);
  }

  return (
    <select
      name={name}
      className="p-2 bg-white border-solid border-2 border-grey-500 rounded-md w-full"
      onInput={handleSelect}
    >
      {options.map((option) => (
        <option
          value={option.value}
          selected={value.toString() === option.value.toString()}
          disabled={option.disabled === true}
        >{option.name}</option>
      ))}
    </select>
  );
}
