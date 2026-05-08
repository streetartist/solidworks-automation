# IGetExcludedFaces Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData~IGetExcludedFaces`

Gets the faces that are excluded from this Flat-Pattern feature.
Gets the faces that are excluded from this Flat-Pattern feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetExcludedFaces() As System.Object
```

```

Dim instance As IFlatPatternFeatureData
Dim value As System.Object
 
value = instance.IGetExcludedFaces()
```

```

System.object IGetExcludedFaces()
```

```

System.Object^ IGetExcludedFaces(); 
```

#### Return Value

- in-process, unmanaged C++: Pointer to an array of [IFace2s](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md)
- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

To get the size of the array returned by this method, call [IFlatPatternFeatureData::IGetExcludedFacesCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData~IGetExcludedFacesCount.md).

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFlatPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData.md)  
[IFlatPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData_members.md)  
[IFlatPatternFeatureData::ExcludedFaces Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData~ExcludedFaces.md)  
[IFlatPatternFeatureData::ISetExcludedFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData~ISetExcludedFaces.md)
