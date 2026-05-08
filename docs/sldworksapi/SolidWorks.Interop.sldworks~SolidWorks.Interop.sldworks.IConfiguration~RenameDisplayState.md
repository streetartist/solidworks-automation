# RenameDisplayState Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~RenameDisplayState`

Renames a display state of this configuration.
Renames a display state of this configuration.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function RenameDisplayState( _
   ByVal OldDisplayStateName As System.String, _
   ByVal NewDisplayStateName As System.String _
) As System.Boolean
```

```

Dim instance As IConfiguration
Dim OldDisplayStateName As System.String
Dim NewDisplayStateName As System.String
Dim value As System.Boolean
 
value = instance.RenameDisplayState(OldDisplayStateName, NewDisplayStateName)
```

```

System.bool RenameDisplayState( 
   System.string OldDisplayStateName,
   System.string NewDisplayStateName
)
```

```

System.bool RenameDisplayState( 
   System.String^ OldDisplayStateName,
   System.String^ NewDisplayStateName
) 
```

#### Parameters

*OldDisplayStateName*
:   Existing name of the display state

*NewDisplayStateName*
:   New name for the display state

#### Return Value

True if the display state is renamed, false if not

Remarks

Use [IConfiguration::GetDisplayStates](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetDisplayStates.md) or [IConfiguration::IGetDisplayStates](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~IGetDisplayStates.md) to get a list of the names of the existing display states for this configuration.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IConfiguration Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.md)  
[IConfiguration Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration_members.md)  
[IConfiguration::ApplyDisplayState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~ApplyDisplayState.md)  
[IConfiguration::DeleteDisplayState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~DeleteDisplayState.md)  
[IConfiguration::CreateDisplayState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~CreateDisplayState.md)  
[IConfiguration::CopyDisplayStateFromConfiguration Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~CopyDisplayStateFromConfiguration.md)
