# CommandTabBoxes Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandTab~CommandTabBoxes`

Gets the tab boxes on this CommandManager tab.
Gets the tab boxes on this CommandManager tab.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CommandTabBoxes() As System.Object
```

```

Dim instance As ICommandTab
Dim value As System.Object
 
value = instance.CommandTabBoxes()
```

```

System.object CommandTabBoxes()
```

```

System.Object^ CommandTabBoxes(); 
```

#### Return Value

Array of [CommandManager tab boxes](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandTabBox.md) on this CommandManager tab

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICommandTab Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandTab.md)  
[ICommandTab Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandTab_members.md)  
[ICommandTab::GetCommandTabBoxCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandTab~GetCommandTabBoxCount.md)  
[ICommandTab::IGetCommandTabBoxes Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandTab~IGetCommandTabBoxes.md)  
[ICommandTab::RemoveCommandTabBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandTab~RemoveCommandTabBox.md)
