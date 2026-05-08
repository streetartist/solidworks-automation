# SynchronizeFlexibleComponents Property (ILocalCircularPatternFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData~SynchronizeFlexibleComponents`

Gets or sets whether to synchronize the movement of flexible subassembly components in this circular component pattern feature.
Gets or sets whether to synchronize the movement of flexible subassembly components in this circular component pattern feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property SynchronizeFlexibleComponents As System.Boolean
```

```

Dim instance As ILocalCircularPatternFeatureData
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

True to synchronize the movement of flexible subassembly components, false to not

Remarks

If this property is set to true, then when you move components in the seed flexible subassembly, components in the patterned instances move, and vice versa.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ILocalCircularPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData.md)  
[ILocalCircularPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData_members.md)
