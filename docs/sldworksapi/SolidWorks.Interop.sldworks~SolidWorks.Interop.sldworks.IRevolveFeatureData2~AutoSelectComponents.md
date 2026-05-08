# AutoSelectComponents Property (IRevolveFeatureData2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2~AutoSelectComponents`

Gets or sets whether to auto-select all components that this assembly revolve feature affects in model.
Gets or sets whether to auto-select all components that this assembly revolve feature affects in model.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property AutoSelectComponents As System.Boolean
```

```

Dim instance As IRevolveFeatureData2
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

True to auto-select all affected components, false to not (use the selected components only or set [IRevolveFeatureData2::AutoSelect](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2~AutoSelect.md) to true)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRevolveFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2.md)  
[IRevolveFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2_members.md)  
[IRevolveFeatureData2::AssemblyFeatureScope Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2~AssemblyFeatureScope.md)  
[IRevolveFeatureData2::PropagateFeatureToParts Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2~PropagateFeatureToParts.md)
