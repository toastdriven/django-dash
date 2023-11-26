/**
 * <Errors
 *   messages={[
 *     "Error message for user goes here.",
 *     // ...more if needed...
 *   ]}
 * />
 */
export default function Errors({ messages, ...props }) {
  if (messages.length <= 0) {
    return;
  }

  return (
    <div className="mb-4 px-4 py-2 border-2 border-solid border-red-600 bg-red-300 text-red-600">
      <ul>
        {messages.map((msg) => (
          <li>{msg}</li>
        ))}
      </ul>
    </div>
  );
}
