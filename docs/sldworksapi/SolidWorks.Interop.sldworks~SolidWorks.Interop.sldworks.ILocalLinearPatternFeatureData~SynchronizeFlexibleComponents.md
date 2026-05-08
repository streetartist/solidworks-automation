# SynchronizeFlexibleComponents Property (ILocalLinearPatternFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~SynchronizeFlexibleComponents`

Gets or sets whether to synchronize the movement of patterned flexible subassembly components with seed flexible subassembly components in this linear component pattern feature.
Gets or sets whether to synchronize the movement of patterned flexible subassembly components with seed flexible subassembly components in this linear component pattern feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property SynchronizeFlexibleComponents As System.Boolean
```

```

Dim instance As ILocalLinearPatternFeatureData
Dim value As System.Boolean
 
instance.SynchronizeFlexibleComponents = value
 
value = instance.SynchronizeFlexibleComponents
```

```

System.bool SynchronizeFlexibleComponents {get; set;}
```

```

property System.bool SynchronizeFlexibleComponents {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to synchronize the movement of patterned flexible subassembly components with seed flexible subassembly components, false to not

Remarks

This property is valid for a linear pattern of flexible subassemblies.

If this property is set to true, then when you move components in the seed flexible subassembly, components in the patterned flexible subassemblies also move, and vice versa.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

Example

See the [ILocalLinearPatternFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData.md) example.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ILocalLinearPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData.md)  
[ILocalLinearPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData_members.md)
