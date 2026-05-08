# MergeFace Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData~MergeFace`

Gets or sets whether to merge the faces that are planar and coincident in the Flat-Pattern feature.
Gets or sets whether to merge the faces that are planar and coincident in the Flat-Pattern feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property MergeFace As System.Boolean
```

```

Dim instance As IFlatPatternFeatureData
Dim value As System.Boolean
 
instance.MergeFace = value
 
value = instance.MergeFace
```

```

System.bool MergeFace {get; set;}
```

```

property System.bool MergeFace {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True merges the faces, false does not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFlatPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData.md)  
[IFlatPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData_members.md)
