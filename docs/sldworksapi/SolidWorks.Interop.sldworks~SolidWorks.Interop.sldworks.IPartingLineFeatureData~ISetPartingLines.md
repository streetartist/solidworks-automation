# ISetPartingLines Method (IPartingLineFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData~ISetPartingLines`

Sets the edges to use as parting lines.
Sets the edges to use as parting lines.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub ISetPartingLines( _
   ByVal Count As System.Integer, _
   ByRef EntIn As Edge _
) 
```

```

Dim instance As IPartingLineFeatureData
Dim Count As System.Integer
Dim EntIn As Edge
 
instance.ISetPartingLines(Count, EntIn)
```

```

void ISetPartingLines( 
   System.int Count,
   ref Edge EntIn
)
```

```

void ISetPartingLines( 
   System.int Count,
   Edge^% EntIn
) 
```

#### Parameters

*Count*
:   Number of edges to use as parting lines

*EntIn*
:   - in-process, unmanaged C++: Poitner to an array of [edges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md) to use as parting lines of size Count

    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPartingLineFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData.md)  
[IPartingLineFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData_members.md)  
[IPartingLineFeatureData::PartingLines Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData~PartingLines.md)  
[IPartingLineFeatureData::IGetPartingLines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData~IGetPartingLines.md)  
[IPartingLineFeatureData::GetPartingLinesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData~GetPartingLinesCount.md)
