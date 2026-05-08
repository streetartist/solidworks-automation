# swFileLoadError_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swFileLoadError_e`

File load errors. Bitmask.
File load errors. [Bitmask](sldworksapiprogguide.chm::/overview/bitmasks.htm).

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

<System.Runtime.InteropServices.GuidAttribute("2D3E40D1-90A0-4DCD-A0B7-7AEE4A0F9BE5")>
Public Enum swFileLoadError_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swFileLoadError_e
```

```

[System.Runtime.InteropServices.Guid("2D3E40D1-90A0-4DCD-A0B7-7AEE4A0F9BE5")]
public enum swFileLoadError_e : System.Enum 
```

```

public enum swFileLoadError_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("2D3E40D1-90A0-4DCD-A0B7-7AEE4A0F9BE5")
public enum swFileLoadError_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("2D3E40D1-90A0-4DCD-A0B7-7AEE4A0F9BE5")]
__value public enum swFileLoadError_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("2D3E40D1-90A0-4DCD-A0B7-7AEE4A0F9BE5")]
public enum class swFileLoadError_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swAddinInteruptError** | 1048576 or 0x100000: The user attempted to open a file, and then interrupted the open-file routine to open a different file |
| **swApplicationBusy** | 8388608 or 0x800000: File open is blocked when application is busy |
| **swBasePartNotLoadedWarn** | Obsolete; see [swFileLoadWarning\_e](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swFileLoadWarning_e.md) |
| **swConnectedIsOffline** | 16777216 or 0x1000000 |
| **swDrawingANSIUpdateWarn** | Obsolete; see [swFileLoadWarning\_e](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swFileLoadWarning_e.md) |
| **swDrawingSFSymbolConvertWarn** | Obsolete; see [swFileLoadWarning\_e](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swFileLoadWarning_e.md) |
| **swDrawingsOnlyRapidDraftWarn** | Obsolete; see [swFileLoadWarning\_e](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swFileLoadWarning_e.md) |
| **swFileAlreadyOpenWarn** | Obsolete; see [swFileLoadWarning\_e](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swFileLoadWarning_e.md) |
| **swFileCriticalDataRepairError** | 4194304 or 0x400000 = A document has critical data corruption |
| **swFileNotFoundError** | 2 or 0x2 = Unable to locate the file; the file is not loaded or the referenced file (that is, component) is suppressed |
| **swFileRequiresRepairError** | 2097152 or 0x200000 = A document has non-critical custom property data corruption |
| **swFileWithSameTitleAlreadyOpen** | 65536 or 0x10000 = A document with the same name is already open |
| **swFutureVersion** | 8192 or 0x2000 = The document was saved in a future version of SOLIDWORKS |
| **swGenericError** | 1 or 0x1 = Another error was encountered |
| **swIdMatchError** | Obsolete; see [swFileLoadWarning\_e](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swFileLoadWarning_e.md) |
| **swInvalidFileTypeError** | 1024 or 0x400 = File type argument is not valid |
| **swLiquidMachineDoc** | 131072 or 0x20000 = File encrypted by Liquid Machines |
| **swLowResourcesError** | 262144 or 0x40000 = File is open and blocked because the system memory is low, or the number of GDI handles has exceeded the allowed maximum |
| **swNeedsRegenWarn** | Obsolete; see [swFileLoadWarning\_e](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swFileLoadWarning_e.md) |
| **swNoDisplayData** | 524288 or 0x80000 = File contains no display data |
| **swReadOnlyWarn** | Obsolete; see [swFileLoadWarning\_e](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swFileLoadWarning_e.md) |
| **swSharingViolationWarn** | Obsolete; see [swFileLoadWarning\_e](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swFileLoadWarning_e.md) |
| **swSheetScaleUpdateWarn** | Obsolete; see [swFileLoadWarning\_e](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swFileLoadWarning_e.md) |
| **swViewMissingReferencedConfig** | Obsolete; see [swFileLoadWarning\_e](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swFileLoadWarning_e.md) |
| **swViewOnlyRestrictions** | Obsolete; see [swFileLoadWarning\_e](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swFileLoadWarning_e.md) |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swFileLoadError\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
