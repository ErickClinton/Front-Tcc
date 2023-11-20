import React, { useState } from "react";

interface IButtonSelect {
  label: string;
  SetValueDisease: any;
  onChangeValue:string
}

export const ButtonSelect: React.FC<IButtonSelect> = ({
  label,
  SetValueDisease,
  onChangeValue
}) => {

  const handleClick = () => {
    SetValueDisease(label);
  };

  const buttonClass = onChangeValue == label ? "bg-purple-500 text-white" : "bg-white";

  return (
    <div className="w-48 h-14">
      <button
        className={`border-purple-500 ${buttonClass} border-2 w-full h-full rounded-3xl hover:bg-purple-500 duration-500 text-lg`}
        onClick={handleClick}
      >
        {label}
      </button>
    </div>
  );
};
