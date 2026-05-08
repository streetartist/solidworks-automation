# CutDirection Property (IIndentFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIndentFeatureData~CutDirection`

Gets or sets whether to flip the side of the cut for this indent feature.
Gets or sets whether to flip the side of the cut for this indent feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property CutDirection As System.Boolean
```

```

Dim instance As IIndentFeatureData
Dim value As System.Boolean
 
instance.CutDirection = value
 
value = instance.CutDirection
```

```

System.bool CutDirection {get; set;}
```

```

property System.bool CutDirection {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to flip the side of the cut, false to not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IIndentFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIndentFeatureData.md)  
[IIndentFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIndentFeatureData_members.md)  
[IIndentFeatureData::IsCut Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIndentFeatureData~IsCut.md)
