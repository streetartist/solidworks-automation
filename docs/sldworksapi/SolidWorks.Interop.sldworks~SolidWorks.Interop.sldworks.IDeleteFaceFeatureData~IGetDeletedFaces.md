# IGetDeletedFaces Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDeleteFaceFeatureData~IGetDeletedFaces`

Get the faces of the DeleteFace feature.
Get the faces of the DeleteFace feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetDeletedFaces( _
   ByVal Count As System.Integer _
) As Face2
```

```

Dim instance As IDeleteFaceFeatureData
Dim Count As System.Integer
Dim value As Face2
 
value = instance.IGetDeletedFaces(Count)
```

```

Face2 IGetDeletedFaces( 
   System.int Count
)
```

```

Face2^ IGetDeletedFaces( 
   System.int Count
) 
```

#### Parameters

*Count*
:   Number of faces

#### Return Value

- in-process, unmanaged C++: Pointer to an array of [faces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md)
- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_methods.htm) for details about this type of method.

Remarks

Call [IDeleteFaceFeatureData::GetDeletedFacesCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDeleteFaceFeatureData~GetDeletedFacesCount.md) before calling this method to get the value for Count.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDeleteFaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDeleteFaceFeatureData.md)  
[IDeleteFaceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDeleteFaceFeatureData_members.md)  
[IDeleteFaceFeatureData::GetDeletedFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDeleteFaceFeatureData~GetDeletedFaces.md)  
[IDeleteFaceFeatureData::ISetDeletedFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDeleteFaceFeatureData~ISetDeletedFaces.md)  
[IDeleteFaceFeatureData::SetDeletedFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDeleteFaceFeatureData~SetDeletedFaces.md)
