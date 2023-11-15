import { useEffect, useState } from 'react'
import { ButtonSelect } from './components/buttonSelect'
import { GraphLine } from './components/graph'



export function App() {

  const [valueDisease,SetValueDisease] = useState("")


  return (
    <div className="grid grid-cols-2 h-screen bg-gray-50">
      <div>
        <div className="py-10 px-28">
          <div className="flex mt-28 gap-10 w-full ">
            
            <ButtonSelect label='teste' SetValueDisease={SetValueDisease}/>
            <ButtonSelect label='teste2' SetValueDisease={SetValueDisease}/>
            <ButtonSelect label='teste3' SetValueDisease={SetValueDisease}/>
            <ButtonSelect label='teste4' SetValueDisease={SetValueDisease}/>
            
          </div>
          <div className='mt-14'>

          <GraphLine/>
          </div>
        </div>
      </div>
      <div className="bg-img-purple bg-cover bg-no-repeat" />
    </div>
  )
}

