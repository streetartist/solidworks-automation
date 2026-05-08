# ISetFaces Method (IClosedCornerFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClosedCornerFeatureData~ISetFaces`

Sets the faces for this closed corner feature.
Sets the faces for this closed corner feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub ISetFaces( _
   ByVal FaceCount As System.Integer, _
   ByRef FaceArray As System.Object _
) 
```

```

Dim instance As IClosedCornerFeatureData
Dim FaceCount As System.Integer
Dim FaceArray As System.Object
 
instance.ISetFaces(FaceCount, FaceArray)
```

```

void ISetFaces( 
   System.int FaceCount,
   ref System.object FaceArray
)
```

```

void ISetFaces( 
   System.int FaceCount,
   System.Object^% FaceArray
) 
```

#### Parameters

*FaceCount*
:   Number of faces used to describe the closed corner

*FaceArray*
:   - in-process, unmanaged C++: Pointer to an array of [faces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md) used to describe the closed corner of size FaceCount

    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IClosedCornerFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClosedCornerFeatureData.md)  
[IClosedCornerFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClosedCornerFeatureData_members.md)  
[IClosedCornerFeatureData::IGetFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClosedCornerFeatureData~IGetFaces.md)  
[IClosedCornerFeatureData::IGetFacesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClosedCornerFeatureData~IGetFacesCount.md)  
[IClosedCornerFeatureData::Faces Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClosedCornerFeatureData~Faces.md)
