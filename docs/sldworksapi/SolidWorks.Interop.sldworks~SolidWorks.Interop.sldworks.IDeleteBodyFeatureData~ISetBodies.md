# ISetBodies Method (IDeleteBodyFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDeleteBodyFeatureData~ISetBodies`

Sets the bodies to delete.
Sets the bodies to delete.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub ISetBodies( _
   ByVal Count As System.Integer, _
   ByRef Bodies As Body2 _
) 
```

```

Dim instance As IDeleteBodyFeatureData
Dim Count As System.Integer
Dim Bodies As Body2
 
instance.ISetBodies(Count, Bodies)
```

```

void ISetBodies( 
   System.int Count,
   ref Body2 Bodies
)
```

```

void ISetBodies( 
   System.int Count,
   Body2^% Bodies
) 
```

#### Parameters

*Count*
:   Number of bodies

*Bodies*
:   - in-process, unmanaged C++: Pointer to an array of [IBody2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md) objects  of size count

    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDeleteBodyFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDeleteBodyFeatureData.md)  
[IDeleteBodyFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDeleteBodyFeatureData_members.md)  
[IDeleteBodyBodyFeatureData::GetBodiesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDeleteBodyFeatureData~GetBodiesCount.md)  
[IDeleteBodyBodyFeatureData::IGetBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDeleteBodyFeatureData~IGetBodies.md)  
[IDeleteBodyBodyFeatureData::Bodies Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDeleteBodyFeatureData~Bodies.md)
