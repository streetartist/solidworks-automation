# DockingState Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~DockingState`

Gets or sets the docking state of the toolbar in the CommandGroup.
Gets or sets the docking state of the toolbar in the CommandGroup.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property DockingState As System.Integer
```

```

Dim instance As ICommandGroup
Dim value As System.Integer
 
instance.DockingState = value
 
value = instance.DockingState
```

```

System.int DockingState {get; set;}
```

```

property System.int DockingState {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Docking state of the toolbar as defined in [swToolbarDockStatePosition\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swToolbarDockStatePosition_e.html)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICommandGroup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup.md)  
[ICommandGroup Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup_members.md)  
[ICommandGroup::SetToolbarVisibility Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~SetToolbarVisibility.md)  
[ICommandGroup::HasToolbar Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~HasToolbar.md)  
[ICommandGroup::ToolbarId Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~ToolbarId.md)
