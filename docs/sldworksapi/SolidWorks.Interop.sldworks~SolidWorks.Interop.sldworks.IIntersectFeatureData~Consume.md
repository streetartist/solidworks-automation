# Consume Property (IIntersectFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIntersectFeatureData~Consume`

Gets or sets whether to remove input surfaces from the FeatureManager design tree.
Gets or sets whether to remove input surfaces from the FeatureManager design tree.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Consume As System.Boolean
```

```

Dim instance As IIntersectFeatureData
Dim value As System.Boolean
 
instance.Consume = value
 
value = instance.Consume
```

```

System.bool Consume {get; set;}
```

```

property System.bool Consume {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to remove input surfaces, false to not

Example

See the [IIntersectFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIntersectFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IIntersectFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIntersectFeatureData.md)  
[IIntersectFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIntersectFeatureData_members.md)
