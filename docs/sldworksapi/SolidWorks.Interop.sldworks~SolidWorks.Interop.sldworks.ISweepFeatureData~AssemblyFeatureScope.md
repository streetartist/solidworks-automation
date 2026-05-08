# AssemblyFeatureScope Property (ISweepFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~AssemblyFeatureScope`

Gets and sets whether this swept-cut feature affects only selected components in the assembly.
Gets and sets whether this swept-cut feature affects only selected components in the assembly.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property AssemblyFeatureScope As System.Boolean
```

```

Dim instance As ISweepFeatureData
Dim value As System.Boolean
 
instance.AssemblyFeatureScope = value
 
value = instance.AssemblyFeatureScope
```

```

System.bool AssemblyFeatureScope {get; set;}
```

```

property System.bool AssemblyFeatureScope {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True if the swept-cutfeature affects only selected components in the assembly, false if affects all components in the assembly (**see Remarks**)

Remarks

Use this property, [ISweepFeatureData::AutoSelectComponents](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~AutoSelectComponents.md), and [ISweepFeatureData::PropagateFeatureToParts](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~PropagateFeatureToParts.md) to insert sweep cuts into an assembly.

This API works with ISweepFeatureData::AutoSelectComponents to configure the scope of an assembly sweep feature. This API performs the same configuration that is done in the Feature Scope section of the PropertyManager page of the sweep feature:

|  |  |  |
| --- | --- | --- |
| **AssemblyFeatureScope setting** | **AutoSelectComponents setting** | **PropertyManager page Feature Scope setting** |
| False | Ignored | All components selected  Auto-select not visible |
| True | If true, affected components are automatically selected  If false, manually select the affected components before calling this API | Selected components selected  If Auto-select is not checked, then manually select components |

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

Example

See the [ISweepFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISweepFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData.md)  
[ISweepFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData_members.md)
