# IGetPartingLines Method (IPartingLineFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData~IGetPartingLines`

Gets the edges used as parting lines.
Gets the edges used as parting lines.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetPartingLines( _
   ByVal Count As System.Integer _
) As Edge
```

```

Dim instance As IPartingLineFeatureData
Dim Count As System.Integer
Dim value As Edge
 
value = instance.IGetPartingLines(Count)
```

```

Edge IGetPartingLines( 
   System.int Count
)
```

```

Edge^ IGetPartingLines( 
   System.int Count
) 
```

#### Parameters

*Count*
:   Number of edges used as parting lines

#### Return Value

- in-process, unmanaged C++: Pointer to an array of [edges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md) used as parting lines of size Count
- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

Call [IPartingLineFeatureData::GetPartingLinesCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData~GetPartingLinesCount.md) before calling this method.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPartingLineFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData.md)  
[IPartingLineFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData_members.md)  
[IPartingLineFeatureData::ISetPartingLines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData~ISetPartingLines.md)  
[IPartingLineFeatureData::PartingLines Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData~PartingLines.md)
