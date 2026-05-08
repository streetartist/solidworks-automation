# GetFlatPatternSketchSegmentCount Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData~GetFlatPatternSketchSegmentCount`

Obsolete. Superseded by IOneBendFeatureData::GetFlatPatternSketchSegmentCount2.
Obsolete. Superseded by [IOneBendFeatureData::GetFlatPatternSketchSegmentCount2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData~GetFlatPatternSketchSegmentCount2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetFlatPatternSketchSegmentCount() As System.Integer
```

```

Dim instance As IOneBendFeatureData
Dim value As System.Integer
 
value = instance.GetFlatPatternSketchSegmentCount()
```

```

System.int GetFlatPatternSketchSegmentCount()
```

```

System.int GetFlatPatternSketchSegmentCount(); 
```

#### Return Value

Number of sketch segments

Remarks

Call this method to populate SegmentsCount in [IOneBendFeatureData::IFlatPatternSketchSegments](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData~IFlatPatternSketchSegments.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IOneBendFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData.md)  
[IOneBendFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData_members.md)  
[IOneBendFeatureData::FlatPatternSketchSegments Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData~FlatPatternSketchSegments.md)
