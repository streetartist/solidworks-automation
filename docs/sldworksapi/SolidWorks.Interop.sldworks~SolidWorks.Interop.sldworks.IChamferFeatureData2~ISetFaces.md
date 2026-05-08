# ISetFaces Method (IChamferFeatureData2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2~ISetFaces`

Gets the faces to which a chamfer is applied.
Gets the faces to which a chamfer is applied.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub ISetFaces( _
   ByVal Count As System.Integer, _
   ByRef FaceList As Face2 _
) 
```

```

Dim instance As IChamferFeatureData2
Dim Count As System.Integer
Dim FaceList As Face2
 
instance.ISetFaces(Count, FaceList)
```

```

void ISetFaces( 
   System.int Count,
   ref Face2 FaceList
)
```

```

void ISetFaces( 
   System.int Count,
   Face2^% FaceList
) 
```

#### Parameters

*Count*
:   Number of faces

*FaceList*
:   - in-process, unmanaged C++: Pointer to an array of [faces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md) of size Count

    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IChamferFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2.md)  
[IChamferFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2_members.md)  
[IChamferFeatureData2::IGetFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2~IGetFaces.md)  
[IChamferFeatureData2::Faces Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2~Faces.md)
