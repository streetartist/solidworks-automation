# ShowBubbleTooltip Method (ISldWorks)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ShowBubbleTooltip`

Displays a bubble ToolTip }}-->and flashes the specified toolbar button.
Displays a bubble ToolTip and flashes the specified toolbar button.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub ShowBubbleTooltip( _
   ByVal PointAt As System.Integer, _
   ByVal FlashButtonIDs As System.String, _
   ByVal TitleResID As System.Integer, _
   ByVal TitleString As System.String, _
   ByVal MessageString As System.String _
) 
```

```

Dim instance As ISldWorks
Dim PointAt As System.Integer
Dim FlashButtonIDs As System.String
Dim TitleResID As System.Integer
Dim TitleString As System.String
Dim MessageString As System.String
 
instance.ShowBubbleTooltip(PointAt, FlashButtonIDs, TitleResID, TitleString, MessageString)
```

```

void ShowBubbleTooltip( 
   System.int PointAt,
   System.string FlashButtonIDs,
   System.int TitleResID,
   System.string TitleString,
   System.string MessageString
)
```

```

void ShowBubbleTooltip( 
   System.int PointAt,
   System.String^ FlashButtonIDs,
   System.int TitleResID,
   System.String^ TitleString,
   System.String^ MessageString
) 
```

#### Parameters

*PointAt*
:   Toolbar button ID

*FlashButtonIDs*
:   Array of strings for the toolbar buttons

*TitleResID*
:   Title resource ID of bubble Tooltip or 0

*TitleString*
:   Title of bubble ToolTip

*MessageString*
:   Message string of bubble ToolTip

Example

[Flash an Add-in's Toolbar Button (VBA)](Flash_an_Add-in_s_Toolbar_Button_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)  
[ISldWorks::ShowBubbleTooltipAt2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ShowBubbleTooltipAt2.md)
