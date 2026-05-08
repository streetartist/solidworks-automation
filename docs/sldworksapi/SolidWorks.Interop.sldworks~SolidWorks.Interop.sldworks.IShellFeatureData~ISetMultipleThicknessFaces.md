# ISetMultipleThicknessFaces Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShellFeatureData~ISetMultipleThicknessFaces`

Sets the multiple-thickness faces in this shell feature.
Sets the multiple-thickness faces in this shell feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub ISetMultipleThicknessFaces( _
   ByVal Count As System.Integer, _
   ByRef FaceArray As System.Object _
) 
```

```

Dim instance As IShellFeatureData
Dim Count As System.Integer
Dim FaceArray As System.Object
 
instance.ISetMultipleThicknessFaces(Count, FaceArray)
```

```

void ISetMultipleThicknessFaces( 
   System.int Count,
   ref System.object FaceArray
)
```

```

void ISetMultipleThicknessFaces( 
   System.int Count,
   System.Object^% FaceArray
) 
```

#### Parameters

*Count*
:   Number of faces

*FaceArray*
:   - in-process, unmanaged C++: Pointer to an array of [faces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md) to set to multiple thickness of size Count

    VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IShellFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShellFeatureData.md)  
[IShellFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShellFeatureData_members.md)  
[IShellFeatureData::IGetMultipleThicknessFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShellFeatureData~IGetMultipleThicknessFaces.md)  
[IShellFeatureData::GetMultipleThicknessAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShellFeatureData~GetMultipleThicknessAtIndex.md)  
[IShellFeatureData::GetMultipleThicknessFacesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShellFeatureData~GetMultipleThicknessFacesCount.md)  
[IShellFeatureData::SetMultipleThicknessAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShellFeatureData~SetMultipleThicknessAtIndex.md)  
[IShellFeatureData::MultipleThicknessFaces Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShellFeatureData~MultipleThicknessFaces.md)  
[IShellFeatureData::Thickness Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShellFeatureData~Thickness.md)
