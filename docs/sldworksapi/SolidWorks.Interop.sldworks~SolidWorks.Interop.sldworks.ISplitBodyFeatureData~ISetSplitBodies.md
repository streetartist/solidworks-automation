# ISetSplitBodies Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData~ISetSplitBodies`

Obsolete. Superseded by ISplitBodyFeatureData::SetSplitBodies2.
Obsolete. Superseded by [ISplitBodyFeatureData::SetSplitBodies2.](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData~SetSplitBodies2.md)

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub ISetSplitBodies( _
   ByVal Count As System.Integer, _
   ByRef PathArr As System.String, _
   ByRef FlagArr As System.Boolean _
) 
```

```

Dim instance As ISplitBodyFeatureData
Dim Count As System.Integer
Dim PathArr As System.String
Dim FlagArr As System.Boolean
 
instance.ISetSplitBodies(Count, PathArr, FlagArr)
```

```

void ISetSplitBodies( 
   System.int Count,
   ref System.string PathArr,
   ref System.bool FlagArr
)
```

```

void ISetSplitBodies( 
   System.int Count,
   System.String^% PathArr,
   System.bool% FlagArr
) 
```

#### Parameters

*Count*
:   Number of split bodies for this Split feature

*PathArr*
:   - in-process, unmanaged C++: Pointer to an array of paths and file names of the split bodies

    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

*FlagArr*
:   - in-process, unmanaged C++: Pointer to an array of booleans indicating whether corresponding PathArr bodies are consumed; true indicates the body is removed from the original part, false otherwise
    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISplitBodyFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData.md)  
[ISplitBodyFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData_members.md)  
[ISplitBodyFeatureData::SetSplitBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData~SetSplitBodies.md)  
[ISplitBodyFeatureData::GetSplitBodiesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData~GetSplitBodiesCount.md)  
[ISplitBodyFeatureData::IGetSplitBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData~IGetSplitBodies.md)  
[ISplitBodyFeatureData::GetSplitBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData~GetSplitBodies.md)
