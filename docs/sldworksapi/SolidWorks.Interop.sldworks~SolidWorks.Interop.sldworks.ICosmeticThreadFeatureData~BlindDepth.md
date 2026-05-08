# BlindDepth Property (ICosmeticThreadFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticThreadFeatureData~BlindDepth`

Gets or sets the depth of a blind cosmetic thread.
Gets or sets the depth of a blind cosmetic thread.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property BlindDepth As System.Double
```

```

Dim instance As ICosmeticThreadFeatureData
Dim value As System.Double
 
instance.BlindDepth = value
 
value = instance.BlindDepth
```

```

System.double BlindDepth {get; set;}
```

```

property System.double BlindDepth {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Depth of the cosmetic thread (see **Remarks**)

Remarks

If [ICosmeticThreadFeatureData::ApplyThread](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticThreadFeatureData~ApplyThread.md) is swApplyCosmeticThread\_Blind, then use this property to get or set the depth of the cosmetic thread.

Example

See the [ICosmeticThreadFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticThreadFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICosmeticThreadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticThreadFeatureData.md)  
[ICosmeticThreadFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticThreadFeatureData_members.md)
