# SymmetryPlane Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISymmetricMateFeatureData~SymmetryPlane`

Gets or sets the symmetry plane of this symmetry mate.
Gets or sets the symmetry plane of this symmetry mate.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property SymmetryPlane As System.Object
```

```

Dim instance As ISymmetricMateFeatureData
Dim value As System.Object
 
instance.SymmetryPlane = value
 
value = instance.SymmetryPlane
```

```

System.object SymmetryPlane {get; set;}
```

```

property System.Object^ SymmetryPlane {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

Front, Top, or Right plane or [IRefPlane](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane.md)

Example

See the [ISymmetricMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISymmetricMateFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISymmetricMateFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISymmetricMateFeatureData.md)  
[ISymmetricMateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISymmetricMateFeatureData_members.md)
