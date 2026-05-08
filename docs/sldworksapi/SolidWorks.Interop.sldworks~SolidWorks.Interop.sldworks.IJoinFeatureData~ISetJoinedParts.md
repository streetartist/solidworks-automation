# ISetJoinedParts Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJoinFeatureData~ISetJoinedParts`

Sets the parts to join.
Sets the parts to join.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub ISetJoinedParts( _
   ByVal Count As System.Integer, _
   ByRef Parts As Component2 _
) 
```

```

Dim instance As IJoinFeatureData
Dim Count As System.Integer
Dim Parts As Component2
 
instance.ISetJoinedParts(Count, Parts)
```

```

void ISetJoinedParts( 
   System.int Count,
   ref Component2 Parts
)
```

```

void ISetJoinedParts( 
   System.int Count,
   Component2^% Parts
) 
```

#### Parameters

*Count*
:   Number of parts to join

*Parts*
:   - in-process, unmanaged C++: Pointer to an array of joined parts, the [IComponent2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md) objects

    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IJoinFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJoinFeatureData.md)  
[IJoinFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJoinFeatureData_members.md)  
[IJoinFeatureData::GetJoinedPartsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJoinFeatureData~GetJoinedPartsCount.md)  
[IJoinFeatureData::IGetJoinedParts Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJoinFeatureData~IGetJoinedParts.md)  
[IJoinFeatureData::JoinedParts Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJoinFeatureData~JoinedParts.md)
