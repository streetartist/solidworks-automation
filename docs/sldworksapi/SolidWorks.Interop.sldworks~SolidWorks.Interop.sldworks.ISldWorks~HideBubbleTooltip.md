# HideBubbleTooltip Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~HideBubbleTooltip`

Hides the bubble ToolTip displayed by ISldWorks::ShowBubbleTooltipAt2.
Hides the bubble ToolTip displayed by [ISldWorks::ShowBubbleTooltipAt2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ShowBubbleTooltipAt2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub HideBubbleTooltip() 
```

```

Dim instance As ISldWorks
 
instance.HideBubbleTooltip()
```

```

void HideBubbleTooltip()
```

```

void HideBubbleTooltip(); 
```

Example

The following examples show how to display and hide a bubble ToolTip. Click a link to jump to the example in that programming language.

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
