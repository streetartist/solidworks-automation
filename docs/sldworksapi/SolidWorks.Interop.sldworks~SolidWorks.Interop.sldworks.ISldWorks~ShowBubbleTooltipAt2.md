# ShowBubbleTooltipAt2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ShowBubbleTooltipAt2`

Displays a bubble ToolTip at the specified location.
Displays a bubble ToolTip at the specified location.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub ShowBubbleTooltipAt2( _
   ByVal PointX As System.Integer, _
   ByVal PointY As System.Integer, _
   ByVal ArrowPos As System.Integer, _
   ByVal TitleString As System.String, _
   ByVal MessageString As System.String, _
   ByVal TitleBitmapID As System.Integer, _
   ByVal TitleBitmap As System.String, _
   ByVal UrlLoc As System.String, _
   ByVal Cookie As System.Integer, _
   ByVal LinkStringID As System.Integer, _
   ByVal LinkString As System.String, _
   ByVal CallBack As System.String _
) 
```

```

Dim instance As ISldWorks
Dim PointX As System.Integer
Dim PointY As System.Integer
Dim ArrowPos As System.Integer
Dim TitleString As System.String
Dim MessageString As System.String
Dim TitleBitmapID As System.Integer
Dim TitleBitmap As System.String
Dim UrlLoc As System.String
Dim Cookie As System.Integer
Dim LinkStringID As System.Integer
Dim LinkString As System.String
Dim CallBack As System.String
 
instance.ShowBubbleTooltipAt2(PointX, PointY, ArrowPos, TitleString, MessageString, TitleBitmapID, TitleBitmap, UrlLoc, Cookie, LinkStringID, LinkString, CallBack)
```

```

void ShowBubbleTooltipAt2( 
   System.int PointX,
   System.int PointY,
   System.int ArrowPos,
   System.string TitleString,
   System.string MessageString,
   System.int TitleBitmapID,
   System.string TitleBitmap,
   System.string UrlLoc,
   System.int Cookie,
   System.int LinkStringID,
   System.string LinkString,
   System.string CallBack
)
```

```

