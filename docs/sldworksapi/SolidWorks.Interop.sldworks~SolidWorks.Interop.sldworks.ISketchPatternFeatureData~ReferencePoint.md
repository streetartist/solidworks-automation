# ReferencePoint Property (ISketchPatternFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData~ReferencePoint`

Gets or sets the reference point for this sketch pattern feature.
Gets or sets the reference point for this sketch pattern feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ReferencePoint As System.Object
```

```

Dim instance As ISketchPatternFeatureData
Dim value As System.Object
 
instance.ReferencePoint = value
 
value = instance.ReferencePoint
```

```

System.object ReferencePoint {get; set;}
```

```

property System.Object^ ReferencePoint {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

Reference point for this sketch pattern feature

Remarks

This property is valid only if [ISketchPatternFeatureData::GetReferencePointType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData~GetReferencePointType.md) does not return -1.

Before calling this property, call [ISketchPatternFeatureData::AccessSelections](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData~AccessSelections.md) or [ISketchPatternFeatureData::IAccessSelections2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData~IAccessSelections2.md) to access the reference point.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData.md)  
[ISketchPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData_members.md)
