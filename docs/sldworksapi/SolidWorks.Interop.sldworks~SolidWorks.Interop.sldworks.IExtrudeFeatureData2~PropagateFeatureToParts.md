# PropagateFeatureToParts Property (IExtrudeFeatureData2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~PropagateFeatureToParts`

Gets whether to propagate this assembly extrude feature to the parts that it affects in this model.
Gets whether to propagate this assembly extrude feature to the parts that it affects in this model.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property PropagateFeatureToParts As System.Boolean
```

```

Dim instance As IExtrudeFeatureData2
Dim value As System.Boolean
 
instance.PropagateFeatureToParts = value
 
value = instance.PropagateFeatureToParts
```

```

System.bool PropagateFeatureToParts {get; set;}
```

```

property System.bool PropagateFeatureToParts {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to propagate this assembly extrude feature to the parts that it affects in the model, false to not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IExtrudeFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2.md)  
[IExtrudeFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2_members.md)  
[IExtrudeFeatureData2::AutoSelect Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~AutoSelect.md)  
[IExtrudeFeatureData2::AutoSelectComponents Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~AutoSelectComponents.md)  
[IExtrudeFeatureData2::AssemblyFeatureScope Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~AssemblyFeatureScope.md)
