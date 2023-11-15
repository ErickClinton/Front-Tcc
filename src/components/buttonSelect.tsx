import React, { useState } from "react";

interface IButtonSelect {
  label: string;
  SetValueDisease: any;
}

export const ButtonSelect: React.FC<IButtonSelect> = ({
  label,
  SetValueDisease,
}) => {
  const [isSelected, setIsSelected] = useState(false);

  const handleClick = () => {
    SetValueDisease(label);
    setIsSelected(!isSelected);
  };

  const buttonClass = isSelected ? "bg-purple-500 text-white" : "bg-white";

  return (
    <div className="w-48 h-10">
      <button
        className={`border-purple-500 ${buttonClass} border-2 w-full h-full rounded-3xl hover:bg-purple-500 duration-500 text-lg`}
        onClick={handleClick}
      >
        {label}
      </button>
    </div>
  );
};
