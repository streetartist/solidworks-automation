# FlipDimension Property (IAngleMateFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAngleMateFeatureData~FlipDimension`

Gets or sets whether to move entities to opposite sides of the dimension in this angle mate.
Gets or sets whether to move entities to opposite sides of the dimension in this angle mate.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property FlipDimension As System.Boolean
```

```

Dim instance As IAngleMateFeatureData
Dim value As System.Boolean
 
instance.FlipDimension = value
 
value = instance.FlipDimension
```

```

System.bool FlipDimension {get; set;}
```

```

property System.bool FlipDimension {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to flip the dimension, false to not

Example

See the [IAngleMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAngleMateFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAngleMateFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAngleMateFeatureData.md)  
[IAngleMateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAngleMateFeatureData_members.md)
