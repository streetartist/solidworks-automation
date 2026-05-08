# ShowBubbleTooltipAt Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ShowBubbleTooltipAt`

Obsolete. Superseded by ISldWorks::ShowBubbleTooltipAt2.
Obsolete. Superseded by [ISldWorks::ShowBubbleTooltipAt2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ShowBubbleTooltipAt2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub ShowBubbleTooltipAt( _
   ByVal PointX As System.Integer, _
   ByVal PointY As System.Integer, _
   ByVal ArrowPos As System.Integer, _
   ByVal TitleString As System.String, _
   ByVal MessageString As System.String, _
   ByVal UrlLoc As System.String _
) 
```

```

Dim instance As ISldWorks
Dim PointX As System.Integer
Dim PointY As System.Integer
Dim ArrowPos As System.Integer
Dim TitleString As System.String
Dim MessageString As System.String
Dim UrlLoc As System.String
 
instance.ShowBubbleTooltipAt(PointX, PointY, ArrowPos, TitleString, MessageString, UrlLoc)
```

```

void ShowBubbleTooltipAt( 
   System.int PointX,
   System.int PointY,
   System.int ArrowPos,
   System.string TitleString,
   System.string MessageString,
   System.string UrlLoc
)
```

```

void ShowBubbleTooltipAt( 
   System.int PointX,
   System.int PointY,
   System.int ArrowPos,
   System.String^ TitleString,
   System.String^ MessageString,
   System.String^ UrlLoc
) 
```

#### Parameters

*PointX*
:   x coordinate in pixels relative to upper-left corner of  screen

*PointY*
:   y coordinate in pixels relative to upper-left corner of screen

*ArrowPos*
:   Arrow position as defined in [swArrowPosition](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swArrowPosition.html)

*TitleString*
:   Title of bubble ToolTip

*MessageString*
:   Message string of bubble ToolTip

*UrlLoc*
:   Any valid Windows Internet Explorer file (see **Remarks**)

Remarks

|  |  |
| --- | --- |
| **If you specified a ...** | **Then the ToolTip's bubble...** |
| gif, .jpg, or .jpeg image for urlLoc | Is automatically expanded to accommodate the image |
| URL for urlLoc | Cannot be resized; if the URL is:   - an HTML file, then the contents of the HTML file are displayed in the bubble ToolTip - to a website, then the default or specified web page at that website is displayed in the bubble ToolTip |

Example

**Visual Basic for Applications (VBA)**

'--------------------------------------------  
'  
' Preconditions: Specified HTML file exists at the specified location.  
'  
' Postconditions: Contents of the HTML file are displayed in a Bubble ToolTip.  
'  
'--------------------------------------------

Option Explicit  
   
Sub main()

    ' Substitute a valid HTML file for the string shown below

    Const sURLpath As String = "*path\_to\_a\_gif\_jpg\_or\_jpeg\_file\_or\_a\_URL*"  
     
    Dim swApp As SldWorks.SldWorks  
    Set swApp = Application.SldWorks

    ' Show Bubble ToolTip  
    swApp.**ShowBubbleTooltipAt** 300, 400, swArrowLeftTop, "Sample ShowBubbleTooltipAt", "Message of Sample ShowBubbleTooltipAt", sURLpath

End Sub

'--------------------------------------------

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)  
[ISldWorks::ShowBubbleTooltip Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ShowBubbleTooltip.md)
