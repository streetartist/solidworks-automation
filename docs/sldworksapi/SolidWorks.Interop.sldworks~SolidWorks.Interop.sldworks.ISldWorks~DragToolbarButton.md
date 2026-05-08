# DragToolbarButton Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~DragToolbarButton`

Copies the specified toolbar button from the specified native SOLIDWORKS toolbar or ICommandGroup toolbar to the specified native SOLIDWORKS toolbar or ICommandGroup toolbar.
Copies the specified toolbar button from the specified native SOLIDWORKS toolbar or [ICommandGroup](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup.md) toolbar to the specified native SOLIDWORKS toolbar or ICommandGroup toolbar.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub DragToolbarButton( _
   ByVal SourceToolbar As System.Integer, _
   ByVal TargetToolbar As System.Integer, _
   ByVal SourceIndex As System.Integer, _
   ByVal TargetIndex As System.Integer _
) 
```

```

Dim instance As ISldWorks
Dim SourceToolbar As System.Integer
Dim TargetToolbar As System.Integer
Dim SourceIndex As System.Integer
Dim TargetIndex As System.Integer
 
instance.DragToolbarButton(SourceToolbar, TargetToolbar, SourceIndex, TargetIndex)
```

```

void DragToolbarButton( 
   System.int SourceToolbar,
   System.int TargetToolbar,
   System.int SourceIndex,
   System.int TargetIndex
)
```

```

void DragToolbarButton( 
   System.int SourceToolbar,
   System.int TargetToolbar,
   System.int SourceIndex,
   System.int TargetIndex
) 
```

#### Parameters

*SourceToolbar*
:   Toolbar as defined by [swToolbar\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swToolbar_e.html) or if a CommandGroup toolbar, use [ICommandGroup::ToolbarId](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~ToolbarId.md)

*TargetToolbar*
:   Toolbar as defined by [swToolbar\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swToolbar_e.html) or if a CommandGroup toolbar, use [ICommandGroup::ToolbarId](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~ToolbarId.md)

*SourceIndex*
:   0-based index of the toolbar button on the native SOLIDWORKS toolbar or CommandGroup toolbar

*TargetIndex*
:   0-based index of the toolbar button on the native SOLIDWORKS toolbar or CommandGroup toolbar

Remarks

This method makes a copy of the specified source toolbar button and moves a copy of the toolbar button to the target toolbar. This method does not remove the specified source toolbar button from the source toolbar.

Examine the toolbars in the user interface to determine the values for SourceIndex and TargetIndex.

Using this method to drag a toolbar button from one toolbar to another is persistent across sessions of SOLIDWORKS and need only be performed once. For example, do not include this operation in any SolidsWorks API start-up routine because you would then be adding a copy of the same toolbar button to the same target toolbar every time you start up SOLIDWORKS.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)  
[ISldWorks::AddToolbar4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddToolbar4.md)  
[ISldWorks::AddToolbarCommand2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddToolbarCommand2.md)  
[ISldWorks::GetCommandID Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetCommandID.md)  
[ISldWorks::GetLastToolbarID Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetLastToolbarID.md)  
[ISldWorks::GetToolbarDock2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetToolbarDock2.md)  
[ISldWorks::GetToolbarState2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetToolbarState2.md)  
[ISldWorks::HideToolbar2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~HideToolbar2.md)  
[ISldWorks::RemoveToolbar2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RemoveToolbar2.md)  
[ISldWorks::SetToolbarDock2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetToolbarDock2.md)  
[ISldWorks::DragToolbarButtonFromCommandID Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~DragToolbarButtonFromCommandID.md)
