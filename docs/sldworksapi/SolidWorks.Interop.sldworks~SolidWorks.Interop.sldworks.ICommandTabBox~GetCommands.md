# GetCommands Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandTabBox~GetCommands`

Gets the buttons' command IDs, text display styles, and number of commands on the CommandManager tab box.
Gets the buttons' command IDs, text display styles, and number of commands on the CommandManager tab box.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetCommands( _
   ByRef CommandIDs As System.Object, _
   ByRef TextDisplayStyles As System.Object _
) As System.Integer
```

```

Dim instance As ICommandTabBox
Dim CommandIDs As System.Object
Dim TextDisplayStyles As System.Object
Dim value As System.Integer
 
value = instance.GetCommands(CommandIDs, TextDisplayStyles)
```

```

System.int GetCommands( 
   out System.object CommandIDs,
   out System.object TextDisplayStyles
)
```

```

System.int GetCommands( 
   [Out] System.Object^ CommandIDs,
   [Out] System.Object^ TextDisplayStyles
) 
```

#### Parameters

*CommandIDs*
:   Array of command IDs for the buttons

*TextDisplayStyles*
:   Array of the text display styles for the buttons as defined in [swCommandTabButtonTextDisplay\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCommandTabButtonTextDisplay_e.html)

#### Return Value

Number of buttons on this CommandManager tab box

Example

[Create CommandManager Tab and Tab Boxes (C#)](Create_CommandManager_Tab_and_Tab_Boxes_Example_CSharp.htm)  
[Create CommandManager Tab and Tab Boxes (VB.NET)](Create_CommandManager_Tab_and_Tab_Boxes_Example_VB.NET.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICommandTabBox Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandTabBox.md)  
[ICommandTabBox Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandTabBox_members.md)  
[ICommandTabBox::IGetCommands Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandTabBox~IGetCommands.md)
