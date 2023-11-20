import { useEffect, useState } from 'react'
import { ButtonSelect } from './components/buttonSelect'
import { GraphLine } from './components/graph'



export function App() {

  const [valueDisease,SetValueDisease] = useState("Grafico BoxPlot")
  console.log(valueDisease)
  return (
    <div className="grid grid-cols-2 h-screen bg-gray-50">
      <div>
        <div className="py-10 px-28">
          <div className="flex mt-28 gap-10 w-full ">
            
            <ButtonSelect label='Grafico de morte por estado' SetValueDisease={SetValueDisease} onChangeValue={valueDisease}/>
            <ButtonSelect label='Grafico BoxPlot' SetValueDisease={SetValueDisease} onChangeValue={valueDisease}/>
            <ButtonSelect label='Grafico com mais casos' SetValueDisease={SetValueDisease} onChangeValue={valueDisease}/>

          </div>
          <div className='mt-14'>

          <GraphLine selectButton={valueDisease}/>
          </div>
        </div>
      </div>
      <div className="bg-img-purple bg-cover bg-no-repeat" />
    </div>
  )
}