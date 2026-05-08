# RemoveCommandTabBox Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandTab~RemoveCommandTabBox`

Removes the specified tab box and its buttons from this CommandManager tab.
Removes the specified tab box and its buttons from this CommandManager tab.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub RemoveCommandTabBox( _
   ByVal CommandTabBox As CommandTabBox _
) 
```

```

Dim instance As ICommandTab
Dim CommandTabBox As CommandTabBox
 
instance.RemoveCommandTabBox(CommandTabBox)
```

```

void RemoveCommandTabBox( 
   CommandTabBox CommandTabBox
)
```

```

void RemoveCommandTabBox( 
   CommandTabBox^ CommandTabBox
) 
```

#### Parameters

*CommandTabBox*
:   [CommandManager tab box](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandTabBox.md) and its buttons to remove

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICommandTab Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandTab.md)  
[ICommandTab Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandTab_members.md)  
[ICommandTab::AddCommandTabBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandTab~AddCommandTabBox.md)  
[ICommandTab::CommandTabBoxes Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandTab~CommandTabBoxes.md)  
[ICommandTab::GetCommandTabBoxCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandTab~GetCommandTabBoxCount.md)  
[ICommandTab::IGetCommandTabBoxes Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandTab~IGetCommandTabBoxes.md)
