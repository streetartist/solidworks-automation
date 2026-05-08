# SetDimension Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~SetDimension`

Sets a dimension's type, name, and value for the library feature.
Sets a dimension's type, name, and value for the library feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetDimension( _
   ByVal Type As System.Integer, _
   ByVal DimName As System.String, _
   ByVal DimVal As System.Double _
) As System.Boolean
```

```

Dim instance As ILibraryFeatureData
Dim Type As System.Integer
Dim DimName As System.String
Dim DimVal As System.Double
Dim value As System.Boolean
 
value = instance.SetDimension(Type, DimName, DimVal)
```

```

System.bool SetDimension( 
   System.int Type,
   System.string DimName,
   System.double DimVal
)
```

```

System.bool SetDimension( 
   System.int Type,
   System.String^ DimName,
   System.double DimVal
) 
```

#### Parameters

*Type*
:   Type of dimension as defined in [swLibFeatDimensionType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLibFeatDimensionType_e.html)

*DimName*
:   Name of dimension

*DimVal*
:   Name of dimension

#### Return Value

True is the dimension is set, false if not

Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ILibraryFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData.md)  
[ILibraryFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData_members.md)  
[ILibraryFeatureData::GetDimensions Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~GetDimensions.md)  
[ILibraryFeatureData::GetDimensionsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~GetDimensionsCount.md)  
[ILibraryFeatureData::IGetDimensions Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~IGetDimensions.md)
