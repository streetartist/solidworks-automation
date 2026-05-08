# IGetMultipleThicknessFaces Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShellFeatureData~IGetMultipleThicknessFaces`

Gets the multiple-thickness faces in this shell feature.
Gets the multiple-thickness faces in this shell feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetMultipleThicknessFaces( _
   ByVal Count As System.Integer _
) As System.Object
```

```

Dim instance As IShellFeatureData
Dim Count As System.Integer
Dim value As System.Object
 
value = instance.IGetMultipleThicknessFaces(Count)
```

```

System.object IGetMultipleThicknessFaces( 
   System.int Count
)
```

```

System.Object^ IGetMultipleThicknessFaces( 
   System.int Count
) 
```

#### Parameters

*Count*
:   Number of multiple-thickness faces

#### Return Value

- in-process, unmanaged C++: Pointer to an array of multiple-thickness [faces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md) of size Count

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

Call [IShellFeatureData::GetMultipleThicknessFacesCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShellFeatureData~GetMultipleThicknessFacesCount.md) before calling this method to get the size of the array for this method.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IShellFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShellFeatureData.md)  
[IShellFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShellFeatureData_members.md)  
[IShellFeatureData::GetMultipleThicknessAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShellFeatureData~GetMultipleThicknessAtIndex.md)  
[IShellFeatureData::ISetMultipleThicknessFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShellFeatureData~ISetMultipleThicknessFaces.md)  
[IShellFeatureData::SetMultipleThicknessAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShellFeatureData~SetMultipleThicknessAtIndex.md)  
[IShellFeatureData::MultipleThicknessFaces Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShellFeatureData~MultipleThicknessFaces.md)  
[IShellFeatureData::Thickness Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShellFeatureData~Thickness.md)
