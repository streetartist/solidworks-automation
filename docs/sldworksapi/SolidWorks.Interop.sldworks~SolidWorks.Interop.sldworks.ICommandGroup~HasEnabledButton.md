# HasEnabledButton Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~HasEnabledButton`

Gets whether any buttons in this CommandGroup are enabled.
Gets whether any buttons in this CommandGroup are enabled.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property HasEnabledButton As System.Boolean
```

```

Dim instance As ICommandGroup
Dim value As System.Boolean
 
value = instance.HasEnabledButton
```

```

System.bool HasEnabledButton {get;}
```

```

property System.bool HasEnabledButton {
   System.bool get();
}
```

#### Property Value

True if at least one CommandGroup button is enabled, false if not

Remarks

Add-in applications can call this method to determine whether to disable flyout buttons in the CommandManager.

Example

[Create Flyouts in the CommandManager (C#)](Create_Flyouts_in_the_CommandManager_Example_CSharp.htm)  
[Create Flyouts in the CommandManager (VB.NET)](Create_Flyouts_in_the_CommandManager_Example_VBNET.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICommandGroup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup.md)  
[ICommandGroup Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup_members.md)  
[ICommandGroup::AddCommandItem2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~AddCommandItem2.md)
