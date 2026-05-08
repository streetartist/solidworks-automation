# ApplyThread Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticThreadFeatureData~ApplyThread`

Gets or sets how to apply the cosmetic thread.
Gets or sets how to apply the cosmetic thread.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ApplyThread As System.Integer
```

```

Dim instance As ICosmeticThreadFeatureData
Dim value As System.Integer
 
instance.ApplyThread = value
 
value = instance.ApplyThread
```

```

System.int ApplyThread {get; set;}
```

```

property System.int ApplyThread {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

How to apply the thread as defined in [swCosmeticThreadType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCosmeticThreadType_e.html) (see **Remarks**)

Remarks

If the value is swApplyCosmeticThread\_Blind, then call [ICosmeticThreadFeatureData::BlindDepth](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticThreadFeatureData~BlindDepth.md) to get or set the depth of the thread.

Example

See the [ICosmeticThreadFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticThreadFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICosmeticThreadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticThreadFeatureData.md)  
[ICosmeticThreadFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticThreadFeatureData_members.md)  
[ICosmeticThreadFeatureData::BlindDepth Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticThreadFeatureData~BlindDepth.md)
