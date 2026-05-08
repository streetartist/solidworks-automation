# IGetDisplayDimensions Method (IMacroFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~IGetDisplayDimensions`

Gets the display dimensions for this macro feature.
Gets the display dimensions for this macro feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub IGetDisplayDimensions( _
   ByVal DimCount As System.Integer, _
   ByRef Dims As DisplayDimension _
) 
```

```

Dim instance As IMacroFeatureData
Dim DimCount As System.Integer
Dim Dims As DisplayDimension
 
instance.IGetDisplayDimensions(DimCount, Dims)
```

```

void IGetDisplayDimensions( 
   System.int DimCount,
   out DisplayDimension Dims
)
```

```

void IGetDisplayDimensions( 
   System.int DimCount,
   [Out] DisplayDimension^ Dims
) 
```

#### Parameters

*DimCount*
:   Number of display dimensions

*Dims*
:   - in-process, unmanaged C++: Pointer to an array of [display dimensions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.md)

    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

Before calling this method, call [IMacroFeatureData::GetDisplayDimensionCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetDisplayDimensionCount.md) to determine the size of the array.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMacroFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData.md)  
[IMacroFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData_members.md)  
[IMacroFeatureData::GetDisplayDimensions Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetDisplayDimensions.md)
