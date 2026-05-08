# ISetSelections Method (IRefPointFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPointFeatureData~ISetSelections`

Sets the number of entities to use to create the reference points.
Sets the number of entities to use to create the reference points.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub ISetSelections( _
   ByVal Count As System.Integer, _
   ByRef Entities As System.Object _
) 
```

```

Dim instance As IRefPointFeatureData
Dim Count As System.Integer
Dim Entities As System.Object
 
instance.ISetSelections(Count, Entities)
```

```

void ISetSelections( 
   System.int Count,
   ref System.object Entities
)
```

```

void ISetSelections( 
   System.int Count,
   System.Object^% Entities
) 
```

#### Parameters

*Count*
:   Number of selected entities

*Entities*
:   - in-process, unmanaged C++: POinter to an array of entities of size Count

    VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRefPointFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPointFeatureData.md)  
[IRefPointFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPointFeatureData_members.md)  
[IRefPointFeatureData::GetSelectionsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPointFeatureData~GetSelectionsCount.md)  
[IRefPointFeatureData::IGetSelections Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPointFeatureData~IGetSelections.md)  
[IRefPointFeatureData::Selections Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPointFeatureData~Selections.md)
