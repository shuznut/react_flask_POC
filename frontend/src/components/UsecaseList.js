import React from 'react'

function UsecaseList(props) {

    const editUsecase = (usecase) => {
        props.editUsecase(usecase)
    }

    return (
        <div>
            {props.usecases && props.usecases.map(usecase => {
                return (
                    <div key={usecase.usecase_id}>
                        <h2>{usecase.usecase_name}</h2>
                        <p>{usecase.usecase_shortcode}</p>
                        <p>{usecase.usecase_startDate}</p>

                        <div className='row'>
                            <div className='col-md-1'>
                                <button className='btn btn-info' onClick={() => editUsecase(usecase)}>Update</button>
                            </div>
                            <div className='col'>
                                <button className='btn btn-info'>Delete</button>
                            </div>

                        </div>
                        <hr/>


                    </div>
                )
            })}
        </div>
    )
}

export default UsecaseList