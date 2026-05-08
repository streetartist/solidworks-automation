# AutoSelect Property (ISimpleHoleFeatureData2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2~AutoSelect`

Gets or sets whether to automatically select all or only specific bodies for the simple hole feature to affect in a multibody body.
Gets or sets whether to automatically select all or only specific bodies for the simple hole feature to affect in a multibody body.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property AutoSelect As System.Boolean
```

```

Dim instance As ISimpleHoleFeatureData2
Dim value As System.Boolean
 
instance.AutoSelect = value
 
value = instance.AutoSelect
```

```

System.bool AutoSelect {get; set;}
```

```

property System.bool AutoSelect {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to automatically select all bodies, false to select specific bodies for [ISimpleHoleFeatureData2::FeatureScopeBodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2~FeatureScopeBodies.md) or [ISimpleHoleFeatureData2::IGetFeatureScopeBodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2~IGetFeatureScopeBodies.md)

Remarks

Th property is only available when [ISimpleHoleFeatureData2::FeatureScope](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2~FeatureScope.md) is true.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISimpleHoleFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2.md)  
[ISimpleHoleFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2_members.md)  
[ISimpleHoleFeatureData2::GetFeatureScopeBodiesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2~GetFeatureScopeBodiesCount.md)  
[ISimpleHoleFeatureData2::IGetFeatureScopeBodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2~IGetFeatureScopeBodies.md)
