# IFlatPatternSketchSegments Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData~IFlatPatternSketchSegments`

Obsolete. Superseded by IOneBendFeatureData::IFlatPatternSketchSegments2.
Obsolete. Superseded by [IOneBendFeatureData::IFlatPatternSketchSegments2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData~IFlatPatternSketchSegments2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IFlatPatternSketchSegments( _
   ByVal SegmentsCount As System.Integer _
) As SketchSegment
```

```

Dim instance As IOneBendFeatureData
Dim SegmentsCount As System.Integer
Dim value As SketchSegment
 
value = instance.IFlatPatternSketchSegments(SegmentsCount)
```

```

SketchSegment IFlatPatternSketchSegments( 
   System.int SegmentsCount
)
```

```

SketchSegment^ IFlatPatternSketchSegments( 
   System.int SegmentsCount
) 
```

#### Parameters

*SegmentsCount*
:   Number of sketch segments (see **Remarks**)

#### Return Value

- in-process, unmanaged C++: Pointer to an array of [ISketchSegment](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment.md)s
- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

Before calling this method, call [IOneBendFeatureData::GetFlatPatternSketchSegmentCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData~GetFlatPatternSketchSegmentCount.md) to populate SegmentsCount.

The sketch segments are calculated in the flattened model. Before calling this method, flatten the model either by un-suppressing the flat pattern in the FeatureManager design tree or by calling [IModelDoc2::SetBendState](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetBendState.md) to set BendState to [swSMBendState\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSMBendState_e.html).swSMBendStateFlattened.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IOneBendFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData.md)  
[IOneBendFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData_members.md)  
[IOneBendFeatureData::FlatPatternSketchSegments Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData~FlatPatternSketchSegments.md)
