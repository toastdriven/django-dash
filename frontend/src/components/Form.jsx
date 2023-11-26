/**
 * <Form
 *   onSubmit={handlerFunc}
 * >
 *   // Form child elements here...
 * </Form>
 */
export default function Form({ onSubmit, ...props }) {
  function handleSubmit(ev) {
    ev.preventDefault();
    onSubmit();
  }

  return (
    <form
      onSubmit={handleSubmit}
    >
      {props.children}
    </form>
  );
}
