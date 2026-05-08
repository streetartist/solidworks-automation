# Close Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~Close`

Gets or sets whether to close this loft feature.
Gets or sets whether to close this loft feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Close As System.Boolean
```

```

Dim instance As ILoftFeatureData
Dim value As System.Boolean
 
instance.Close = value
 
value = instance.Close
```

```

System.bool Close {get; set;}
```

```

property System.bool Close {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True for closed loft features, false for open

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ILoftFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData.md)  
[ILoftFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData_members.md)
