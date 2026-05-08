# swSaveWithReferencesOptions_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSaveWithReferencesOptions_e`

Options for saving references while getting the IAdvancedSaveAsOptions object; used by the Options parameter of IModelDocExtension::GetAdvancedSaveAsOptions. Bitmask.
Options for saving references while getting the [IAdvancedSaveAsOptions](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSaveAsOptions.html) object; used by the Options parameter of [IModelDocExtension::GetAdvancedSaveAsOptions](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetAdvancedSaveAsOptions.html). [Bitmask](sldworksapiprogguide.chm::/overview/bitmasks.htm).

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

<System.Runtime.InteropServices.GuidAttribute("890F4E56-EAD8-41A2-8A8E-94604E9784DA")>
Public Enum swSaveWithReferencesOptions_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swSaveWithReferencesOptions_e
```

```

[System.Runtime.InteropServices.Guid("890F4E56-EAD8-41A2-8A8E-94604E9784DA")]
public enum swSaveWithReferencesOptions_e : System.Enum 
```

```

public enum swSaveWithReferencesOptions_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("890F4E56-EAD8-41A2-8A8E-94604E9784DA")
public enum swSaveWithReferencesOptions_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("890F4E56-EAD8-41A2-8A8E-94604E9784DA")]
__value public enum swSaveWithReferencesOptions_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("890F4E56-EAD8-41A2-8A8E-94604E9784DA")]
public enum class swSaveWithReferencesOptions_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swSaveWithReferencesOptions\_IncludeBrokenReferences** | 4 = Reference list contains both normal references and components with broken references |
| **swSaveWithReferencesOptions\_IncludeToolBoxParts** | 2 = Reference list contains both normal and ToolBox references |
| **swSaveWithReferencesOptions\_IncludeVirtualComponents** | 1 = Reference list contains both normal and virtual component references |
| **swSaveWithReferencesOptions\_None** | 0 = Reference list contains only normal references |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swSaveWithReferencesOptions\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
