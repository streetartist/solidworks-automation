# SelectedPoint Property (ILocalCurvePatternFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData~SelectedPoint`

Gets or sets the reference point for this curve-driven component pattern feature.
Gets or sets the reference point for this curve-driven component pattern feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property SelectedPoint As System.Object
```

```

Dim instance As ILocalCurvePatternFeatureData
Dim value As System.Object
 
instance.SelectedPoint = value
 
value = instance.SelectedPoint
```

```

System.object SelectedPoint {get; set;}
```

```

property System.Object^ SelectedPoint {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

Reference point (see **Remarks**)

Remarks

You can pre-select the reference point using Mark = 32 before creating the feature definition.

This property is valid only if [ILocalCurvePatternFeatureData::D1ReferencePoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData~D1ReferencePoint.md) is set to [swLocalCurvePatternReferencePoint\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLocalCurvePatternReferencePoint_e.html).swLocalCurvePatternSelectedPoint.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

For more information, see the **Curve Driven Component Pattern** topic in the SOLIDWORKS user-interface help.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ILocalCurvePatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData.md)  
[ILocalCurvePatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData_members.md)
