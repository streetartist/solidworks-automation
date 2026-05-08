# swFileSaveWarning_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swFileSaveWarning_e`

Values for File, Save warnings that can be returned from the IModelDoc2 Save methods. These warnings do not cause the File, Save operation to fail. Bitmask.
Values for File, Save warnings that can be returned from the [IModelDoc2](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2.html) Save methods. These warnings do not cause the File, Save operation to fail. [Bitmask](sldworksapiprogguide.chm::/overview/bitmasks.htm).

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

<System.Runtime.InteropServices.GuidAttribute("151C8B13-209B-4677-8309-89E3EB5FE5CD")>
Public Enum swFileSaveWarning_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swFileSaveWarning_e
```

```

[System.Runtime.InteropServices.Guid("151C8B13-209B-4677-8309-89E3EB5FE5CD")]
public enum swFileSaveWarning_e : System.Enum 
```

```

public enum swFileSaveWarning_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("151C8B13-209B-4677-8309-89E3EB5FE5CD")
public enum swFileSaveWarning_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("151C8B13-209B-4677-8309-89E3EB5FE5CD")]
__value public enum swFileSaveWarning_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("151C8B13-209B-4677-8309-89E3EB5FE5CD")]
public enum class swFileSaveWarning_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swFileSaveWarning\_AnimatorCameraViews** | 128 or 0x80 |
| **swFileSaveWarning\_AnimatorFeatureEdits** | 16 or 0x10 |
| **swFileSaveWarning\_AnimatorLightEdits** | 64 or 0x40 |
| **swFileSaveWarning\_AnimatorNeedToSolve** | 8 or 0x8 |
| **swFileSaveWarning\_AnimatorSectionViews** | 256 or 0x100 |
| **swFileSaveWarning\_EdrwingsBadSelection** | 32 or 0x20 |
| **swFileSaveWarning\_MissingOLEObjects** | 512 or 0x200 |
| **swFileSaveWarning\_NeedsRebuild** | 2 or 0x2 |
| **swFileSaveWarning\_OpenedViewOnly** | 1024 or 0x400 |
| **swFileSaveWarning\_RebuildError** | 1 or 0x1 |
| **swFileSaveWarning\_ViewsNeedUpdate** | 4 or 0x4 |
| **swFileSaveWarning\_XmlInvalid** | 2048 or 0x800 |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swFileSaveWarning\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
