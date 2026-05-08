# DragToolbarButtonFromCommandID Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~DragToolbarButtonFromCommandID`

Copies a button to a toolbar using a command ID.
Copies a button to a toolbar using a command ID.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function DragToolbarButtonFromCommandID( _
   ByVal CommandID As System.Integer, _
   ByVal TargetToolbar As System.Integer, _
   ByVal TargetIndex As System.Integer _
) As System.Integer
```

```

Dim instance As ISldWorks
Dim CommandID As System.Integer
Dim TargetToolbar As System.Integer
Dim TargetIndex As System.Integer
Dim value As System.Integer
 
value = instance.DragToolbarButtonFromCommandID(CommandID, TargetToolbar, TargetIndex)
```

```

System.int DragToolbarButtonFromCommandID( 
   System.int CommandID,
   System.int TargetToolbar,
   System.int TargetIndex
)
```

```

System.int DragToolbarButtonFromCommandID( 
   System.int CommandID,
   System.int TargetToolbar,
   System.int TargetIndex
) 
```

#### Parameters

*CommandID*
:   Command ID as defined by [swCommands\_e](SOLIDWORKS.Interop.swcommands~SOLIDWORKS.Interop.swcommands.swCommands_e.md)

*TargetToolbar*
:   Toolbar as defined by [swToolbar\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swToolbar_e.html) or if a CommandGroup toolbar, use [ICommandGroup::ToolbarId](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~ToolbarId.md)

*TargetIndex*
:   0-based index of the toolbar button on the native SOLIDWORKS toolbar or CommandGroup toolbar

#### Return Value

Index of the toolbar or -1 if the button is not added

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)  
[ISldWorks::DragToolbarButton Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~DragToolbarButton.md)  
[ISldWorks::AddToolbar4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddToolbar4.md)  
[ISldWorks::AddToolbarCommand2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddToolbarCommand2.md)  
[ISldWorks::GetLastToolbarID Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetLastToolbarID.md)  
[ISldWorks::GetToolbarDock2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetToolbarDock2.md)  
[ISldWorks::GetToolbarState2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetToolbarState2.md)  
[ISldWorks::HideToolbar2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~HideToolbar2.md)  
[ISldWorks::RemoveToolbar2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RemoveToolbar2.md)  
[ISldWorks::SetToolbarDock2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetToolbarDock2.md)
