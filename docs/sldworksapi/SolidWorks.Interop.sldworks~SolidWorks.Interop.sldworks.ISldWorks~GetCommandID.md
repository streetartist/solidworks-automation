# GetCommandID Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetCommandID`

Gets the SOLIDWORKS command ID for an instance of an add-in's control (e.g., an add-in's toolbar button).
Gets the SOLIDWORKS command ID for an instance of an add-in's control (e.g., an add-in's toolbar button).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetCommandID( _
   ByVal Clsid As System.String, _
   ByVal UserCmdID As System.Integer _
) As System.Integer
```

```

Dim instance As ISldWorks
Dim Clsid As System.String
Dim UserCmdID As System.Integer
Dim value As System.Integer
 
value = instance.GetCommandID(Clsid, UserCmdID)
```

```

System.int GetCommandID( 
   System.string Clsid,
   System.int UserCmdID
)
```

```

System.int GetCommandID( 
   System.String^ Clsid,
   System.int UserCmdID
) 
```

#### Parameters

*Clsid*
:   Add-in's class ID

*UserCmdID*
:   User-defined command ID for the add-in's control (see **Remarks**)

#### Return Value

Actual runtime value that SOLIDWORKS assigned the add-in's control

Remarks

UserCmdId is the same user-defined command ID specified when you created the add-in control using [ICommandGroup::AddCommandItem2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~AddCommandItem2.md). You need the SOLIDWORKS command ID if you want to do something like cause an add-in's toolbar button to flash when visible in SOLIDWORKS.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)  
[ICommandGroup::CommandID Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~CommandID.md)
