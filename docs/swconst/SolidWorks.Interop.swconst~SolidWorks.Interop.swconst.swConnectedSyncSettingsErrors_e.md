# swConnectedSyncSettingsErrors_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swConnectedSyncSettingsErrors_e`

Return codes for ISldWorks::UploadToMySolidWorksSettings and ISldWorks::DownloadFromMySolidWorksSettings.
Return codes for [ISldWorks::UploadToMySolidWorksSettings](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~UploadToMySolidWorksSettings.html) and [ISldWorks::DownloadFromMySolidWorksSettings](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~DownloadFromMySolidWorksSettings.html).

Syntax

- [Visual Basic](#Syntax-VBAll)
- [C#](#Syntax-CS)
- [Delphi](#Syntax-Delphi)
- [JScript](#Syntax-JScript)
- [Managed Extensions for C++](#Syntax-CPP)
- [C++/CLI](#Syntax-CPP2005)

```

'Declaration
 
```

```

<System.Runtime.InteropServices.GuidAttribute("94709A7E-5093-424C-9DEC-DB6236EC09DB")>
Public Enum swConnectedSyncSettingsErrors_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swConnectedSyncSettingsErrors_e
```

```

[System.Runtime.InteropServices.Guid("94709A7E-5093-424C-9DEC-DB6236EC09DB")]
public enum swConnectedSyncSettingsErrors_e : System.Enum 
```

```

public enum swConnectedSyncSettingsErrors_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("94709A7E-5093-424C-9DEC-DB6236EC09DB")
public enum swConnectedSyncSettingsErrors_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("94709A7E-5093-424C-9DEC-DB6236EC09DB")]
__value public enum swConnectedSyncSettingsErrors_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("94709A7E-5093-424C-9DEC-DB6236EC09DB")]
public enum class swConnectedSyncSettingsErrors_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swConnectedSyncSettings\_ConnectedDisabled** | 1 |
| **swConnectedSyncSettings\_ConnectedNotLoggedIn** | 2 |
| **swConnectedSyncSettings\_Success** | 0 |
| **swConnectedSyncSettings\_UploadDownloadError** | 3 |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swConnectedSyncSettingsErrors\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
