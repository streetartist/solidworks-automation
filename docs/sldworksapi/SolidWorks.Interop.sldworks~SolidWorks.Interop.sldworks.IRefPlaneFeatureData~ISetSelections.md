# ISetSelections Method (IRefPlaneFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData~ISetSelections`

Sets the entities to use to create the reference plane feature.
Sets the entities to use to create the reference plane feature.

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

Dim instance As IRefPlaneFeatureData
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
:   - in-process, unmanaged C++: Pointer to an array of entities of size Count

    VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

**IMPORTANT:** Reference planes created in SOLIDWORKS 2010 or later are constraint based; reference planes created in SOLIDWORKS 2009 or earlier are not. See the **Remarks** section in the [IRefPlaneFeatureData interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData.md) topic for details about reference planes and this interface.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRefPlaneFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData.md)  
[IRefPlaneFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData_members.md)  
[IRefPlaneFeatureData::GetSelectionsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData~GetSelectionsCount.md)  
[IRefPlaneFeatureData::IGetSelections Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData~IGetSelections.md)  
[IRefPlaneFeatureData::Selections Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData~Selections.md)
