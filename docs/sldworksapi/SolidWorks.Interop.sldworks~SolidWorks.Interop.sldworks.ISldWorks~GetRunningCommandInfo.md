# GetRunningCommandInfo Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetRunningCommandInfo`

Get a command's ID or PropertyManager page's command ID, title, and whether it is active in the user-interface.
Get a command's ID or PropertyManager page's command ID, title, and whether it is active in the user-interface.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub GetRunningCommandInfo( _
   ByRef CommandID As System.Integer, _
   ByRef PMTitle As System.String, _
   ByRef IsUiActive As System.Boolean _
) 
```

```

Dim instance As ISldWorks
Dim CommandID As System.Integer
Dim PMTitle As System.String
Dim IsUiActive As System.Boolean
 
instance.GetRunningCommandInfo(CommandID, PMTitle, IsUiActive)
```

```

void GetRunningCommandInfo( 
   out System.int CommandID,
   out System.string PMTitle,
   out System.bool IsUiActive
)
```

```

void GetRunningCommandInfo( 
   [Out] System.int CommandID,
   [Out] System.String^ PMTitle,
   [Out] System.bool IsUiActive
) 
```

#### Parameters

*CommandID*
:   Command's ID or PropertyManager page's command ID as defined in [swCommands\_e](SOLIDWORKS.Interop.swcommands~SOLIDWORKS.Interop.swcommands.swCommands_e.md)

*PMTitle*
:   Title of PropertyManager page

*IsUiActive*
:   True if command or PropertyManager page is active in the user-interface, false if not

Remarks

Before using this method, you must add a reference to the SOLIDWORKS commands type library or DLL to access the SOLIDWORKS commands.

Example

[Fire Events When PropertyManager Page Opened and Canceled (VBA)](Fire_Events_When_PropertyManager_Page_Opened_and_Canceled_Example_VB.htm)  
[Fire Events When PropertyManager Page Opened and Canceled (VB.NET)](Fire_Events_When_PropertyManager_Page_Opened_and_Canceled_Example_VBNET.htm)  
[Fire Events When PropertyManager Page Opened and Canceled (C#)](Fire_Events_When_PropertyManager_Page_Opened_and_Canceled_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)  
[ISldWorks::RunCommand Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RunCommand.md)  
[ISldWorks::IsCommandEnabled Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IsCommandEnabled.md)  
[DSldWorksEvents\_CommandOpenPreNotifyEventHandler Delegate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_CommandOpenPreNotifyEventHandler.md)  
[DSldWorksEvents\_CommandCloseNotifyEventHandler Delegate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_CommandCloseNotifyEventHandler.md)
