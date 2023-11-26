/**
 * <Button
 *   label="human_readable"
 *   [onClick={handlerFunc}]
 *   [type="button" | "submit"]
 *   [className="additional-custom-classes"]
 * />
 */
export default function Button({ label, onClick = undefined, type = 'button', className = '', ...props }) {
  const baseClasses = 'rounded-md border-2 px-4 py-2 font-bold';
  let activeClasses = `${baseClasses} ${className}`;

  function handleClick(ev) {
    if (onClick) {
      ev.preventDefault();
      return onClick();
    }

    // If there's no custom handling, allow the event to bubble up.
  }

  return (
    <button
      type={(type === 'submit') ? 'submit' : 'button'}
      className={activeClasses}
      onClick={handleClick}
    >{label}</button>
  );
}
