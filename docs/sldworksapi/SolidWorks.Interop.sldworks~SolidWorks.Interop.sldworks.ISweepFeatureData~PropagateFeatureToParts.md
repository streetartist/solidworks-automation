# PropagateFeatureToParts Property (ISweepFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~PropagateFeatureToParts`

Gets and sets whether to extend the swept-cut feature to all affected parts in the assembly.
Gets and sets whether to extend the swept-cut feature to all affected parts in the assembly.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property PropagateFeatureToParts As System.Boolean
```

```

Dim instance As ISweepFeatureData
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

True to extend the swept-cut feature to all affected parts in the assembly, false to not

Remarks

Use this property, [ISweepFeatureData::AssemblyFeatureScope](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~AssemblyFeatureScope.md), and [ISweepFeatureData::AutoSelectComponents](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~AutoSelectComponents.md) to insert sweep cuts into an assembly.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

Example

See the [ISweepFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISweepFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData.md)  
[ISweepFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData_members.md)
