jQuery(document).ready(function($) 
{
	
		//add disable class for custom button//
	    document.getElementById('dvcustom').classList.add('dvcustom');
	    
	    //datepicker//
	    $('.datepicker').datepicker({dateFormat: 'dd-m-yy'});
	    $(".datepicker").datepicker();
	    
	    
	    $(document).on('click','#slide1 input[type="button"]',function(){
	    	
	    	var curVal = $(this).val();
	    	var preVal = $('#customStorageCondition').val();

	    	if(curVal == 'Space')
	    	{
	    		curVal = " ";
	    	}

	    	if(curVal == 'Del')
	    	{
	    		$('#customStorageCondition').val(preVal.slice(0,-1));
	    	}
	    	else
	    	{
	    		var finalVal = preVal.concat(curVal);
	    		$('#customStorageCondition').val(finalVal);
	    	}	
	    });

	    $(document).on('click','#addConditionBtn',function(){
	    	var val = $('#customStorageCondition').val();

	    	$('#customConditionContainer').append('<div class="part4_modal"><input type="checkbox" value="'+ val +'" checked> '+ val +'</div>');
	    	$('#customStorageCondition').val('');
	    });

	    $('#slide1').on('hidden.bs.modal', function () {
	    	$('#customStorageCondition').val('');
	    });
});

function ShowHideDiv(custom) 
{
	if(custom.checked == true)
	{
	    showLink();
	}
	else
	{
		disableLink();
	}
}
function disableLink()
{
	document.getElementById('dvcustom').disabled=true;
	document.getElementById('dvcustom').style.cursor = 'not-allowed';
	document.getElementById('dvcustom').style.background = 'grey';
	document.getElementById('dvcustom').classList.add('dvcustom')
}

function showLink()
{
	var css = '.button-blue : hover{ background:#384e69 }';
    document.getElementById('dvcustom').disabled=false;
	document.getElementById("dvcustom").style.cursor = "pointer";
	document.getElementById('dvcustom').style.background = '#3aa5d9';
	document.getElementById('dvcustom').style.cssText = css;
	document.getElementById('dvcustom').classList.remove('dvcustom')
}

function ShowHideTextarea(str) {
    var detail_text = document.getElementById("detail_text");
    detail_text.style.display = str.checked ? "block" : "none";
}
function get_uploaded_file(fl)
{
	var uploaded_link = document.getElementById("uploaded_link");
	uploaded_link.style.display = fl.checked ? "block" : "none";
}

