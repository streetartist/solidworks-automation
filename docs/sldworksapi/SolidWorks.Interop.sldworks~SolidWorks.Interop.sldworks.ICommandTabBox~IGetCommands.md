# IGetCommands Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandTabBox~IGetCommands`

Gets the buttons' Command IDs, text display styles, and number of commands on the CommandManager tab box.
Gets the buttons' Command IDs, text display styles, and number of commands on the CommandManager tab box.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetCommands( _
   ByRef CommandIDs As System.Integer, _
   ByRef TextDisplayStyles As System.Integer _
) As System.Integer
```

```

Dim instance As ICommandTabBox
Dim CommandIDs As System.Integer
Dim TextDisplayStyles As System.Integer
Dim value As System.Integer
 
value = instance.IGetCommands(CommandIDs, TextDisplayStyles)
```

```

System.int IGetCommands( 
   out System.int CommandIDs,
   out System.int TextDisplayStyles
)
```

```

System.int IGetCommands( 
   [Out] System.int CommandIDs,
   [Out] System.int TextDisplayStyles
) 
```

#### Parameters

*CommandIDs*
:   - in-process, unmanaged C++: Pointer to an array of command IDs (see **Remarks**)
    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

*TextDisplayStyles*
:   - in-process, unmanaged C++: Pointer to an array the text display styles for the buttons as defined in [swCommandTabButtonTextDisplay\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCommandTabButtonTextDisplay_e.html)

    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method

#### Return Value

Number of buttons on this CommandManager tab box

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICommandTabBox Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandTabBox.md)  
[ICommandTabBox Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandTabBox_members.md)  
[ICommandTabBox::GetCommands Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandTabBox~GetCommands.md)
