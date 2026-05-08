# FeatureScopeBodies Property (ISketchPatternFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData~FeatureScopeBodies`

Gets the bodies in this multibody part to be affected by this sketch-driven pattern feature.
Gets the bodies in this multibody part to be affected by this sketch-driven pattern feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property FeatureScopeBodies As System.Object
```

```

Dim instance As ISketchPatternFeatureData
Dim value As System.Object
 
value = instance.FeatureScopeBodies
```

```

System.object FeatureScopeBodies {get;}
```

```

property System.Object^ FeatureScopeBodies {
   System.Object^ get();
}
```

#### Property Value

Array of [bodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md) to be affected

Remarks

This property is valid only if [ISketchPatternFeatureData::GeometryPattern](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData~GeometryPattern.md) is true.

Call [ISketchPatternFeatureData::SetFeatureScope](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData~SetFeatureScope.md) to set this property.

For more information, see the **Sketch Driven Patterns PropertyManager** topic in the SOLIDWORKS user-interface help.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData.md)  
[ISketchPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData_members.md)
