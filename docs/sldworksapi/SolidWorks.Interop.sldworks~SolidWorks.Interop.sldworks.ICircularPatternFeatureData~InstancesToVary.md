# InstancesToVary Property (ICircularPatternFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~InstancesToVary`

Gets or sets whether to vary the spacing of pattern instances in this circular pattern feature.
Gets or sets whether to vary the spacing of pattern instances in this circular pattern feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property InstancesToVary As System.Boolean
```

```

Dim instance As ICircularPatternFeatureData
Dim value As System.Boolean
 
instance.InstancesToVary = value
 
value = instance.InstancesToVary
```

```

System.bool InstancesToVary {get; set;}
```

```

property System.bool InstancesToVary {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to vary the spacing of pattern instances, false to not

Remarks

This property is valid only when editing the circular pattern feature. You cannot set this property during creation of the feature.

To vary instances in a circular pattern feature:

1. Call [IFeature::GetDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetDefinition.md).
2. Call [ICircularPatternFeatureData::AccessSelections](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~AccessSelections.md).
3. Set this property to true.
4. Call [IFeature::ModifyDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~ModifyDefinition.md).
5. Call ICircularPatternFeatureData::AccessSelections.
6. Call [ICircularPatternFeatureData::GetInstanceToVaryOptions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~GetInstanceToVaryOptions.md).
7. Modify [IInstanceToVaryOptions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInstanceToVaryOptions.md) properties.
8. Call [ICircularPatternFeatureData::SetInstanceToVaryOptions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~SetInstanceToVaryOptions.md).
9. Call IFeature::ModifyDefinition.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICircularPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData.md)  
[ICircularPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData_members.md)
