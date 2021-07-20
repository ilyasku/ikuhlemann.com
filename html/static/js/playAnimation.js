var x=0;

ani=document.getElementById("HR");
descr=document.getElementById("animationDescription")
btnPrev=document.getElementById("buttonPrev")
btnRep=document.getElementById("buttonRep")
btnNext=document.getElementById("buttonNext")

cases=[
    ["Press button to start animation.","../images/HRDAnimation.png",["noOption","noOption",""]],
    ["When the object passes the left photoreceptor, the photoreceptor's response is sent along two pathways.","../images/animation_part_1.gif",["","",""]],
    ["The signal on the left pathway gets delayed, the other one does not.","../images/animation_part_2.gif",["","",""]],
    ["The fast signal reaches the right M alone, no output is evoked there and the signal vanishes.","../images/animation_part_3.gif",["","",""]],
    ["At the left M two signals coincide. They multiply to a larger and, more importantly, non-zero output.","../images/animation_part_4.gif",["","",""]],
    ["The left M's output reaches the output stage. It's transduced unaltered, since there is no input from the the other M.","../images/animation_part_5.gif",["","","noOption"]],
]

function changeIt(key) {
    
    var new_x;
    new_x=x+key;
    if (new_x<0) {
	new_x=0;
    }
    x=new_x%6;

    descr.innerHTML=cases[x][0];
    ani.src=cases[x][1];
    btnPrev.className=cases[x][2][0];
    btnRep.className=cases[x][2][1];
    btnNext.className=cases[x][2][2];
}

