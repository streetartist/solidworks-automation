# IGetFaces Method (IDomeFeatureData2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDomeFeatureData2~IGetFaces`

Gets the planar or non-planar faces of this dome feature.
Gets the planar or non-planar faces of this dome feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetFaces( _
   ByVal FaceCount As System.Integer _
) As Face2
```

```

Dim instance As IDomeFeatureData2
Dim FaceCount As System.Integer
Dim value As Face2
 
value = instance.IGetFaces(FaceCount)
```

```

Face2 IGetFaces( 
   System.int FaceCount
)
```

```

Face2^ IGetFaces( 
   System.int FaceCount
) 
```

#### Parameters

*FaceCount*
:   Number of planar or non-planar faces of this dome feature

#### Return Value

- in-process, unmanaged C++: Pointer to an array of planar or non-planar [faces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md) of this dome feature
- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

Call [IDomeFeatureData2::GetFaceCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDomeFeatureData2~GetFaceCount.md) before using this method to determine the size of the output array.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDomeFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDomeFeatureData2.md)  
[IDomeFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDomeFeatureData2_members.md)  
[IDomeFeatureData2::ISetFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDomeFeatureData2~ISetFaces.md)  
[IDomeFeatureData2::Faces Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDomeFeatureData2~Faces.md)
