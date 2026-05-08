# FlatPatternSketchSegments2 Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData~FlatPatternSketchSegments2`

Gets the sketch segments and bend lines for this bend.
Gets the sketch segments and bend lines for this bend.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property FlatPatternSketchSegments2 As System.Object
```

```

Dim instance As IOneBendFeatureData
Dim value As System.Object
 
value = instance.FlatPatternSketchSegments2
```

```

System.object FlatPatternSketchSegments2 {get;}
```

```

property System.Object^ FlatPatternSketchSegments2 {
   System.Object^ get();
}
```

#### Property Value

Array of [ISketchSegment](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment.md)s

Remarks

The sketch segments are calculated in the flattened model. Before calling this method, flatten the model either by unsuppressing the flat pattern in the FeatureManager design tree or by calling [IModelDoc2::SetBendState](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetBendState.md) to set BendState to [swSMBendState\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSMBendState_e.html).swSMBendStateFlattened.

This property returns the bend lines for older parts that do not have flat patterns.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

Example

[Get Names of Sketch Segments (VBA)](Get_Names_of_Sketch_Segments_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IOneBendFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData.md)  
[IOneBendFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData_members.md)  
[IOneBendFeatureData::IFlatPatternSketchSegments2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData~IFlatPatternSketchSegments2.md)  
[IOneBendFeatureData::GetFlatPatternSketchSegmentCount2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData~GetFlatPatternSketchSegmentCount2.md)
