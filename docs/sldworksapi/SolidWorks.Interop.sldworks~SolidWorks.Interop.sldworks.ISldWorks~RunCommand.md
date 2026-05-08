# RunCommand Method (ISldWorks)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RunCommand`

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

Dim instance As ISldWorks
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
:   SOLIDWORKS command as defined in [swCommands\_e](SOLIDWORKS.Interop.swcommands.md) (see Remarks)

*NewTitle*
:   Your title for the SOLIDWORKS PropertyManager page, if invoked by this command

#### Return Value

True if the SOLIDWORKS command ran, false if not

Example

[Fire Events When PropertyManager Page Opened and Canceled (VBA)](Fire_Events_When_PropertyManager_Page_Opened_and_Canceled_Example_VB.htm)  
[Record Macros (C#)](Record_Macros_Example_CSharp.htm)  
[Record Macros (VB.NET)](Record_Macros_Example_VBNET.htm)  
[Record Macros (VBA)](Record_Macros_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)  
[IModelDocExtension::RunCommand Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~RunCommand.md)  
[ISldWorks::IsCommandEnabled Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IsCommandEnabled.md)  
[ISldWorks::GetRunningCommandInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetRunningCommandInfo.md)  
[DSldWorksEvents\_CommandCloseNotifyEventHandler Delegate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_CommandCloseNotifyEventHandler.md)  
[DSldWorksEvents\_CommandOpenPreNotifyEventHandler Delegate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_CommandOpenPreNotifyEventHandler.md)  
[ISldWorks::RecordLine Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RecordLine.md)  
[ISldWorks::RecordLineCSharp Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RecordLineCSharp.md)  
[ISldWorks::RecordLineVBnet Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RecordLineVBnet.md)
