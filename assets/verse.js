(function(){
"use strict";
/* 1. Meditation timer (progressive enhancement: the steps work without it) */
try{
var ol=document.querySelector("ol.med");
if(ol){
 var steps=[].slice.call(ol.querySelectorAll("li")),total=0,rng=[];
 steps.forEach(function(li){var m=(li.querySelector(".mn")||{}).textContent||"";var n=m.match(/\d+/g);
  if(n){var a=+n[0],b=+n[n.length-1];rng.push([a,b]);if(b>total)total=b}else{rng.push(null)}});
 if(total>0&&rng.every(Boolean)){
  var bar=document.createElement("div");bar.className="mtimer";
  bar.innerHTML='<button type="button" class="btn-s" data-a="go">Begin the '+total+'-minute practice</button> <button type="button" class="btn-s ghost" data-a="reset" hidden>Reset</button><span class="mclock" aria-hidden="true"></span><span class="sr" role="status" aria-live="polite"></span>';
  ol.parentNode.insertBefore(bar,ol);
  var go=bar.querySelector('[data-a="go"]'),rs=bar.querySelector('[data-a="reset"]'),clk=bar.querySelector(".mclock"),sr=bar.querySelector(".sr");
  var left=total*60,t=null,running=false,last=-1;
  function fmt(x){var m=Math.floor(x/60),s=x%60;return m+":"+(s<10?"0":"")+s}
  function paint(){
   var el=total*60-left,min=Math.min(total,Math.floor(el/60)+1),idx=-1;
   steps.forEach(function(li,i){var r=rng[i],on=running&&min>=r[0]&&min<=r[1];li.classList.toggle("now",on);if(on)idx=i});
   clk.textContent=left>0?fmt(left):"";
   if(idx!==last&&idx>=0){sr.textContent="Minute "+min;last=idx}
  }
  function stop(done){clearInterval(t);running=false;last=-1;steps.forEach(function(li){li.classList.remove("now")});
   if(done){clk.textContent="Practice complete. Take a slow breath.";sr.textContent="Practice complete";go.textContent="Begin again";left=total*60}
   else{clk.textContent=""}}
  go.addEventListener("click",function(){
   if(!running){running=true;if(left<=0)left=total*60;go.textContent="Pause";rs.hidden=false;paint();
    t=setInterval(function(){left--;if(left<=0){stop(true);return}paint()},1000)}
   else{clearInterval(t);running=false;go.textContent="Resume";steps.forEach(function(li){li.classList.remove("now")})}
  });
  rs.addEventListener("click",function(){stop(false);left=total*60;go.textContent="Begin the "+total+"-minute practice";rs.hidden=true});
 }
}
}catch(e){}
/* 2. Sketch note: full-screen view */
try{
var wrap=document.querySelector(".sk-wrap");
if(wrap&&typeof HTMLDialogElement==="function"){
 var act=document.querySelector(".sk-act");
 var b=document.createElement("button");b.type="button";b.className="btn-s ghost";b.textContent="View full screen";
 var d=document.createElement("dialog");d.className="skdlg";d.setAttribute("aria-label","Sketch note, full screen");
 d.innerHTML='<button type="button" class="skx" aria-label="Close">Close ✕</button><div class="skbody"></div>';
 document.body.appendChild(d);
 b.addEventListener("click",function(){d.querySelector(".skbody").innerHTML=wrap.innerHTML;d.showModal()});
 d.addEventListener("click",function(e){if(e.target===d||e.target.className==="skx")d.close()});
 if(act)act.appendChild(b);
}
}catch(e){}
})();
/* 3. Open-sky verse pages: reading progress, soft reveals, light parallax (all optional) */
(function(){try{
var d=document,root=d.documentElement,calm=window.matchMedia&&matchMedia("(prefers-reduced-motion: reduce)").matches;
if(!d.querySelector(".vwide"))return;
var bar=d.createElement("div");bar.id="vprog";bar.setAttribute("aria-hidden","true");d.body.appendChild(bar);
var hero=d.querySelector(".vhero"),tk=false;
function fr(){tk=false;var h=root.scrollHeight-innerHeight,y=window.pageYOffset;bar.style.transform="scaleX("+(h>0?Math.min(1,y/h):0).toFixed(3)+")";
 if(hero&&!calm){hero.style.setProperty("--vy",Math.min(y,600).toFixed(0))}}
addEventListener("scroll",function(){if(!tk){tk=true;requestAnimationFrame(fr)}},{passive:true});addEventListener("resize",fr);fr();
if(calm||!("IntersectionObserver" in window))return;
var sd=d.querySelector(".ov-verse .deva");if(sd)sd.classList.add("shim");
root.classList.add("js");
var sel=".ov-card,.card.ins,.story>*,.word,ol.med li,.reflect,.closing,table.wtable tbody tr";
var els=[].slice.call(d.querySelectorAll(sel)).filter(function(e){return e.getBoundingClientRect().top>innerHeight*0.92});
els.forEach(function(e,i){e.classList.add("vrv");e.style.setProperty("--d",((i%3)*0.07).toFixed(2)+"s")});
var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add("in");io.unobserve(e.target)}})},{rootMargin:"0px 0px -6% 0px",threshold:0.05});
els.forEach(function(e){io.observe(e)});
}catch(e){}})();
