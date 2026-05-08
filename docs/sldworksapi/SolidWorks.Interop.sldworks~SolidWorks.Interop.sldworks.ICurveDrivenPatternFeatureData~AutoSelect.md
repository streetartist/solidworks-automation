# AutoSelect Property (ICurveDrivenPatternFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData~AutoSelect`

Gets whether to automatically select all bodies in a multibody part intersected by this curve-driven pattern feature.
Gets whether to automatically select all bodies in a multibody part intersected by this curve-driven pattern feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property AutoSelect As System.Boolean
```

```

Dim instance As ICurveDrivenPatternFeatureData
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

True to automatically select all bodies intersected by this curve driven pattern feature, false to specify affected bodies

Remarks

This property is valid only if [ICurveDrivenPatternFeatureData::GeometryPattern](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData~GeometryPattern.md) is true.

Call [ICurveDrivenPatternFeatureData::SetFeatureScope](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData~SetFeatureScope.md) to set this property.

For more information, see the **Curve Driven Patterns and the** **Curve Driven Pattern PropertyManager** topic in the SOLIDWORKS user-interface help.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICurveDrivenPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData.md)  
[ICurveDrivenPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData_members.md)
