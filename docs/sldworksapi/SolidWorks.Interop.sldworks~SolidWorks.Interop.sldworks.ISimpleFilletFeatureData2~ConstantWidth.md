# ConstantWidth Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~ConstantWidth`

Gets or sets whether this simple fillet has a constant width.
Gets or sets whether this simple fillet has a constant width.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ConstantWidth As System.Boolean
```

```

Dim instance As ISimpleFilletFeatureData2
Dim value As System.Boolean
 
instance.ConstantWidth = value
 
value = instance.ConstantWidth
```

```

System.bool ConstantWidth {get; set;}
```

```

property System.bool ConstantWidth {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True if simple fillet has constant width, false if not

Example

See [ISimpleFilletFeatureData2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISimpleFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2.md)  
[ISimpleFilletFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2_members.md)
