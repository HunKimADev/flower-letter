import React from 'react';
import styled from 'styled-components';

const PreviewFrame = styled.div`
    width: 300px;
    position: relative;
    margin: 50px;

    .cover{
        width: 300px;
        position: relative;
    }
    .flower{
        position: absolute;
        height: 240px;
        left:40px;
        bottom: 30px;
    }
    .label{
        position: absolute;
        width:300px;
        left:0;
        bottom:0;
    }
    .title{
        position: absolute;
        top: 80px;
        right: 30px;
        font-family: sungsil;
        font-size: 1.7rem;
        color: ${props => props.textColor};
    }

`;

function Preview () {
    const text = "네가 지나간 자리에" //스테이트로 관리
    const currentCover = {
        src: "../resources/black_cover.png",
        textColor: '#ffffff'
    }
    return(<div>
        <PreviewFrame textColor={currentCover.textColor}>
            <img className="cover" src={require("../resources/black_cover.png").default}/>
            <img className="flower" src={require("../resources/rotus.png").default} />
            <img className="label" src={require("../resources/black_label.png").default}/>
            <div className="title">{text}</div>
        </PreviewFrame>
    </div>);
}


export default Preview;