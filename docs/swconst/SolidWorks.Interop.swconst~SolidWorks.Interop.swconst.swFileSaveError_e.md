# swFileSaveError_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swFileSaveError_e`

File save errors. Bitmask.
File save errors. [Bitmask](sldworksapiprogguide.chm::/overview/bitmasks.htm).

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

<System.Runtime.InteropServices.GuidAttribute("DF330771-B47D-4397-ACC7-79FDE1321B4D")>
Public Enum swFileSaveError_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swFileSaveError_e
```

```

[System.Runtime.InteropServices.Guid("DF330771-B47D-4397-ACC7-79FDE1321B4D")]
public enum swFileSaveError_e : System.Enum 
```

```

public enum swFileSaveError_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("DF330771-B47D-4397-ACC7-79FDE1321B4D")
public enum swFileSaveError_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("DF330771-B47D-4397-ACC7-79FDE1321B4D")]
__value public enum swFileSaveError_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("DF330771-B47D-4397-ACC7-79FDE1321B4D")]
public enum class swFileSaveError_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swFileLockError** | 16 or 0x10 |
| **swFileNameContainsAtSign** | 8 or 0x8 = File name cannot contain the at symbol (@) |
| **swFileNameEmpty** | 4 or 0x4 = File name cannot be empty |
| **swFileSaveAsBadEDrawingsVersion** | 1024 or 0x400 |
| **swFileSaveAsDetachedDrawingsNotSupported** | 16384 or 0x4000 = Detached drawing save as options is not supported |
| **swFileSaveAsDoNotOverwrite** | 128 or 0x80 = Do not overwrite an existing file |
| **swFileSaveAsInvalidFileExtension** | 256 or 0x100 = File name extension does not match the SOLIDWORKS document type |
| **swFileSaveAsNameExceedsMaxPathLength** | 2048 or 0x800 = File name cannot exceed 255 characters |
| **swFileSaveAsNoSelection** | 512 or 0x200 = Save the selected bodies in a part document. Valid option for [IPartDoc::SaveToFile2](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPartDoc~SaveToFile2.html); however, not a valid option for [IModelDocExtension::SaveAs](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~SaveAs.html) |
| **swFileSaveAsNotSupported** | 4096 or 0x1000 = Save As operation:   - is not supported - was executed is such a way that the resulting file might not be complete, possibly because SOLIDWORKS is hidden; if the error persists after [setting SOLIDWORKS to visible](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~Visible.html) and re-attempting the Save As operation, contact [SOLIDWORKS API support](mailto:apisupport@3ds.com). |
| **swFileSaveFormatNotAvailable** | 32 or 0x20 = Save As file type is not valid |
| **swFileSaveRequiresSavingReferences** | 8192 or 0x2000 = Saving an assembly with renamed components requires saving the references |
| **swFileSaveWithRebuildError** | Obsolete = See [swFileSaveWarning\_e](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swFileSaveWarning_e.md) |
| **swGenericSaveError** | 1 or 0x1 |
| **swReadOnlySaveError** | 2 or 0x2 |

Remarks

Not all of these return codes are fatal errors. The return code is a bitmask of different conditions that can occur during the operation, some of which are fatal and some are informational or warnings.

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swFileSaveError\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
