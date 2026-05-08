# IGetBodies Method (IScaleFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScaleFeatureData~IGetBodies`

Gets the bodies that are scaled in a multibody part.
Gets the bodies that are scaled in a multibody part.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetBodies( _
   ByVal Count As System.Integer _
) As Body2
```

```

Dim instance As IScaleFeatureData
Dim Count As System.Integer
Dim value As Body2
 
value = instance.IGetBodies(Count)
```

```

Body2 IGetBodies( 
   System.int Count
)
```

```

Body2^ IGetBodies( 
   System.int Count
) 
```

#### Parameters

*Count*
:   Number of bodies that are scaled

#### Return Value

- in-process, unmanaged C++: Pointer to an array of [bodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md) that are scaled of size Count

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

Call [IScaleFeatureData::GetBodiesCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScaleFeatureData~GetBodiesCount.md) before calling this method to get the value for Count.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IScaleFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScaleFeatureData.md)  
[IScaleFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScaleFeatureData_members.md)  
[IScaleFeatureData::ISetBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScaleFeatureData~ISetBodies.md)  
[IScaleFeatureData::Bodies Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScaleFeatureData~Bodies.md)
