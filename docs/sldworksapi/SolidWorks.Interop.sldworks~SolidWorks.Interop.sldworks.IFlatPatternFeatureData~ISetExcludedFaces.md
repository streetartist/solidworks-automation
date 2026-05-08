# ISetExcludedFaces Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData~ISetExcludedFaces`

Sets the faces to exclude from this Flat-Pattern feature.
Sets the faces to exclude from this Flat-Pattern feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub ISetExcludedFaces( _
   ByVal FaceCount As System.Integer, _
   ByRef FaceArray As System.Object _
) 
```

```

Dim instance As IFlatPatternFeatureData
Dim FaceCount As System.Integer
Dim FaceArray As System.Object
 
instance.ISetExcludedFaces(FaceCount, FaceArray)
```

```

void ISetExcludedFaces( 
   System.int FaceCount,
   ref System.object FaceArray
)
```

```

void ISetExcludedFaces( 
   System.int FaceCount,
   System.Object^% FaceArray
) 
```

#### Parameters

*FaceCount*
:   Number of faces to exclude

*FaceArray*
:   - in-process, unmanaged C++: Pointer to an array of [IFace2s](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md) to exclude
    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFlatPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData.md)  
[IFlatPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData_members.md)  
[IFlatPatternFeatureData::IGetExcludedFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData~IGetExcludedFaces.md)  
[IFlatPatternFeatureData::IGetExcludedFacesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData~IGetExcludedFacesCount.md)  
[IFlatPatternFeatureData::ExcludedFaces Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData~ExcludedFaces.md)
