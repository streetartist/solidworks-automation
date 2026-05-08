# AutoSelect Property (ISketchPatternFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData~AutoSelect`

Gets whether to automatically select all bodies in a multibody part intersected by this sketch-driven pattern feature.
Gets whether to automatically select all bodies in a multibody part intersected by this sketch-driven pattern feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property AutoSelect As System.Boolean
```

```

Dim instance As ISketchPatternFeatureData
Dim value As System.Boolean
 
value = instance.AutoSelect
```

```

System.bool AutoSelect {get;}
```

```

property System.bool AutoSelect {
   System.bool get();
}
```

#### Property Value

True to automatically select all bodies intersected by this sketch-driven pattern feature, false to specify affected bodies (see **Remarks**)

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
