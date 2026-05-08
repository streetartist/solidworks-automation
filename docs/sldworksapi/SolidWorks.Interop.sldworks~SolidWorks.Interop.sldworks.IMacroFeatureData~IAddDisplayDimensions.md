# IAddDisplayDimensions Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~IAddDisplayDimensions`

Adds the specified display dimensions to this macro feature.
Adds the specified display dimensions to this macro feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub IAddDisplayDimensions( _
   ByVal DimCount As System.Integer, _
   ByRef DimTypes As System.Integer, _
   ByRef DimValues As System.Double _
) 
```

```

Dim instance As IMacroFeatureData
Dim DimCount As System.Integer
Dim DimTypes As System.Integer
Dim DimValues As System.Double
 
instance.IAddDisplayDimensions(DimCount, DimTypes, DimValues)
```

```

void IAddDisplayDimensions( 
   System.int DimCount,
   ref System.int DimTypes,
   ref System.double DimValues
)
```

```

void IAddDisplayDimensions( 
   System.int DimCount,
   System.int% DimTypes,
   System.double% DimValues
) 
```

#### Parameters

*DimCount*
:   Number of display dimensions

*DimTypes*
:   - in-process, unmanaged C++: Pointer to an array of display dimension types as defined [swDimensionType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDimensionType_e.html)
    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

*DimValues*
:   - in-process, unmanaged C++: Pointer to an array of display dimension values
    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMacroFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData.md)  
[IMacroFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData_members.md)
