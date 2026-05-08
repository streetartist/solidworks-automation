# GetFlatPatternSketchSegmentCount2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData~GetFlatPatternSketchSegmentCount2`

Gets the number of sketch segments, including bend lines, in this bend.
Gets the number of sketch segments, including bend lines, in this bend.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetFlatPatternSketchSegmentCount2() As System.Integer
```

```

Dim instance As IOneBendFeatureData
Dim value As System.Integer
 
value = instance.GetFlatPatternSketchSegmentCount2()
```

```

System.int GetFlatPatternSketchSegmentCount2()
```

```

System.int GetFlatPatternSketchSegmentCount2(); 
```

#### Return Value

Number of sketch segments in this bend

Remarks

Call this method to populate SegmentsCount in [IOneBendFeatureData::IFlatPatternSketchSegments2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData~IFlatPatternSketchSegments2.md).

Example

[Get Names of Sketch Segments (VBA)](Get_Names_of_Sketch_Segments_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IOneBendFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData.md)  
[IOneBendFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData_members.md)  
[IOneBendFeatureData::FlatPatternSketchSegments2 Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData~FlatPatternSketchSegments2.md)
