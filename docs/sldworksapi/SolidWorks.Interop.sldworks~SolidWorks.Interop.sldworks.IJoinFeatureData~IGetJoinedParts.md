# IGetJoinedParts Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJoinFeatureData~IGetJoinedParts`

Gets the joined parts.
Gets the joined parts.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetJoinedParts( _
   ByVal Count As System.Integer _
) As Component2
```

```

Dim instance As IJoinFeatureData
Dim Count As System.Integer
Dim value As Component2
 
value = instance.IGetJoinedParts(Count)
```

```

Component2 IGetJoinedParts( 
   System.int Count
)
```

```

Component2^ IGetJoinedParts( 
   System.int Count
) 
```

#### Parameters

*Count*
:   Number of joined parts

#### Return Value

- in-process, unmanaged C++: Pointer to an array of joined parts, the [IComponent2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md) objects

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

Call [IJoinFeatureData::GetJoinedPartsCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJoinFeatureData~GetJoinedPartsCount.md) before calling this method to determine Count.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IJoinFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJoinFeatureData.md)  
[IJoinFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJoinFeatureData_members.md)  
[IJoinFeatureData::ISetJoinedParts Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJoinFeatureData~ISetJoinedParts.md)  
[IJoinFeatureData::JoinedParts Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJoinFeatureData~JoinedParts.md)
