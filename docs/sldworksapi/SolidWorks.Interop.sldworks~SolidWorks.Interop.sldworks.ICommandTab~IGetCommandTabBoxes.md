# IGetCommandTabBoxes Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandTab~IGetCommandTabBoxes`

Gets the CommandManager tab boxes on this CommandManager tab.
Gets the CommandManager tab boxes on this CommandManager tab.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetCommandTabBoxes( _
   ByVal TabBoxCount As System.Integer _
) As CommandTabBox
```

```

Dim instance As ICommandTab
Dim TabBoxCount As System.Integer
Dim value As CommandTabBox
 
value = instance.IGetCommandTabBoxes(TabBoxCount)
```

```

CommandTabBox IGetCommandTabBoxes( 
   System.int TabBoxCount
)
```

```

CommandTabBox^ IGetCommandTabBoxes( 
   System.int TabBoxCount
) 
```

#### Parameters

*TabBoxCount*
:   Number of CommandManager tab boxes on this CommandManager tab

#### Return Value

- in-process, unmanaged C++: Pointer to an array of [CommandManager tab boxes](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandTabBox.md) on this CommandManager tab

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

Call [ICommandTab::GetCommandTabBoxCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandTab~GetCommandTabBoxCount.md) before calling this method to get the value of TabBoxCount.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICommandTab Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandTab.md)  
[ICommandTab Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandTab_members.md)  
[ICommandTab::AddCommandTabBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandTab~AddCommandTabBox.md)  
[ICommandTab::CommandTabBoxes Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandTab~CommandTabBoxes.md)  
[ICommandTab::RemoveCommandTabBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandTab~RemoveCommandTabBox.md)
