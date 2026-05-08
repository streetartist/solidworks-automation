# swCornerReliefSuitCaseType_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCornerReliefSuitCaseType_e`

Sheet metal corner relief suitcase types.
Sheet metal corner relief suitcase types.

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

<System.Runtime.InteropServices.GuidAttribute("10C4682D-B557-40DE-B10B-542ADEF93B7A")>
Public Enum swCornerReliefSuitCaseType_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swCornerReliefSuitCaseType_e
```

```

[System.Runtime.InteropServices.Guid("10C4682D-B557-40DE-B10B-542ADEF93B7A")]
public enum swCornerReliefSuitCaseType_e : System.Enum 
```

```

public enum swCornerReliefSuitCaseType_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("10C4682D-B557-40DE-B10B-542ADEF93B7A")
public enum swCornerReliefSuitCaseType_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("10C4682D-B557-40DE-B10B-542ADEF93B7A")]
__value public enum swCornerReliefSuitCaseType_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("10C4682D-B557-40DE-B10B-542ADEF93B7A")]
public enum class swCornerReliefSuitCaseType_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swCornerReliefSuitCase\_Default** | 0 = Leaves the gap unchanged |
| **swCornerReliefSuitCase\_ExtendGapInBendArea** | 1 = Cut the corner relief with the gap |
| **swCornerReliefSuitCase\_FillInSomeGap** | 2 = Extends the corner relief material into the gap |

Remarks

A suitcase is a closed spherical corner without any cutouts.

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swCornerReliefSuitCaseType\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
