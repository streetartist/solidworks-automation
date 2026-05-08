# IsCommandEnabled Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IsCommandEnabled`

Gets whether the specified command is enabled.
Gets whether the specified command is enabled.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IsCommandEnabled( _
   ByVal CommandID As System.Integer _
) As System.Boolean
```

```

Dim instance As ISldWorks
Dim CommandID As System.Integer
Dim value As System.Boolean
 
value = instance.IsCommandEnabled(CommandID)
```

```

System.bool IsCommandEnabled( 
   System.int CommandID
)
```

```

System.bool IsCommandEnabled( 
   System.int CommandID
) 
```

#### Parameters

*CommandID*
:   Command ID as defined [swCommands\_e](SOLIDWORKS.Interop.swcommands.md) (see Remarks)

#### Return Value

True if the command is enabled, false if not

Remarks

Before using this method, you must add a reference to the version-specific SOLIDWORKS Commands type library to access the SOLIDWORKS commands.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)  
[ISldWorks::RunCommand Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RunCommand.md)
