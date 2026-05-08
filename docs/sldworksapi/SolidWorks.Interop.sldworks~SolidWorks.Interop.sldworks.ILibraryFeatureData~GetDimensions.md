# GetDimensions Method (ILibraryFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~GetDimensions`

Gets the names and values of the specified type of dimension for this library feature.
Gets the names and values of the specified type of dimension for this library feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetDimensions( _
   ByVal Type As System.Integer, _
   ByRef DimName As System.Object _
) As System.Object
```

```

Dim instance As ILibraryFeatureData
Dim Type As System.Integer
Dim DimName As System.Object
Dim value As System.Object
 
value = instance.GetDimensions(Type, DimName)
```

```

System.object GetDimensions( 
   System.int Type,
   out System.object DimName
)
```

```

System.Object^ GetDimensions( 
   System.int Type,
   [Out] System.Object^ DimName
) 
```

#### Parameters

*Type*
:   Type of dimension as defined in [swLibFeatDimensionType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLibFeatDimensionType_e.html)

*DimName*
:   Array of the dimension names

#### Return Value

Array of the values of the dimensions

Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

Example

[Get Library Feature Data (VBA)](Get_Library_Feature_Data_Example_VB.htm)  
[Get Library Feature Data (VB.NET)](Get_Library_Feature_Data_Example_VBNET.htm)  
[Get Library Feature Data (C#)](Get_Library_Feature_Data_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ILibraryFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData.md)  
[ILibraryFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData_members.md)  
[ILibraryFeatureData::IGetDimensions Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~IGetDimensions.md)  
[ILibraryFeatureData::GetDimensionsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~GetDimensionsCount.md)  
[ILibraryFeatureData::OverrideDimension Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~OverrideDimension.md)
