# AutoSelectComponents Property (ISimpleHoleFeatureData2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2~AutoSelectComponents`

Gets or sets whether to auto-select all components that this assembly simple hole feature affects in model.
Gets or sets whether to auto-select all components that this assembly simple hole feature affects in model.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property AutoSelectComponents As System.Boolean
```

```

Dim instance As ISimpleHoleFeatureData2
Dim value As System.Boolean
 
instance.AutoSelectComponents = value
 
value = instance.AutoSelectComponents
```

```

System.bool AutoSelectComponents {get; set;}
```

```

property System.bool AutoSelectComponents {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to auto-select all affected components, false to not (use the selected components only or set [ISimpleHoleFeatureData2::AutoSelect](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2~AutoSelect.md) to true)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISimpleHoleFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2.md)  
[ISimpleHoleFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2_members.md)  
[ISimpleHoleFeatureData2::AssemblyFeatureScope Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2~AssemblyFeatureScope.md)  
[ISimpleHoleFeatureData2::PropagateFeatureToParts Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2~PropagateFeatureToParts.md)
