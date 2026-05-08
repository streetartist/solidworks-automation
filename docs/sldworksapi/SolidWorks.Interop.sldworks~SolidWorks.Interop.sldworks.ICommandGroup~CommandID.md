# CommandID Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~CommandID`

Gets the command ID for the specified item in the CommandGroup.
Gets the command ID for the specified item in the CommandGroup.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property CommandID( _
   ByVal CommandIndex As System.Integer _
) As System.Integer
```

```

Dim instance As ICommandGroup
Dim CommandIndex As System.Integer
Dim value As System.Integer
 
value = instance.CommandID(CommandIndex)
```

```

System.int CommandID( 
   System.int CommandIndex
) {get;}
```

```

property System.int CommandID {
   System.int get(System.int CommandIndex);
}
```

#### Parameters

*CommandIndex*
:   Index of the item in the CommandGroup

#### Property Value

Command ID of the specified item

Remarks

The value of CommandIndex is the value returned by [ICommandGroup::AddCommandItem2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~AddCommandItem2.md).

Example

[Create Flyouts in the CommandManager (C#)](Create_Flyouts_in_the_CommandManager_Example_CSharp.htm)  
[Create Flyouts in the CommandManager (VB.NET)](Create_Flyouts_in_the_CommandManager_Example_VBNET.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICommandGroup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup.md)  
[ICommandGroup Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup_members.md)  
[ISldWorks::GetCommandID Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetCommandID.md)  
[ICommandGroup::NumberOfGroupItems Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~NumberOfGroupItems.md)
