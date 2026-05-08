# RunCommand Method (IModelDocExtension)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~RunCommand`

Runs the specified SOLIDWORKS command.
Runs the specified SOLIDWORKS command.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function RunCommand( _
   ByVal CommandID As System.Integer, _
   ByVal NewTitle As System.String _
) As System.Boolean
```

```

Dim instance As IModelDocExtension
Dim CommandID As System.Integer
Dim NewTitle As System.String
Dim value As System.Boolean
 
value = instance.RunCommand(CommandID, NewTitle)
```

```

System.bool RunCommand( 
   System.int CommandID,
   System.string NewTitle
)
```

```

System.bool RunCommand( 
   System.int CommandID,
   System.String^ NewTitle
) 
```

#### Parameters

*CommandID*
:   SOLIDWORKS command as defined in [swCommands\_e](SOLIDWORKS.Interop.swcommands~SOLIDWORKS.Interop.swcommands.swCommands_e.md)

*NewTitle*
:   Your title for the SOLIDWORKS PropertyManager page, if invoked by this command

#### Return Value

True if the SOLIDWORKS command ran, false if not

Example

[Run SOLIDWORKS Commands (VBA)](Run_SOLIDWORKS_Commands_Example_VB.htm)  
[Fire Events When PropertyManager Page Opened and Canceled (C#)](Fire_Events_When_PropertyManager_Page_Opened_and_Canceled_Example_CSharp.htm)  
[Fire Events When PropertyManager Page Opened and Canceled (VB.NET)](Fire_Events_When_PropertyManager_Page_Opened_and_Canceled_Example_VBNET.htm)  
[Fire Events When PropertyManager Page Opened and Canceled (VBA)](Fire_Events_When_PropertyManager_Page_Opened_and_Canceled_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[ISldWorks::RunCommand Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RunCommand.md)  
[ISldWorks::IsCommandEnabled Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IsCommandEnabled.md)
