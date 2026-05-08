# MateAlignment Property (ISymmetricMateFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISymmetricMateFeatureData~MateAlignment`

Gets or sets the alignment of this symmetry mate.
Gets or sets the alignment of this symmetry mate.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property MateAlignment As System.Integer
```

```

Dim instance As ISymmetricMateFeatureData
Dim value As System.Integer
 
instance.MateAlignment = value
 
value = instance.MateAlignment
```

```

System.int MateAlignment {get; set;}
```

```

property System.int MateAlignment {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Mate alignment as defined in [swMateAlign\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swMateAlign_e.html)

Remarks

If this property is set to swMateAlign\_e:

- swMateAlignALIGNED, then vectors normal to the selected entities point in the same direction.
- swMateAlignANTI\_ALIGNED, then vectors normal to the selected entities point in opposite directions.

Example

See the [ISymmetricMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISymmetricMateFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISymmetricMateFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISymmetricMateFeatureData.md)  
[ISymmetricMateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISymmetricMateFeatureData_members.md)
