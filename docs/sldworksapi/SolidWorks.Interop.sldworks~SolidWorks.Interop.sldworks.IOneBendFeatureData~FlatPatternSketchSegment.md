# FlatPatternSketchSegment Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData~FlatPatternSketchSegment`

Obsolete. Superseded by IOneBendFeatureData::FlatPatternSketchSegments.
Obsolete. Superseded by [IOneBendFeatureData::FlatPatternSketchSegments](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData~FlatPatternSketchSegments.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property FlatPatternSketchSegment As SketchSegment
```

```

Dim instance As IOneBendFeatureData
Dim value As SketchSegment
 
value = instance.FlatPatternSketchSegment
```

```

SketchSegment FlatPatternSketchSegment {get;}
```

```

property SketchSegment^ FlatPatternSketchSegment {
   SketchSegment^ get();
}
```

#### Property Value

[Sketch segment](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment.md) for this bend

Remarks

The sketch segment is not calculated until the part is unfolded through the user interface or by [IModelDoc2::SetBendState](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetBendState.md) with BendState of swSMBendStateFlattened.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IOneBendFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData.md)  
[IOneBendFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData_members.md)
