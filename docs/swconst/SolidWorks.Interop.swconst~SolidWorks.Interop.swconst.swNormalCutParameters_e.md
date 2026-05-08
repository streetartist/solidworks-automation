# swNormalCutParameters_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swNormalCutParameters_e`

Sheet metal normal cut parameters.
Sheet metal normal cut parameters.

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

<System.Runtime.InteropServices.GuidAttribute("CF41A180-D834-46A3-8795-4874D7492EBF")>
Public Enum swNormalCutParameters_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swNormalCutParameters_e
```

```

[System.Runtime.InteropServices.Guid("CF41A180-D834-46A3-8795-4874D7492EBF")]
public enum swNormalCutParameters_e : System.Enum 
```

```

public enum swNormalCutParameters_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("CF41A180-D834-46A3-8795-4874D7492EBF")
public enum swNormalCutParameters_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("CF41A180-D834-46A3-8795-4874D7492EBF")]
__value public enum swNormalCutParameters_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("CF41A180-D834-46A3-8795-4874D7492EBF")]
public enum class swNormalCutParameters_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swNormalCutExtent** | 0 = Cuts the maximum amount from the intersection profiles on the top and bottom of the sheet metal body |
| **swNormalCutOffsetPlane** | 1 = Adjusts the layer where the intersection curve intersects the sheet metal body; Select a reference plane or top or bottom face to define the offset plane and then either set [ISMNormalCutFeatureData2::LinkToKFactor](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMNormalCutFeatureData2~LinkToKFactor.html) to true or set [ISMNormalCutFeatureData2::LayerAdjustmentValue](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMNormalCutFeatureData2~LayerAdjustmentValue.html) to a value between 0 and 1 to adjust the layer |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swNormalCutParameters\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
