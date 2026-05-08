# ISetFaces Method (IDomeFeatureData2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDomeFeatureData2~ISetFaces`

Sets the planar or non-planar faces of this dome feature.
Sets the planar or non-planar faces of this dome feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub ISetFaces( _
   ByVal FaceCount As System.Integer, _
   ByRef FaceList As Face2 _
) 
```

```

Dim instance As IDomeFeatureData2
Dim FaceCount As System.Integer
Dim FaceList As Face2
 
instance.ISetFaces(FaceCount, FaceList)
```

```

void ISetFaces( 
   System.int FaceCount,
   ref Face2 FaceList
)
```

```

void ISetFaces( 
   System.int FaceCount,
   Face2^% FaceList
) 
```

#### Parameters

*FaceCount*
:   Number of planar or non-planar faces

*FaceList*
:   - in-process, unmanaged C++: Pointer to an array of planar and non-planar [faces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md) of this dome feature

    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

This method does not affect geometry until you call [IFeature::IModifyDefintion2.](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IModifyDefinition2.md)

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDomeFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDomeFeatureData2.md)  
[IDomeFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDomeFeatureData2_members.md)  
[IDomeFeatureData2::GetFaceCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDomeFeatureData2~GetFaceCount.md)  
[IDomeFeatureData2::IGetFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDomeFeatureData2~IGetFaces.md)  
[IDomeFeatureData2::Faces Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDomeFeatureData2~Faces.md)
