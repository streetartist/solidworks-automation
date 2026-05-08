# swDimensionTextParts_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swDimensionTextParts_e`

Options for getting and setting display dimension text.
Options for getting and setting display dimension text.

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

<System.Runtime.InteropServices.GuidAttribute("44B8E5FE-D1F6-4072-9758-98E1EECE6095")>
Public Enum swDimensionTextParts_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swDimensionTextParts_e
```

```

[System.Runtime.InteropServices.Guid("44B8E5FE-D1F6-4072-9758-98E1EECE6095")]
public enum swDimensionTextParts_e : System.Enum 
```

```

public enum swDimensionTextParts_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("44B8E5FE-D1F6-4072-9758-98E1EECE6095")
public enum swDimensionTextParts_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("44B8E5FE-D1F6-4072-9758-98E1EECE6095")]
__value public enum swDimensionTextParts_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("44B8E5FE-D1F6-4072-9758-98E1EECE6095")]
public enum class swDimensionTextParts_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swDimensionTextAll** | 0 = Entire dimension text string ([IDisplayDimension::SetText](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayDimension~SetText.html) only) |
| **swDimensionTextCalloutAbove** | 3 = Callout-above portion of the text |
| **swDimensionTextCalloutAboveDefinition** | 7 = Definition of the callout portion of the text above the dimension |
| **swDimensionTextCalloutBelow** | 4 = Callout-below portion of the text |
| **swDimensionTextCalloutBelowDefinition** | 8 = Definition of the callout portion of the text below the dimension |
| **swDimensionTextPrefix** | 1 = Prefix portion of the text |
| **swDimensionTextPrefixDefinition** | 5 = Definition of the prefix portion of the text |
| **swDimensionTextSuffix** | 2 = Suffix portion of the text |
| **swDimensionTextSuffixDefinition** | 6 = Definition of the suffix portion of the text |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swDimensionTextParts\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
