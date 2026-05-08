# swCheckInterferenceOption_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCheckInterferenceOption_e`

Check interference options. Bitmask.
Check interference options. [Bitmask](sldworksapiprogguide.chm::/overview/bitmasks.htm).

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

<System.Runtime.InteropServices.GuidAttribute("ACBE3DA8-0239-41F8-8E38-683702876729")>
Public Enum swCheckInterferenceOption_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swCheckInterferenceOption_e
```

```

[System.Runtime.InteropServices.Guid("ACBE3DA8-0239-41F8-8E38-683702876729")]
public enum swCheckInterferenceOption_e : System.Enum 
```

```

public enum swCheckInterferenceOption_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("ACBE3DA8-0239-41F8-8E38-683702876729")
public enum swCheckInterferenceOption_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("ACBE3DA8-0239-41F8-8E38-683702876729")]
__value public enum swCheckInterferenceOption_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("ACBE3DA8-0239-41F8-8E38-683702876729")]
public enum class swCheckInterferenceOption_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swBodyInterference\_IncludeCoincidentFaces** | 2 or 0x2; Abutment (i.e., faces touching each other) type of clash |
| **swBodyInterference\_OptionDefault** | 1 or 0x1; If this option specified, then swBodyInterference\_IncludeCoincidentFaces and swBodyInterference\_ReturnInterferingObject are set to false |
| **swBodyInterference\_ReturnInterferingObject** | 4 or 0x4; Return face and body arrays |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swCheckInterferenceOption\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
