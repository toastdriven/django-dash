const DEFAULT_COLORS = [
  'red-500',
  'pink-500',
  'orange-500',
  'yellow-500',
  'green-500',
  'blue-500',
  'purple-500',
  'slate-400',
];

function colorForName(name, options) {
  let accum = 0;

  for (let i = 0; i < name.length; i++) {
    accum += name.codePointAt(i);
  }

  const offset = accum % options.length;
  return options[offset];
}

/**
 * <Avatar
 *   name="name_or_initials"
 *   [size={size_number}]
 *   [roundingAmount='full' | 'lg' | 'md' | 'sm' | 'none']
 *   [imageUrl={image_url_here}]
 *   [color="specific-tailwind-color-name"]
 *   [colorOptions={[
 *     "specific-tailwind-color-name"
 *     // More colors...
 *   ]}]
 * />
 */
export default function Avatar({
  name,
  size = 8,
  roundingAmount = 'full',
  imageUrl = null,
  color = null,
  colorOptions = DEFAULT_COLORS,
  ...props
}) {
  const classes = [
    `h-${size}`,
    `w-${size}`,
    `rounded-${roundingAmount}`,
    'text-white',
    'font-bold',
    'flex',
    'items-center',
    'justify-center',
  ];
  let adjustedSize = 'sm';

  // Adjust font size based on overall size.
  if (size <= 8) {
    adjustedSize = 'xs';
  } else if (size <= 24) {
    adjustedSize = 'md';
  } else {
    adjustedSize = '2xl';
  }

  classes.push(`text-${adjustedSize}`);

  if (imageUrl) {
    return (
      <img
        src={imageUrl}
        className={classes.join(' ')}
        alt={name}
      />
    );
  }

  if (color !== null) {
    // If a color is provided, use that.
    classes.push(`bg-${color}`);
  } else {
    // Otherwise, choose a consistent pseudo-random color based on name.
    classes.push(`bg-${colorForName(name, colorOptions)}`);
  }

  return (
    <div className={classes.join(' ')}>
      {name.substr(0, 3)}
    </div>
  );
}
