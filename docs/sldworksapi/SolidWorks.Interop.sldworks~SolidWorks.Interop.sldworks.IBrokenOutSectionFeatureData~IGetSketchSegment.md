# IGetSketchSegment Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBrokenOutSectionFeatureData~IGetSketchSegment`

Gets the sketch segments that form the border of this broken-out section feature.
Gets the sketch segments that form the border of this broken-out section feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetSketchSegment( _
   ByVal Count As System.Integer _
) As SketchSegment
```

```

Dim instance As IBrokenOutSectionFeatureData
Dim Count As System.Integer
Dim value As SketchSegment
 
value = instance.IGetSketchSegment(Count)
```

```

SketchSegment IGetSketchSegment( 
   System.int Count
)
```

```

SketchSegment^ IGetSketchSegment( 
   System.int Count
) 
```

#### Parameters

*Count*
:   Number of sketch segments

#### Return Value

- In-process, unmanaged C++: Pointer to an array of [ISketchSegment](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment.md)s
- VBA, VB.NET, C#, and C++/CLI: Not supported

 See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

To get the sketch segments that form the border of this broken-out section feature:

1. Set the property [IBrokenOutSectionFeatureData::EditSketch](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBrokenOutSectionFeatureData~EditSketch.md) to true.
2. Call [IBrokenOutSectionFeatureData::GetSketchSegmentCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBrokenOutSectionFeatureData~GetSketchSegmentCount.md) to set the value of this method's Count parameter.
3. Call this method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBrokenOutSectionFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBrokenOutSectionFeatureData.md)  
[IBrokenOutSectionFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBrokenOutSectionFeatureData_members.md)  
[IBrokenOutSectionFeatureData::SketchSegment Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBrokenOutSectionFeatureData~SketchSegment.md)
