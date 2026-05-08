# ISetEditBodies Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~ISetEditBodies`

Sets the bodies to be modified by this macro feature.
Sets the bodies to be modified by this macro feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub ISetEditBodies( _
   ByVal BodiesCount As System.Integer, _
   ByRef PBodies As Body2 _
) 
```

```

Dim instance As IMacroFeatureData
Dim BodiesCount As System.Integer
Dim PBodies As Body2
 
instance.ISetEditBodies(BodiesCount, PBodies)
```

```

void ISetEditBodies( 
   System.int BodiesCount,
   ref Body2 PBodies
)
```

```

void ISetEditBodies( 
   System.int BodiesCount,
   Body2^% PBodies
) 
```

#### Parameters

*BodiesCount*
:   Number of bodies to be modified by this macro feature

*PBodies*
:   - in-process, unmanaged C++: Pointer to an array of [bodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md) to be modified by this macro feature

    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMacroFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData.md)  
[IMacroFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData_members.md)  
[IMacroFeatureData::IGetEditBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~IGetEditBodies.md)  
[IMacroFeatureData::EditBodies Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~EditBodies.md)
