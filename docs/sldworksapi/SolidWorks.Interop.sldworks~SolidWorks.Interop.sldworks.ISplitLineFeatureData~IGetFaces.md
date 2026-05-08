# IGetFaces Method (ISplitLineFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData~IGetFaces`

Gets the faces split by the split line.
Gets the faces split by the split line.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetFaces( _
   ByVal Count As System.Integer _
) As Face2
```

```

Dim instance As ISplitLineFeatureData
Dim Count As System.Integer
Dim value As Face2
 
value = instance.IGetFaces(Count)
```

```

Face2 IGetFaces( 
   System.int Count
)
```

```

Face2^ IGetFaces( 
   System.int Count
) 
```

#### Parameters

*Count*
:   Number of faces to split

#### Return Value

- in-process, unmanaged C++: Pointer to an array of split [faces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md)

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

Before calling this method, call [ISplitLineFeatureData::GetFacesCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData~GetFacesCount.md) to determine the size of the array for this method.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISplitLineFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData.md)  
[ISplitLineFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData_members.md)  
[ISplitLineFeatureData::ISetFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData~ISetFaces.md)  
[ISplitLineFeatureData::Faces Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData~Faces.md)