void ShowBubbleTooltipAt2( 
   System.int PointX,
   System.int PointY,
   System.int ArrowPos,
   System.String^ TitleString,
   System.String^ MessageString,
   System.int TitleBitmapID,
   System.String^ TitleBitmap,
   System.String^ UrlLoc,
   System.int Cookie,
   System.int LinkStringID,
   System.String^ LinkString,
   System.String^ CallBack
) 
```

#### Parameters

*PointX*
:   x coordinate in pixels relative to upper-left corner of the screen (see **Remarks**)

*PointY*
:   y coordinate in pixels relative to upper-left corner of the screen (see **Remarks**)

*ArrowPos*
:   Arrow position as defined in [swArrowPosition](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swArrowPosition.html)

*TitleString*
:   Title of bubble ToolTip

*MessageString*
:   Message for bubble ToolTip

*TitleBitmapID*
:   ID of the bitmap to display in the bubble ToolTip as defined in [swBitMaps](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBitMaps.html) (see **Remarks**)

*TitleBitmap*
:   Path and filename of the bitmap to display before TitleString in the bubble ToolTip

*UrlLoc*
:   Any valid Windows Internet Explorer file to display in the body of the bubble ToolTip (see **Remarks**)

*Cookie*
:   Add-in's application ID specified in [ISwAddin::ConnectToSW](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.ISwAddin~ConnectToSW.md)

*LinkStringID*
:   ID of the hyperlink as defined in [swLinkString](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLinkString.html) (see **Remarks**)

*LinkString*
:   String to show as the hyperlink in the bubble ToolTip

*CallBack*
:   Name of the callback function for the hyperlink

Remarks

If PointX and PointY are both set to 0 and TitleBitmapID is swBitMapTreeError and a PropertyManager page is displayed, then the bubble ToolTip will appear in the same location as the SOLIDWORKS user-interface Rebuild Errors bubble ToolTip. You must specify both TitleBitmapID and TitleBitmap values.

|  |  |
| --- | --- |
| **If you specified a ...** | **Then the bubble ToolTip...** |
| gif, .jpg, or .jpeg image for UrlLoc | is automatically expanded to accommodate the image. |
| URL for UrlLoc | cannot be resized; if the URL:   - is an HTML file, then the contents of the HTML file are displayed in the bubble ToolTip. - links to a website, then the default or specified web page at that website is displayed in the bubble ToolTip. |

The Cookie, LinkStringID, LinkString, and Callback parameters are intended for use by add-in applications to display a hyperlink in the bubble ToolTip that, when clicked, calls a function to do something outside of the application; for example, open the add-in application's Help system.

Example

The following examples show how to display a bubble ToolTip. Click a link to jump to the example in that programming language.

- [C#](#CSharp)
- [VB.NET](#VBNET)
- [VBA](#VBA)

**C#**

//--------------------------------------------

// Preconditions: SOLIDWORKS is running. 

// Postconditions:

// (1) Bubble ToolTip is shown.

// (2) Bubble ToolTip is hidden.  

//--------------------------------------------

using SOLIDWORKS.Interop.sldworks;

using SOLIDWORKS.Interop.swconst;

using System;

namespace ShowBubbleToolTipAt2SldWorksCSharp.csproj

{

    public partial class SOLIDWORKSMacro

    {

        public void Main()

        {

           // Show bubble ToolTip

           swApp.**ShowBubbleTooltipAt2**(300, 400, (int)swArrowPosition.swArrowLeftTop, "Sample Bubble Tooltip", "Message of Sample Bubble ToolTip", (int)swBitMaps.swBitMapUserDefined, "C:\\Program Files\\SOLIDWORKS Corp\\SOLIDWORKS\\data\\user macro icons\\questionmark.bmp", "", 0, (int)swLinkString.swLinkStringNone, "", "");

        // 1. Insert a breakpoint at next command.

        // 2. Examine the SOLIDWORKS graphics area to see the bubble ToolTip.

        // 3. Toggle the breakpoint to hide the bubble ToolTip.

        swApp.HideBubbleTooltip();

        }

        /// <summary>

        /// The SldWorks swApp variable is pre-assigned for you.

        /// </summary>

        public SldWorks swApp;

    }

}

**VB.NET**

'--------------------------------------------

' Preconditions: SOLIDWORKS is running.

' Postconditions:

'   (1) Bubble ToolTip is shown.

'   (2) Bubble ToolTip is hidden.

'--------------------------------------------

Imports SOLIDWORKS.Interop.sldworks

Imports SOLIDWORKS.Interop.swconst

Imports System

Partial Class SOLIDWORKSMacro

Public Sub main()

    ' Show bubble ToolTip

    swApp.**ShowBubbleTooltipAt2**(300, 400, swArrowPosition.swArrowLeftTop, "Sample Bubble Tooltip", "Message of Sample Bubble ToolTip", swBitMaps.swBitMapUserDefined, "C:\Program Files\SOLIDWORKS Corp\SOLIDWORKS\data\user macro icons\questionmark.bmp", "", 0, swLinkString.swLinkStringNone, "", "")

    Stop

 

    swApp.HideBubbleTooltip()

End Sub

    ''' <summary>

    ''' The SldWorks swApp variable is pre-assigned for you.

    ''' </summary>

    Public swApp As SldWorks

End Class

**VBA**

'--------------------------------------------  
' Preconditions: SOLIDWORKS is running  
'  
' Postconditions:

'       (1) Bubble ToolTip is shown.

'       (2) Bubble ToolTip is hidden.  
'--------------------------------------------

Option Explicit  
   
Sub main()

     
    Dim swApp As SldWorks.SldWorks  
    Set swApp = Application.SldWorks

    ' Show Bubble ToolTip  
    swApp.**ShowBubbleTooltipAt2** 300, 400, swArrowLeftTop, "Sample Bubble Tooltip", "Message of Sample Bubble ToolTip", swBitMapUserDefined, "C:\Program Files\SOLIDWORKS Corp\SOLIDWORKS\data\user macro icons\questionmark.bmp", "", 0, swLinkStringNone, "", ""   

    Stop  
     
    swApp.HideBubbleTooltip  
    

    End Sub

'--------------------------------------------

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)  
[ISldWorks::ShowBubbleTooltip Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ShowBubbleTooltip.md)  
[ISldWorks::HideBubbleTooltip Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~HideBubbleTooltip.md)
