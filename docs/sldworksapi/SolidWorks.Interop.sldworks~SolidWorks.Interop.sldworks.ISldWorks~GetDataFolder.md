# GetDataFolder Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetDataFolder`

Gets the data directory name currently used by SOLIDWORKS.
Gets the data directory name currently used by SOLIDWORKS.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetDataFolder( _
   ByVal BShowErrorMsg As System.Boolean _
) As System.String
```

```

Dim instance As ISldWorks
Dim BShowErrorMsg As System.Boolean
Dim value As System.String
 
value = instance.GetDataFolder(BShowErrorMsg)
```

```

System.string GetDataFolder( 
   System.bool BShowErrorMsg
)
```

```

System.String^ GetDataFolder( 
   System.bool BShowErrorMsg
) 
```

#### Parameters

*BShowErrorMsg*
:   True to show any error messages in a dialog or false to avoid these dialogs (that is, data directory could not be found messages)

#### Return Value

Data directory currently used by the SOLIDWORKS application

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)  
[ISldWorks::GetCurrentWorkingDirectory Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetCurrentWorkingDirectory.md)  
[ISldWorks::SetCurrentWorkingDirectory Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetCurrentWorkingDirectory.md)  
[ISldWorks::GetExecutablePath Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetExecutablePath.md)  
[ISldWorks::GetSearchFolders Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetSearchFolders.md)
