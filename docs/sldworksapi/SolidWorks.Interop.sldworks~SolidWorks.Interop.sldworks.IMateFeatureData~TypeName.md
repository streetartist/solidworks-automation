# TypeName Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateFeatureData~TypeName`

Gets or sets the type of this mate.
Gets or sets the type of this mate.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property TypeName As System.Integer
```

```

Dim instance As IMateFeatureData
Dim value As System.Integer
 
instance.TypeName = value
 
value = instance.TypeName
```

```

System.int TypeName {get; set;}
```

```

property System.int TypeName {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Mate type as defined in [swMateType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swMateType_e.html)

Example

See the [IMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMateFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateFeatureData.md)  
[IMateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateFeatureData_members.md)
