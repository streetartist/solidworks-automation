# ToolbarId Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~ToolbarId`

Gets the toolbar ID of this CommandGroup.
Gets the toolbar ID of this CommandGroup.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property ToolbarId As System.Integer
```

```

Dim instance As ICommandGroup
Dim value As System.Integer
 
value = instance.ToolbarId
```

```

System.int ToolbarId {get;}
```

```

property System.int ToolbarId {
   System.int get();
}
```

#### Property Value

Toolbar ID of this CommandGroup

Remarks

Use this property when [dragging a toolbar button](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~DragToolbarButton.md) from one toolbar (native SOLIDWORKS or a CommandGroup toolbar) to another toolbar (native SOLIDWORKS or a CommandGroup toolbar).

Example

[Create Flyouts in the CommandManager (VB.NET)](Create_Flyouts_in_the_CommandManager_Example_VBNET.htm)  
[Create Flyouts in the CommandManager (C#)](Create_Flyouts_in_the_CommandManager_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICommandGroup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup.md)  
[ICommandGroup Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup_members.md)  
[ICommandManager::HasToolbar Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~HasToolbar.md)
