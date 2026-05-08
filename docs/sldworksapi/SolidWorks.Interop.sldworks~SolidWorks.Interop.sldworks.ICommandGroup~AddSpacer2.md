# AddSpacer2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~AddSpacer2`

Adds a spacer between items in a CommandGroup.
Adds a spacer between items in a CommandGroup.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AddSpacer2( _
   ByVal Position As System.Integer, _
   ByVal MenuTBOption As System.Integer _
) As System.Integer
```

```

Dim instance As ICommandGroup
Dim Position As System.Integer
Dim MenuTBOption As System.Integer
Dim value As System.Integer
 
value = instance.AddSpacer2(Position, MenuTBOption)
```

```

System.int AddSpacer2( 
   System.int Position,
   System.int MenuTBOption
)
```

```

System.int AddSpacer2( 
   System.int Position,
   System.int MenuTBOption
) 
```

#### Parameters

*Position*
:   Position of the spacer within the CommandGroup

    NOTE: Specify 0 to add this a spacer to the beginning of the CommandGroup, or specify -1 to add it to the end of the CommandGroup. This argument specifies the position of the spacer in relation to its immediate parent item.

*MenuTBOption*
:   Command item type as defined in [swCommandItemType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCommandItemType_e.html)

#### Return Value

Index of the item within the CommandGroup as assigned by SOLIDWORKS

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICommandGroup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup.md)  
[ICommandGroup Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup_members.md)
