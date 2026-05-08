# swGetOpenFileNameOptions_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swGetOpenFileNameOptions_e`

Options for opening a file returned by ISldWorks::GetOpenFileName2. Bitmask.
Options for opening a file returned by [ISldWorks::GetOpenFileName2](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetOpenFileName2.html). [Bitmask](sldworksapiprogguide.chm::/overview/bitmasks.htm).

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

<System.Runtime.InteropServices.GuidAttribute("6F9085A4-C8D4-4B27-80A1-16A76C49D23A")>
Public Enum swGetOpenFileNameOptions_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swGetOpenFileNameOptions_e
```

```

[System.Runtime.InteropServices.Guid("6F9085A4-C8D4-4B27-80A1-16A76C49D23A")]
public enum swGetOpenFileNameOptions_e : System.Enum 
```

```

public enum swGetOpenFileNameOptions_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("6F9085A4-C8D4-4B27-80A1-16A76C49D23A")
public enum swGetOpenFileNameOptions_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("6F9085A4-C8D4-4B27-80A1-16A76C49D23A")]
__value public enum swGetOpenFileNameOptions_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("6F9085A4-C8D4-4B27-80A1-16A76C49D23A")]
public enum class swGetOpenFileNameOptions_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swGetOpenFileNameOptions\_AdvancedConfig** | 0x2000; "<Advanced>" selected in configuration dropdown |
| **swGetOpenFileNameOptions\_AutoMissingConfig** | 0x20; Reserved for internal use |
| **swGetOpenFileNameOptions\_DontLoadHiddenComponents** | 0x100; Does not load hidden components (assemblies only) |
| **swGetOpenFileNameOptions\_LDR\_EditAssembly** | 0x800; Reserved for internal use |
| **swGetOpenFileNameOptions\_LoadExternalReferencesInMemory** | 0x200; Reserved for internal use |
| **swGetOpenFileNameOptions\_LoadLightweight** | 0x80; Opens the document in lightweight mode |
| **swGetOpenFileNameOptions\_LoadModel** | 0x10; Reserved for internal use |
| **swGetOpenFileNameOptions\_OpenDetailingMode** | 0x400; Opens the document in detailing mode without part and assembly data (drawings only) |
| **swGetOpenFileNameOptions\_OverrideDefaultLoadLightweight** | 0x40; Reserved for internal use |
| **swGetOpenFileNameOptions\_RapidDraft** | 0x8; Reserved for internal use |
| **swGetOpenFileNameOptions\_ReadOnly** | 0x2; Opens the document read only |
| **swGetOpenFileNameOptions\_SelectedSheets** | 0x8000; "Selected" is checked in Select Sheet to load dialog |
| **swGetOpenFileNameOptions\_Silent** | 0x1; Reserved for internal use |
| **swGetOpenFileNameOptions\_SpeedPak** | 0x1000; Uses Speedpak (assemblies only) |
| **swGetOpenFileNameOptions\_UseLargeAssemblySettings** | 0x4000; Uses large assembly settings (assemblies only) |
| **swGetOpenFileNameOptions\_ViewOnly** | 0x4; Opens the document view only; returned if "None" is selected in Select Sheet to load dialog |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swGetOpenFileNameOptions\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
