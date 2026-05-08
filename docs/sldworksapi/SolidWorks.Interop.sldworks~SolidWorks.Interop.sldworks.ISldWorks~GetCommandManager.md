# GetCommandManager Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetCommandManager`

Gets the CommandManager for the specified add-in.
Gets the CommandManager for the specified add-in.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetCommandManager( _
   ByVal Cookie As System.Integer _
) As CommandManager
```

```

Dim instance As ISldWorks
Dim Cookie As System.Integer
Dim value As CommandManager
 
value = instance.GetCommandManager(Cookie)
```

```

CommandManager GetCommandManager( 
   System.int Cookie
)
```

```

CommandManager^ GetCommandManager( 
   System.int Cookie
) 
```

#### Parameters

*Cookie*
:   Cookie specified in [ISwAddin::ConnectToSW](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.ISwAddin~ConnectToSW.md)

#### Return Value

[CommandManager](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager.md)

Remarks

See [CommandManager and CommandGroups](sldworksAPIProgGuide.chm::/OVERVIEW/CommandManager_and_CommandGroups.htm) for details.

Example

[Create Submenus in the CommandManager (C#)](Create_Submenus_in_the_CommandManager_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)
