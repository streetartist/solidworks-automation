# UseReverse Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEndCapFeatureData~UseReverse`

Gets or sets whether to reverse the offset of this end cap feature.
Gets or sets whether to reverse the offset of this end cap feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property UseReverse As System.Boolean
```

```

Dim instance As IEndCapFeatureData
Dim value As System.Boolean
 
instance.UseReverse = value
 
value = instance.UseReverse
```

```

System.bool UseReverse {get; set;}
```

```

property System.bool UseReverse {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to reverse the offset, false to not

Example

See the [IEndCapFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEndCapFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IEndCapFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEndCapFeatureData.md)  
[IEndCapFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEndCapFeatureData_members.md)
