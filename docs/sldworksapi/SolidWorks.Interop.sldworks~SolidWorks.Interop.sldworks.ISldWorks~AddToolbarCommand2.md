# AddToolbarCommand2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddToolbarCommand2`

Specifies the application functions to call when a toolbar button is clicked or sets a separator.
Specifies the application functions to call when a toolbar button is clicked or sets a separator.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AddToolbarCommand2( _
   ByVal Cookie As System.Integer, _
   ByVal ToolbarId As System.Integer, _
   ByVal ToolbarIndex As System.Integer, _
   ByVal ButtonCallback As System.String, _
   ByVal ButtonEnableMethod As System.String, _
   ByVal ToolTip As System.String, _
   ByVal HintString As System.String _
) As System.Boolean
```

```

Dim instance As ISldWorks
Dim Cookie As System.Integer
Dim ToolbarId As System.Integer
Dim ToolbarIndex As System.Integer
Dim ButtonCallback As System.String
Dim ButtonEnableMethod As System.String
Dim ToolTip As System.String
Dim HintString As System.String
Dim value As System.Boolean
 
value = instance.AddToolbarCommand2(Cookie, ToolbarId, ToolbarIndex, ButtonCallback, ButtonEnableMethod, ToolTip, HintString)
```

```

System.bool AddToolbarCommand2( 
   System.int Cookie,
   System.int ToolbarId,
   System.int ToolbarIndex,
   System.string ButtonCallback,
   System.string ButtonEnableMethod,
   System.string ToolTip,
   System.string HintString
)
```

```

System.bool AddToolbarCommand2( 
   System.int Cookie,
   System.int ToolbarId,
   System.int ToolbarIndex,
   System.String^ ButtonCallback,
   System.String^ ButtonEnableMethod,
   System.String^ ToolTip,
   System.String^ HintString
) 
```

#### Parameters

*Cookie*
:   Resource ID of the toolbar; this is the same cookie that you specified in [ISwAddin::ConnectToSW](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.ISwAddin~ConnectToSW.md)

*ToolbarId*
:   Toolbar ID from [ISldWorks::AddToolbar5](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddToolbar5.md)

*ToolbarIndex*
:   0-based index of the bitmap button

*ButtonCallback*
:   Function called when the user clicks the button (see **Remarks**)

*ButtonEnableMethod*
:   Function called to check whether the button should be enabled; typically used to check the type of object selected (see Remarks)

*ToolTip*
:   ToolTip for the toolbar button

*HintString*
:   Text that SOLIDWORKS displays in the status bar when the user moves their mouse over this toolbar button

#### Return Value

True if successful, false if unsuccessful

Remarks

See [Add-in Callback and Enable Methods](sldworksapiprogguide.chm::/OVERVIEW/Add-in_Callbacks.htm) to learn how to specify ButtonCallback and ButtonEnableMethod.

Call this method to specify the functions that get called by the SOLIDWORKS software when the button is pressed and to check if the button is enabled. Until this method is called, the SOLIDWORKS software does not display the button.

| If ButtonEnableMethod returns... | **Then SOLIDWORKS...** |
| --- | --- |
| 0 | Deselects and disables the menu item |
| 1 | Deselects and enables the menu item; this is the default menu state if no update function is specified |
| 2 | Selects and disables the menu item |
| 3 | Selects and enables the menu item |

To create a separator, all of the method's string parameters (ButtonCallback, ButtonEnableMethod, ToolTip, and HintString) must be blank strings. A bitmap button must still be defined in the add-in's resources, but it is not used.

Example

[Create Toolbars (C++)](Create_Toolbars_Example_CPlusPlus_COM.htm)  
[Add Toolbars (C#)](Add_Toolbars_Example_CSharp.htm)  
[Add Toolbars (VB.NET)](Add_Toolbars_Example_VBNET.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)  
[ISldWorks::AddMenu Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddMenu.md)  
[ISldWorks::AddMenuItem3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddMenuItem3.md)  
[ISldWorks::AddMenuPopupItem2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddMenuPopupItem2.md)  
[ISldWorks::RemoveFromMenu Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RemoveFromMenu.md)  
[ISldWorks::RemoveFromPopupMenu Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RemoveFromPopupMenu.md)  
[ISldWorks::RemoveMenu Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RemoveMenu.md)  
[ISldWorks::RemoveMenuPopupItem2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RemoveMenuPopupItem2.md)  
[ISldWorks::RemoveToolbar2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RemoveToolbar2.md)  
[ISldWorks::DragToolbarButton Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~DragToolbarButton.md)  
[ISldWorks::GetToolbarDock2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetToolbarDock2.md)  
[ISldWorks::GetToolbarState2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetToolbarState2.md)  
[ISldWorks::HideToolbar2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~HideToolbar2.md)  
[ISldWorks::SetToolbarDock2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetToolbarDock2.md)
