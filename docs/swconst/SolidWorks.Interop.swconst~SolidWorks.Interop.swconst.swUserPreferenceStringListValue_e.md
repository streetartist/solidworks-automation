# swUserPreferenceStringListValue_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swUserPreferenceStringListValue_e`

User-preference enumerators for system options and document properties.
User-preference enumerators for system options and document properties.

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

<System.Runtime.InteropServices.GuidAttribute("136EB330-9CE8-4FDC-9ED0-B691CCCA02E6")>
Public Enum swUserPreferenceStringListValue_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swUserPreferenceStringListValue_e
```

```

[System.Runtime.InteropServices.Guid("136EB330-9CE8-4FDC-9ED0-B691CCCA02E6")]
public enum swUserPreferenceStringListValue_e : System.Enum 
```

```

public enum swUserPreferenceStringListValue_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("136EB330-9CE8-4FDC-9ED0-B691CCCA02E6")
public enum swUserPreferenceStringListValue_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("136EB330-9CE8-4FDC-9ED0-B691CCCA02E6")]
__value public enum swUserPreferenceStringListValue_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("136EB330-9CE8-4FDC-9ED0-B691CCCA02E6")]
public enum class swUserPreferenceStringListValue_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swDxfMappingFiles** | 0 = This setting is persistent across SOLIDWORKS sessions; you can also interactively get or set the custom map file setting by clicking File, Save As, .dxf or .dwg as Save as type, and Options; separate each string in the list by a line feed  (e.g., the vbLf constant in Visual Basic). |
| **swEmodelAttachmentList** | 2 = Sets which configurations for which to generate and attach STEP files |
| **swEmodelSelectionList** | 1 = Sets which configurations or sheets to save when publishing an eDrawings |

Remarks

Use this enumeration with [ISldWorks::GetUserPreferenceStringListValue](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~GetUserPreferenceStringListValue.html) and [ISldWorks::SetUserPreferenceStringListValue](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~SetUserPreferenceStringListValue.html).

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swUserPreferenceStringListValue\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)  
[swUserPreferenceDoubleValue\_e Enumeration](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swUserPreferenceDoubleValue_e.md)  
[swUserPreferenceIntegerValue\_e Enumeration](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swUserPreferenceIntegerValue_e.md)  
[swUserPreferenceStringValue\_e Enumeration](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swUserPreferenceStringValue_e.md)  
[swUserPreferenceTextFormat\_e Enumeration](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swUserPreferenceTextFormat_e.md)  
[swUserPreferenceToggle\_e Enumeration](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swUserPreferenceToggle_e.md)
