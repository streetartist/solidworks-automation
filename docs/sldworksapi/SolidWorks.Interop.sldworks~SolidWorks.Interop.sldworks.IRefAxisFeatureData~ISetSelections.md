# ISetSelections Method (IRefAxisFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxisFeatureData~ISetSelections`

Sets the entities for this reference axis feature.
Sets the entities for this reference axis feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ISetSelections( _
   ByVal Count As System.Integer, _
   ByRef EntArr As System.Object _
) As System.Boolean
```

```

Dim instance As IRefAxisFeatureData
Dim Count As System.Integer
Dim EntArr As System.Object
Dim value As System.Boolean
 
value = instance.ISetSelections(Count, EntArr)
```

```

System.bool ISetSelections( 
   System.int Count,
   ref System.object EntArr
)
```

```

System.bool ISetSelections( 
   System.int Count,
   System.Object^% EntArr
) 
```

#### Parameters

*Count*
:   Number of entities

*EntArr*
:   - in-process,unmanaged C++: Pointer to an array of entities for this reference axis feature
    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

#### Return Value

True if the method executed, false if not

Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRefAxisFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxisFeatureData.md)  
[IRefAxisFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxisFeatureData_members.md)  
[IRefAxisFeatureData::SetSelections Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxisFeatureData~SetSelections.md)  
[IRefAxisFeatureData::GetSelections Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxisFeatureData~GetSelections.md)  
[IRefAxisFeatureData::GetSelectionsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxisFeatureData~GetSelectionsCount.md)  
[IRefAxisFeatureData::IGetSelections Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxisFeatureData~IGetSelections.md)
