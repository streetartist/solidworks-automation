# AlignmentReferences Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~AlignmentReferences`

Gets or sets the alignment references for components whose orientation axes align to them.
Gets or sets the alignment references for components whose orientation axes align to them.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property AlignmentReferences As System.Object
```

```

Dim instance As IMirrorComponentFeatureData
Dim value As System.Object
 
instance.AlignmentReferences = value
 
value = instance.AlignmentReferences
```

```

System.object AlignmentReferences {get; set;}
```

```

property System.Object^ AlignmentReferences {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

Array of [IEdge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md), [IFace2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md), [IRefPlane](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane.md), [ISketchSegment](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment.md) (linear)

Remarks

This property is valid only if [IMirrorComponentFeatureData::ComponentsToInstanceAlignToSelection](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~ComponentsToInstanceAlignToSelection.md) is not null or Nothing.

There is a one-to-one mapping between this property's array and IMirrorComponentFeatureData::ComponentsToInstanceAlignToSelection. If this array contains fewer elements than IMirrorComponentFeatureData::ComponentsToInstanceAlignToSelection, then the feature will fail to be created.

Example

See the [IMirrorComponentFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData.md) example.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMirrorComponentFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData.md)  
[IMirrorComponentFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData_members.md)  
[IMirrorComponentFeatureData::FlipDirections Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~FlipDirections.md)
