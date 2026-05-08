# EndCondition Property (ICosmeticThreadFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticThreadFeatureData~EndCondition`

Gets or sets the thread end condition.
Gets or sets the thread end condition.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property EndCondition As System.Integer
```

```

Dim instance As ICosmeticThreadFeatureData
Dim value As System.Integer
 
instance.EndCondition = value
 
value = instance.EndCondition
```

```

System.int EndCondition {get; set;}
```

```

property System.int EndCondition {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Thread end condition as defined in [swCosmeticEndConditions\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCosmeticEndConditions_e.html)

Example

See the [ICosmeticThreadFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticThreadFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICosmeticThreadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticThreadFeatureData.md)  
[ICosmeticThreadFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticThreadFeatureData_members.md)
