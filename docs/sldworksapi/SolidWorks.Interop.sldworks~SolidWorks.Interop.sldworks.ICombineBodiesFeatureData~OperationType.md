# OperationType Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICombineBodiesFeatureData~OperationType`

Gets or sets how to combine multiple solid bodies for a combine feature.
Gets or sets how to combine multiple solid bodies for a combine feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property OperationType As System.Integer
```

```

Dim instance As ICombineBodiesFeatureData
Dim value As System.Integer
 
instance.OperationType = value
 
value = instance.OperationType
```

```

System.int OperationType {get; set;}
```

```

property System.int OperationType {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Type of combination as defined in [swCombineBodiesOperationType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCombineBodiesOperationType_e.html)

Example

[Combine Bodies (C#)](Combine_Bodies_Example_CSharp.htm)  
[Combine Bodies (VB.NET)](Combine_Bodies_Example_VBNET.htm)  
[Combine Bodies (VBA)](Combine_Bodies_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICombineBodiesFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICombineBodiesFeatureData.md)  
[ICombineBodiesFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICombineBodiesFeatureData_members.md)
